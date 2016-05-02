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
    TABLE_CLOCK_LAST_CHANGE_TIME = time.time()

    WALL_CLOCK_REAL_12 = 0

def puzzle_status(puzzle_name, status):
    PUZZLE_OK_MSG = "\tOK"
    PUZZLE_ERROR_MSG = "\tERROR"

    if status:
        print("{pname}: {msg}".format(pname=puzzle_name, msg=PUZZLE_OK_MSG))
    else:
        print("{pname}: {msg}".format(pname=puzzle_name, msg=PUZZLE_ERROR_MSG))


def check_puzzles(master):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()

    # check bottles
    print("Puzzle status:")
    puzzle_status("BOTTLES", buttons[DEVICES_TABLE.BTN_BOTTLES] == 0)

    knife_slots = []
    for slot_index in range(len(DEVICES_TABLE.BTN_KNIFE_SLOTS)):
        knife_slots.append(
                buttons[ DEVICES_TABLE.BTN_KNIFE_SLOTS[slot_index] ])
    puzzle_status("KNIFE_SLOTS: {}".format(knife_slots), knife_slots == [0]*5)

    # # check monets
    # adc_list = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()
    # adc_coins_values = (adc_list[DEVICES_TABLE.COIN_1],
    #         adc_list[DEVICES_TABLE.COIN_2],
    #         adc_list[DEVICES_TABLE.COIN_3],
    #         adc_list[DEVICES_TABLE.COIN_4])
    #
    # inserted_coins_number = 0
    # for index, coin_value in enumerate(adc_coins_values):
    #     print("REQ: check_coins_inserted coin_id {} value: {}".format(index, coin_value))
    #     if DEVICES_TABLE.COIN_INSERTED_RANGE[0] <= coin_value <= DEVICES_TABLE.COIN_INSERTED_RANGE[1]:
    #         inserted_coins_number = inserted_coins_number + 1
    #     elif DEVICES_TABLE.COIN_NONE_RANGE[0] <= coin_value <= DEVICES_TABLE.COIN_NONE_RANGE[1]:
    #         # all ok, just monet not inserted
    #         pass
    #     else:
    #         pass
    #

def REQ_QUEST_INIT(master, task, game_state):
    # close all boxes
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_COIN] = DEVICES_TABLE.CLOSE
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_PICTURE] = DEVICES_TABLE.CLOSE
    # sl_controlls[DEVICES_TABLE.SL_CODE_LOCKS_LOCKER_LOCK] = DEVICES_TABLE.CLOSE
    # sl_controlls[DEVICES_TABLE.SL_BOX_IN_CLOSET_WITH_KNIFE] = DEVICES_TABLE.CLOSE
    # sl_controlls[DEVICES_TABLE.SL_BOX_UNDER_PICTURE] = DEVICES_TABLE.CLOSE
    for scare_index in DEVICES_TABLE.SL_SCARE_IN_LOCKER:
        sl_controlls[scare_index] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    # init colors
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    for smart_index in range(0,20):
        smart_leds.setOneLed(smart_index, [0x0, 0x0, 0x0])
    # smart_leds.setOneLed(17, [0x000, 0x0, 0x0])
    # smart_leds.setOneLed(18, [0x000, 0x0, 0x0])

    # init doors
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    # relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.OPEN
    # relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_WITH_SKELET] = DEVICES_TABLE.CLOSE
    # master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

    # init GODS table
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = DEVICES_TABLE.OPEN
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)
    time.sleep(10)
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = DEVICES_TABLE.CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

    # check_puzzles
    check_puzzles(master)

    return True

