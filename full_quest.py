#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import random
from collections import Counter
from copy import copy
from threading import Timer
# import pygame

from settings import Devices, DEVICES_TABLE, TASKS_IDS

class GLOBAL_VARIABLES:
    TABLE_CLOCK_VALUE = 0
    WALL_CLOCK_INIT_VALUE = 0

def REQ_QUEST_INIT(master, task, game_state):
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, [0,0,0,0])

    # AC_ENABLE_INIT_LIGHTS(master, task, game_state)


    return True

def TABLE_CLOCK_UP(master):
    if GLOBAL_VARIABLES.TABLE_CLOCK_VALUE == 12:
        GLOBAL_VARIABLES.TABLE_CLOCK_VALUE = 0
    GLOBAL_VARIABLES.TABLE_CLOCK_VALUE = GLOBAL_VARIABLES.TABLE_CLOCK_VALUE + 2

    clock_ctrl = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    next_time_cmd = clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD]
    next_time_cmd = ~next_time_cmd & 0x1
    clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = next_time_cmd

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)
    print("Value of table clock is: {}".format(GLOBAL_VARIABLES.TABLE_CLOCK_VALUE))

def AC_ADD_BACKGROUND_TABLE_CLOCK_JOB(master, tas, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.BACKGROUND_TABLE_CLOCK)


def REQ_BACKGROUND_TABLE_CLOCK(master, task, game_state):
    INITIALIZATION_SET_TIME = 30
    INITIALIZATION_UNSET_TIME = 20 + INITIALIZATION_SET_TIME
    CLOCK_CHANGE_PERIOD = 5 * 60

    # debug values
    # INITIALIZATION_SET_TIME = 0
    # INITIALIZATION_UNSET_TIME = 2 + INITIALIZATION_SET_TIME
    # CLOCK_CHANGE_PERIOD = 1 * 2

    clock_ctrl = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()

    stack = task.stack
    if stack == []:
        start_time = time.time()
        clock_last_change_time = start_time + INITIALIZATION_UNSET_TIME + 1
    else:
        start_time = stack.pop()
        clock_last_change_time = stack.pop()


    time_passed = time.time() - start_time
    if time_passed < INITIALIZATION_SET_TIME:
        # Signals ZERO and NEXT CMD to SET
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 1
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        stack.append(clock_last_change_time)
        stack.append(start_time)
        return
    elif time_passed < INITIALIZATION_UNSET_TIME:
        # Clear ZERO CMD around 20 sec
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 0
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        stack.append(clock_last_change_time)
        stack.append(start_time)
        return

    change_clock_time_passed = time.time() - clock_last_change_time

    if change_clock_time_passed > CLOCK_CHANGE_PERIOD:
        TABLE_CLOCK_UP(master)

        clock_last_change_time = time.time()

    stack.append(clock_last_change_time)
    stack.append(start_time)

def AC_REMEMBER_WALL_CLOCK_INIT_VALUE(master, task, game_state):
    encoders = master.getEncoders(Devices.LOVECRAFT_DEVICE_NAME).get()

    wall_clock_init_value = encoders[DEVICES_TABLE.WALL_CLOCK]
    GLOBAL_VARIABLES.WALL_CLOCK_INIT_VALUE = wall_clock_init_value

    print("Wall Clock Init value: {}".format(wall_clock_init_value))

def AC_ADD_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_STATUE_ON_LORDS_TABLE)

def REQ_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    PUT_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_RANGE
    NONE_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_NONE_RANGE

    lords_table_value = master.getAdc(
            Devices.LOVECRAFT_DEVICE_NAME).get()[DEVICES_TABLE.ADC_LORDS_TABLE_STATUE]
    if PUT_RANGE[0] <= lords_table_value <= PUT_RANGE[1]:
        return True
    elif NONE_RANGE[0] <= lords_table_value <= NONE_RANGE[1]:
        # it's ok. statue just absent
        pass
    else:
        # error - puzzle is broken
        if not master.debugMode():
            print("ERROR: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(lords_table_value))

    return False

def AC_TURN_LORDS_TABLE(master, task, game_state):
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = 1
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

def AC_ADD_PUT_FIRST_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_FIRST_COIN)

