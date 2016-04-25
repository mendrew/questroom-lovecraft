#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import random
from collections import Counter
from copy import copy
from threading import Timer
# import pygame

from settings import Devices, DEVICES_TABLE

def REQ_QUEST_INIT(master, task, game_state):
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, [0,0,0,0])

    # AC_ENABLE_INIT_LIGHTS(master, task, game_state)
    # Add Table clock job
    game_state.add_active_task_with_id(TASKS_IDS.BACKGROUND_TABLE_CLOCK)

    return True

def REQ_BACKGROUND_TABLE_CLOCK(master, task, game_state):
    INITIALIZATION_SET_TIME = 30
    INITIALIZATION_UNSET_TIME = 20 + INITIALIZATION_SET_TIME
    MINIMUM_CLOCK_CYCLE_MOVE_TIME = 12
    CLOCK_CHANGE_PERIOD = 5 * 60
    clock_ctrl = master.getSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME).get()


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
        master.setSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        stack.append(clock_last_change_time)
        stack.append(start_time)
        return
    elif time_passed < INITIALIZATION_UNSET_TIME:
        # Clear ZERO CMD around 20 sec
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 0
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
        master.setSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        stack.append(clock_last_change_time)
        stack.append(start_time)
        return
    else:
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 0
        master.setSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME, clock_ctrl)

    change_clock_time_passed = time.time() - clock_last_change_time

    if change_clock_time_passed > CLOCK_CHANGE_PERIOD:
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
        master.setSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        clock_last_change_time = time.time()

    stack.append(clock_last_change_time)
    stack.append(start_time)

def AC_ADD_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_STATUE_ON_LORDS_TABLE)

def REQ_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    PUT_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_RANGE

    lords_table_value = master.getAdc(
            Devices.LOVECRAFT_DEVICE_NAME).get()[DEVICES_TABLE.ADC_LORDS_TABLE_STATUE]
    if PUT_RANGE[0] <= lords_table_value <= PUT_RANGE[1]:
        return True

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
    for index, coin_value in adc_coins_values:
        if DEVICES_TABLE.COIN_INSERTED_RANGE(0) <= coin_value <= DEVICES_TABLE.COIN_INSERTED_RANGE(1):
            inserted_coins_number = inserted_coins_number + 1

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
    clock_ctrl = master.getSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME).get()

    clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
    master.setSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME, clock_ctrl)
    time.sleep(0.5)

    clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 0
    master.setSimpleLeds(DEVICES_TABLE.LOVECRAFT_DEVICE_NAME, clock_ctrl)
    pass

def AC_ADD_CLOCK_SYNCHRONIZATION(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CLOCK_SYNCHRONIZATION)

def REQ_CLOCK_SYNCHRONIZATION(master, task, game_state):
    pass
    return True

def AC_BOX_UNDER_CLOCK_FACE_OPEN(master, task, game_state):
    # What box is opened ?
    pass

def ADD_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.FAMILY_PICTURE_BARLEY_BREAK)

def REQ_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    pass

def AC_SECOND_COIN_FALL(master, task, game_state):
    pass

def ADD_PUT_SECOND_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_SECOND_COIN)

def REQ_PUT_SECOND_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 2)