def TABLE_CLOCK_UP(master):

    clock_ctrl = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    next_time_cmd = clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD]
    next_time_cmd = ~next_time_cmd & 0x1
    clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = next_time_cmd

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)

    GLOBAL_VARIABLES.TABLE_CLOCK_VALUE = GLOBAL_VARIABLES.TABLE_CLOCK_VALUE + 2
    GLOBAL_VARIABLES.TABLE_CLOCK_LAST_CHANGE_TIME = time.time()

    if GLOBAL_VARIABLES.TABLE_CLOCK_VALUE == 12:
        GLOBAL_VARIABLES.TABLE_CLOCK_VALUE = 0

    print("TABLE CLOCK VALUE: {}".format(GLOBAL_VARIABLES.TABLE_CLOCK_VALUE))

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
        GLOBAL_VARIABLES.TABLE_CLOCK_LAST_CHANGE_TIME = start_time + INITIALIZATION_UNSET_TIME + 1
    else:
        start_time = stack.pop()

    time_passed = time.time() - start_time
    if time_passed < INITIALIZATION_SET_TIME:
        # Signals ZERO and NEXT CMD to SET
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 1
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        stack.append(start_time)
        return
    elif time_passed < INITIALIZATION_UNSET_TIME:
        # Clear ZERO CMD around 20 sec
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 0
        clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)

        stack.append(start_time)
        return

    change_clock_time_passed = time.time() - GLOBAL_VARIABLES.TABLE_CLOCK_LAST_CHANGE_TIME

    if change_clock_time_passed > CLOCK_CHANGE_PERIOD:
        TABLE_CLOCK_UP(master)

    stack.append(start_time)

def AC_ADD_BACKGROUND_WALL_CLOCK_INIT(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.BACKGROUND_WALL_CLOCK_INIT)

def REQ_BACKGROUND_WALL_CLOCK_INIT(master, task, game_state):
    # time to set 12 o'clock
    INITIALIZATION_SET_12_TIME = 20

    stack = task.stack
    if stack == []:
        start_time = time.time()
    else:
        start_time = stack.pop()

    time_passed = time.time() - start_time
    if time_passed < INITIALIZATION_SET_12_TIME:
        # just wait till time pass
        stack.append(start_time)
        return

    encoders = master.getEncoders(Devices.LOVECRAFT_DEVICE_NAME).get()
    GLOBAL_VARIABLES.WALL_CLOCK_REAL_12 = encoders[DEVICES_TABLE.WALL_CLOCK]
    print("WALL_CLOCK_INIT_12_VALUE: {}".format(GLOBAL_VARIABLES.WALL_CLOCK_REAL_12))

    return True


def REQ_BACKGROUND_PICTURE_MOVES(master, task, game_state):
    # INITIALIZATION_SET_TIME = 30
    # INITIALIZATION_UNSET_TIME = 20 + INITIALIZATION_SET_TIME
    # PICTURE_CHANGE_PERIOD = 15 * 60
    #
    # debug values
    INITIALIZATION_SET_TIME = 0
    INITIALIZATION_UNSET_TIME = 2 + INITIALIZATION_SET_TIME
    CLOCK_CHANGE_PERIOD = 1 * 2
    #
    # clock_ctrl = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    #
    stack = task.stack
    if stack == []:
        start_time = time.time()
        clock_last_change_time = start_time + INITIALIZATION_UNSET_TIME + 1
    else:
        start_time = stack.pop()
        clock_last_change_time = stack.pop()


    time_passed = time.time() - start_time
    if time_passed < INITIALIZATION_SET_TIME:
        pass
    #     # Signals ZERO and NEXT CMD to SET
    #     clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 1
    #     clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
    #     master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)
    #
    #     stack.append(clock_last_change_time)
    #     stack.append(start_time)
    #     return
    elif time_passed < INITIALIZATION_UNSET_TIME:
        pass
    #     # Clear ZERO CMD around 20 sec
    #     clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_ZERO_CMD] = 0
    #     clock_ctrl[DEVICES_TABLE.SL_TABLE_CLOCK_NEXT_TIME_CMD] = 1
    #     master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, clock_ctrl)
    #
    #     stack.append(clock_last_change_time)
    #     stack.append(start_time)
    #     return
    #
    # change_clock_time_passed = time.time() - clock_last_change_time
    #
    if change_clock_time_passed > PICTURE_CHANGE_PERIOD:
        pass
    #     TABLE_CLOCK_UP(master)
    #
        clock_last_change_time = time.time()
        print("(REQ:{task_id}) Change picture".format(task_id=task.id))
    #
    stack.append(clock_last_change_time)
    stack.append(start_time)

def AC_ADD_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_STATUE_ON_LORDS_TABLE)