def check_coins_inserted(master, task, game_state, nubmer_of_coins):
    adc_list = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()

    adc_coins_values = (adc_list[DEVICES_TABLE.COIN_1],
            adc_list[DEVICES_TABLE.COIN_2],
            adc_list[DEVICES_TABLE.COIN_3],
            adc_list[DEVICES_TABLE.COIN_4])

    inserted_coins_number = 0
    for index, coin_value in enumerate(adc_coins_values):
        if DEVICES_TABLE.COIN_INSERTED_RANGE[0] <= coin_value <= DEVICES_TABLE.COIN_INSERTED_RANGE[1]:
            inserted_coins_number = inserted_coins_number + 1
        elif DEVICES_TABLE.COIN_NONE_RANGE[0] <= coin_value <= DEVICES_TABLE.COIN_NONE_RANGE[1]:
            # all ok, just monet not inserted
            pass
        else:
            if not master.debugMode():
                print("ERROR: check_coins_inserted coin_id {} value: {}".format(index, coin_value)) 
    if inserted_coins_number >= nubmer_of_coins:
        return True
    return False


def REQ_PUT_FIRST_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 1)

#!!!
def AC_BAKE_FLARE_UP(master, task, game_state):
    pass

def AC_PERFORMANCE_DOLL_GIFT(master, task, game_state):
    pass

def AC_POLTERGEISTS(master, task, game_state):
    pass

def AC_FALLING_BOOKS(master, task, game_state):
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_PUSH] = 1
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

def AC_FALLING_FISHING_RODS(master, task, game_state):
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_FISHING_RODS_HOLDERS] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def AC_ADD_COLLECT_DAD_FISHING(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.COLLECT_DAD_FISHING)

def REQ_COLLECT_DAD_FISHING(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    dad_collected = buttons[DEVICES_TABLE.BTN_COLLECT_DAD_FISHING]

    return dad_collected

def AC_RING_OUT_THE_CLOCK(master, task, game_state):
    pass

def AC_TABLE_CLOCK_CHANGE_TIME(master, task, game_state):
    # Time must set to random value
    TABLE_CLOCK_UP(master)

def AC_ADD_CLOCK_SYNCHRONIZATION(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CLOCK_SYNCHRONIZATION)

def REQ_CLOCK_SYNCHRONIZATION(master, task, game_state):
    if task.stack == []:
        task.stack.append([GLOBAL_VARIABLES.WALL_CLOCK_INIT_VALUE])
        task.stack.append(time.time())

    last_time = task.stack.pop()
    time_passed = time.time() - last_time
    if time_passed < 1:
        task.stack.append(last_time)
        return

    wall_clock_values_list = task.stack.pop()
    last_value = wall_clock_values_list[-1]

    encoders = master.getEncoders(Devices.LOVECRAFT_DEVICE_NAME).get()
    wall_clock_value = encoders[DEVICES_TABLE.WALL_CLOCK]

    if last_value != wall_clock_value:
        wall_clock_values_list.append(wall_clock_value)

        print("REQ_CLOCK_SYNCHRONIZATION: late value: {}, new_value: {}".format(last_value, wall_clock_value))
        print("REQ_CLOCK_SYNCHRONIZATION: list {}".format(wall_clock_values_list))

        # !!!
        # convert value to time and compare with table clock

    task.stack.append(wall_clock_values_list)
    # save time
    current_time = time.time()
    task.stack.append(current_time)

    return False

def AC_BOX_UNDER_CLOCK_FACE_OPEN(master, task, game_state):
    # What box is opened ? On Device table looks like it not my job
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_PICTURE] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def ADD_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.FAMILY_PICTURE_BARLEY_BREAK)

def REQ_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    puzzle_collected = buttons[DEVICES_TABLE.BTN_PICTURE_BARLEY_BREAK]

    return puzzle_collected

def AC_SECOND_COIN_FALL(master, task, game_state):
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_COIN] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def ADD_PUT_SECOND_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_SECOND_COIN)

def REQ_PUT_SECOND_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 2)