def REQ_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    PUT_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_RANGE
    NONE_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_NONE_RANGE

    lords_table_value = master.getAdc(
            Devices.LOVECRAFT_DEVICE_NAME).get()[DEVICES_TABLE.ADC_LORDS_TABLE_STATUE]
    if PUT_RANGE[0] <= lords_table_value <= PUT_RANGE[1]:
        print("YES: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(lords_table_value))
        return True
    elif NONE_RANGE[0] <= lords_table_value <= NONE_RANGE[1]:
        print("NONE: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(lords_table_value))
        # it's ok. statue just absent
        pass
    else:
        # error - puzzle is broken
        if not master.debugMode():
            print("ERROR: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(lords_table_value))

    return False

def AC_TURN_LORDS_TABLE(master, task, game_state):
    print("(ACTION:{task_id})We turn lords table".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = DEVICES_TABLE.OPEN
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
        print("REQ: check_coins_inserted coin_id {} value: {}".format(index, coin_value))
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
    time.sleep(5)
    return check_coins_inserted(master, task, game_state, 1)

#!!!
def AC_BAKE_FLARE_UP(master, task, game_state):
    print("(ACTION:{task_id}) Bake flare up".format(task_id=task.id))
    pass

def AC_PERFORMANCE_DOLL_GIFT(master, task, game_state):
    print("(ACTION:{task_id}) Performance - doll gift".format(task_id=task.id))
    pass

def AC_POLTERGEISTS(master, task, game_state):
    print("(ACTION:{task_id}) Poltergeists".format(task_id=task.id))
    pass

def AC_FALLING_BOOKS(master, task, game_state):
    print("(ACTION:{task_id}) Falling books".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_PUSH] = DEVICES_TABLE.CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)
    time.sleep(1.5)
    relays[DEVICES_TABLE.RELAY_PUSH] = 0
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

def AC_FALLING_FISHING_RODS(master, task, game_state):
    print("(ACTION:{task_id}) Falling fishing rods".format(task_id=task.id))
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
    print("(ACTION:{task_id}) Ring out the clock".format(task_id=task.id))
    pass

def AC_TABLE_CLOCK_CHANGE_TIME(master, task, game_state):
    print("(ACTION:{task_id}) Table clock change time".format(task_id=task.id))
    # Time must set to random value
    TABLE_CLOCK_UP(master)

def AC_ADD_CLOCK_SYNCHRONIZATION(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CLOCK_SYNCHRONIZATION)

def REQ_CLOCK_SYNCHRONIZATION(master, task, game_state):
    if task.stack == []:
        task.stack.append([GLOBAL_VARIABLES.WALL_CLOCK_REAL_12])
        task.stack.append(time.time())

    last_time = task.stack.pop()
    time_passed = time.time() - last_time
    if time_passed < 0.1:
        task.stack.append(last_time)
        return

    wall_clock_values_list = task.stack.pop()
    wall_clock_last_value = wall_clock_values_list[-1]

    encoders = master.getEncoders(Devices.LOVECRAFT_DEVICE_NAME).get()
    wall_clock_value = encoders[DEVICES_TABLE.WALL_CLOCK]


    if wall_clock_last_value == wall_clock_value:
        task.stack.append(wall_clock_values_list)
        task.stack.append(time.time())
        return

    # choose clock direction
    delta_time = GLOBAL_VARIABLES.WALL_CLOCK_REAL_12 - wall_clock_value
    if wall_clock_last_value > 1000 and wall_clock_value < 100:
        clockwise_direction = False
    elif wall_clock_last_value < 100 and wall_clock_value > 1000:
        clockwise_direction = True
    elif wall_clock_value > wall_clock_last_value:
        clockwise_direction = True
    else:
        clockwise_direction = False

    delta_time = abs(delta_time)

    if clockwise_direction:
        wall_clock_time = 0 + delta_time/2 - int((delta_time/2)/12) * 12
    else:
        wall_clock_time = 12 - (delta_time/2 - int((delta_time/2)/12) * 12 )

    if wall_clock_time == 12:
        wall_clock_time = 0

    print("Wall clock TIME: {}".format(wall_clock_time))

    wall_clock_values_list.append(wall_clock_value)

    print("REQ_CLOCK_SYNCHRONIZATION: wall late value: {}, new_value: {}  init_real {}".format(wall_clock_last_value, wall_clock_value, GLOBAL_VARIABLES.WALL_CLOCK_REAL_12))
    print("REQ_CLOCK_SYNCHRONIZATION: wall list {}".format(wall_clock_values_list))
    print("REQ_CLOCK_SYNCHRONIZATION: table time: {}, wall time: {}".format(GLOBAL_VARIABLES.TABLE_CLOCK_VALUE, wall_clock_time))

    # if GLOBAL_VARIABLES.TABLE_CLOCK_VALUE ==  wall_clock_time:
    #     print("(REQ:{task_id}) Clocks sync!".format(task_id=task.id))
    #     return True

    task.stack.append(wall_clock_values_list)
    # save time
    current_time = time.time()
    task.stack.append(current_time)

    return False

def AC_BOX_UNDER_CLOCK_FACE_OPEN(master, task, game_state):
    print("(ACTION:{task_id}) Lock under clock face opened".format(task_id=task.id))
    # What box is opened ? On Device table looks like it not my job
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_PICTURE] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def ADD_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.FAMILY_PICTURE_BARLEY_BREAK)

def REQ_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    puzzle_collected = buttons[DEVICES_TABLE.BTN_PICTURE_BARLEY_BREAK]

    return puzzle_collected

def AC_SECOND_COIN_FALL(master, task, game_state):
    print("(ACTION:{task_id}) Second coin fall from clock".format(task_id=task.id))
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_COIN] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def ADD_PUT_SECOND_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_SECOND_COIN)

def REQ_PUT_SECOND_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 2)

def AC_PERFORMANCE_YOU_NOT_MY_FATHER(master, task, game_state):
    print("(ACTION:{task_id}) Performance - you not my father".format(task_id=task.id))
    pass

def AC_STRENGTHENING_OF_PRESENCE(master, task, game_state):
    # усиление присутствия
    print("(ACTION:{task_id}) Feel of strengthening presence".format(task_id=task.id))
    # LEDS and what else
    pass

def AC_ADD_CODE_LOCK(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CODE_LOCK)

def AC_SPIDERS_RUNNING(master, task, game_state):
    print("(ACTION:{task_id}) Spiders running".format(task_id=task.id))
    pass

def AC_SCARE_IN_LOCKER(master, task, game_state):
    print("(ACTION:{task_id}) Scare in LOCKER".format(task_id=task.id))

    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    for scare_index in DEVICES_TABLE.SL_SCARE_IN_LOCKER:
        sl_controlls[scare_index] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    time.sleep(2)

    for scare_index in DEVICES_TABLE.SL_SCARE_IN_LOCKER:
        sl_controlls[scare_index] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def REQ_CODE_LOCK(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()

    code_buttons = buttons[DEVICES_TABLE.BTN_CODE_LOCKS_CODE_BUTTONS]
    else_buttons = buttons[DEVICES_TABLE.BTN_CODE_LOCKS_ELSE_BUTTONS]

    return code_buttons and not else_buttons

def AC_LOCKER_OPEN(master, task, game_state):
    print("(ACTION:{task_id}) Code lock opened".format(task_id=task.id))
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_CODE_LOCKS_LOCKER_LOCK] = DEVICES_TABLE.OPEN

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def AC_ADD_KUNSTKAMERA(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.ONCOMING_TO_KUNSTKAMERA)
    game_state.add_active_task_with_id(TASKS_IDS.PLACE_THE_BOTTLES)


def REQ_ONCOMING_TO_KUNSTKAMERA(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()

    head_sensor = buttons[DEVICES_TABLE.BTN_HEAD_SENSOR]
    return head_sensor

def AC_OCTOPUS_SPIT_LIQUID(master, task, game_state):
    print("(ACTION:{task_id}) Octopus spit liquid".format(task_id=task.id))
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP_1] = 1
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP_2] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    time.sleep(5)
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP_1] = 0
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP_2] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    # maybe here play sound or in external action

def AC_PLAY_OCTOPUS_SPRUT(master, task, game_state):
    print("(ACTION:{task_id}) Octopus sprut sound".format(task_id=task.id))
    pass


def REQ_PLACE_THE_BOTTLES(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()

    bottles_placed = buttons[DEVICES_TABLE.BTN_BOTTLES]

    return bottles_placed

def AC_PUMPS_WATER(master, task, game_state):
    print("(ACTION:{task_id}) Pumps water | where pump? Ask Alexey".format(task_id=task.id))
    # maybe pump used one of eyes leds
    # sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    # sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP_2] = 1
    #
    # master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    pass

def AC_ADD_PUT_THIRD_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_THIRD_COIN)

def REQ_PUT_THIRD_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 3)

def AC_ADD_CLOSE_THE_DOOR(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CLOSE_THE_DOOR)

def REQ_CLOSE_THE_DOOR(master, task, game_state):
    TIME_TO_CLOSE_THE_DOOR = 15
    TIME_TO_OPEN_THE_DOOR = 90
    TIME_WAIT_TO_OPEN = 10
    # initialization
    if task.stack == []:
        # set motor to start close the door
        print("(REQ:{task_id}) Try to close door in closet | wait {time} sec.".format(task_id=task.id, time=TIME_TO_CLOSE_THE_DOOR))
        relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
        relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.CLOSE
        master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)


        close_start_time = time.time()
        task.stack.append(close_start_time)
        wait_till_action = False
        task.stack.append(wait_till_action)

    wait_till_action = task.stack.pop()
    close_start_time = task.stack.pop()
    passed_time = time.time() - close_start_time

    if passed_time >= TIME_TO_CLOSE_THE_DOOR:
        # check door lock
        # if players start play
        buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
        # if door closed
        if not buttons[DEVICES_TABLE.BTN_DOOR_OPEN]:

            return True
        else:
            # door not closed - open
            relays_value[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.OPEN
            relays.set(relays_value)

            close_start_time = time.time()

    task.stack.append(close_start_time)
    task.stack.append(wait_till_action)
    return False


def AC_PARANORMAL_ACTIVITY(master, task, game_state):
    print("(ACTION:{task_id}) Paranormal activity".format(task_id=task.id))
    pass

def AC_PERFORMANCE_GIRL_GONE(master, task, game_state):
    print("(ACTION:{task_id}) Performance - girl gone".format(task_id=task.id))
    pass

def AC_ADD_ANOMALOUS_PHENOMENA(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.ANOMALOUS_PHENOMENA_LEDS)
    game_state.add_active_task_with_id(TASKS_IDS.ANOMALOUS_PHENOMENA_ENTER_NUMBERS)

def REQ_ANOMALOUS_PHENOMENA_LEDS(master, task, game_state):
    return True

def REQ_ANOMALOUS_PHENOMENA_ENTER_NUMBERS(master, task, game_state):
    adcs = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()
    number_1 = adcs[DEVICES_TABLE.BOX_LOCK_SYMBOL_1]
    number_2 = adcs[DEVICES_TABLE.BOX_LOCK_SYMBOL_2]
    number_3 = adcs[DEVICES_TABLE.BOX_LOCK_SYMBOL_3]

    if not master.debugMode():
        print("ANOMALOUS_PHENOMENA_ENTER_NUMBERS:\n number1: {}\tnumber2: {}\tnumber3: {}".format(
            number_1, number_2, number_3))

    number_ok_1 = True if number_1 == DEVICES_TABLE.SYMBOL_1_VALUE else False
    number_ok_2 = True if number_2 == DEVICES_TABLE.SYMBOL_2_VALUE else False
    number_ok_3 = True if number_3 == DEVICES_TABLE.SYMBOL_3_VALUE else False

    return number_ok_1 and number_ok_2 and number_ok_3


def AC_OPEN_CLOSET_BOX_WITH_KNIFE(master, task, game_state):
    print("(ACTION:{task_id}) Closet box with knife opened".format(task_id=task.id))
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_BOX_IN_CLOSET_WITH_KNIFE] = DEVICES_TABLE.OPEN

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def AC_ADD_MARINE_TROPHIES(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.MARINE_TROPHIES)

class Colors:
    WHITE = [0xff, 0xff, 0xff]
    RED = [0xff, 0, 0]
    LIGHT_RED = [0xff, 33, 33]
    GREEN = [0, 0xff, 0]
    LIGHT_GREEN = [33, 0xff, 33]
    BLUE = [0, 0, 0xff]
    NONE = [0, 0, 0]

class pColors:
    RED = Colors.RED
    GREEN = Colors.GREEN
    BLUE = Colors.BLUE

def toggleEyeColor(color):
    if pColors.GREEN == color:
        color = pColors.BLUE
    elif pColors.BLUE == color:
        color = pColors.RED
    else:
        color = pColors.GREEN
    return color

# initialization value
def REQ_MARINE_TROPHIES(master, task, game_state):
    WINNER_EYES_CLOLORS = [pColors.BLUE] * 5
    if task.stack == []:

        knife_slots = [1] * len(DEVICES_TABLE.BTN_KNIFE_SLOTS)

        # init eyes
        fishes_eyes = [pColors.RED] * 5

        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        for index in range(len(knife_slots)):
            smart_leds.setOneLed(DEVICES_TABLE.SML_FISH_EYES[index], fishes_eyes[index])

        task.stack.append(knife_slots)
        task.stack.append(fishes_eyes)


    fishes_eyes = task.stack.pop()
    old_knife_slots = task.stack.pop()

    # get knife slots status
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    knife_slots = []
    for slot_index in range(len(DEVICES_TABLE.BTN_KNIFE_SLOTS)):
        knife_slots.append(
                buttons[ DEVICES_TABLE.BTN_KNIFE_SLOTS[slot_index] ])

    if knife_slots != old_knife_slots:
        for index in range(len(knife_slots)):
            if (knife_slots[index] != old_knife_slots[index]) and (knife_slots[index] == 0):
                fishes_eyes[index] = toggleEyeColor(fishes_eyes[index])
                if index == 0:
                    fishes_eyes[index + 1] = toggleEyeColor(fishes_eyes[index + 1])
                elif index == len(fishes_eyes) - 1:
                    fishes_eyes[index - 1] = toggleEyeColor(fishes_eyes[index - 1])
                else:
                    fishes_eyes[index - 1] = toggleEyeColor(fishes_eyes[index - 1])
                    fishes_eyes[index + 1] = toggleEyeColor(fishes_eyes[index + 1])

        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        for index in range(len(knife_slots)):
            smart_leds.setOneLed(DEVICES_TABLE.SML_FISH_EYES[index], fishes_eyes[index])

    if knife_slots != old_knife_slots:
        print("(REQ:{task_id}) Knife slots changed: {slots}".format(task_id=task.id, slots=knife_slots))
        print("(REQ:{task_id}) Knife slots changed: colors {eyes}".format(task_id=task.id, eyes=fishes_eyes))
        old_knife_slots = knife_slots

    if WINNER_EYES_CLOLORS == fishes_eyes:
        print("(REQ:{task_id}) Fishes eyes done!!!!: {slots}".format(task_id=task.id, slots=knife_slots))
        return True


    task.stack.append(old_knife_slots)
    task.stack.append(fishes_eyes)

def AC_OPEN_CLOSET_DOOR(master, task, game_state):
    print("(ACTION:{task_id}) Open closet".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)


def AC_OPEN_DOOR_WITH_SKELET(master, task, game_state):
    print("(ACTION:{task_id}) Open door with skelet".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_WITH_SKELET] = DEVICES_TABLE.CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)


def AC_ADD_PUT_FOURTH_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_FOURTH_COIN)

def REQ_PUT_FOURTH_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 4)

def AC_PERFORMANCE_CULMINATION(master, task, game_state):
    print("(ACTION:{task_id}) Performance culmination".format(task_id=task.id))

def AC_ADD_THE_FINAL(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.THE_FINAL)

def REQ_THE_FINAL(master, task, game_state):
    pass

def AC_THE_FINAL(master, task, game_state):
    print("(ACTION:{task_id}) The final".format(task_id=task.id))

def AC_OPEN_PICTURE_BOX(master, task, game_state):
    print("(ACTION:{task_id}) Open picture box".format(task_id=task.id))

    sl_control = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_control[DEVICES_TABLE.SL_BOX_UNDER_PICTURE] = DEVICES_TABLE.OPEN
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_control)

