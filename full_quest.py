#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import random
from settings import Devices, DEVICES_TABLE, TASKS_IDS
from settings import SOUNDS_NAMES
from settings import SOUNDS
from settings import COLORS


class GLOBAL_VARIABLES:
    TABLE_CLOCK_VALUE = 1
    TABLE_CLOCK_LAST_CHANGE_TIME = time.time()

    CLOCKS_SYNCHRONIZE = False

    WALL_CLOCK_REAL_12 = 0
    CURRENT_MOVE_PICTURE = None

    SOUND_ARRAY = [];


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
                buttons[DEVICES_TABLE.BTN_KNIFE_SLOTS[slot_index]])
    puzzle_status("KNIFE_SLOTS: {}".format(knife_slots), knife_slots == [1]*5)

    # # check monets
    # adc_list = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()
    # adc_coins_values = (adc_list[DEVICES_TABLE.COIN_1],
    #         adc_list[DEVICES_TABLE.COIN_2],
    #         adc_list[DEVICES_TABLE.COIN_3],
    #         adc_list[DEVICES_TABLE.COIN_4])
    #
    # inserted_coins_number = 0
    # for index, coin_value in enumerate(adc_coins_values):
    #         print("REQ: check_coins_inserted |"
    #               " coin_id {} value: {}".format(index, coin_value))
    #     if coin_value >= DEVICES_TABLE.COIN_INSERTED_RANGE[0] and
    #             coin_value <= DEVICES_TABLE.COIN_INSERTED_RANGE[1]:
    #         inserted_coins_number = inserted_coins_number + 1
    #     elif DEVICES_TABLE.COIN_NONE_RANGE[0] <= coin_value <= DEVICES_TABLE.COIN_NONE_RANGE[1]:
    #         # all ok, just monet not inserted
    #         pass
    #     else:
    #         pass
    #


def init_sounds(game_state):
    sound_manager = game_state.sound_manager
    SOUNDS.stage_1 = sound_manager.add_sound(SOUNDS_NAMES.STAGE_1)
    SOUNDS.lifesaver_begin = sound_manager.add_sound(SOUNDS_NAMES.LIFESAVER_2_1)
    SOUNDS.lifesaver_end = sound_manager.add_sound(SOUNDS_NAMES.LIFESAVER_3_1)
    SOUNDS.lightning = sound_manager.add_sound(SOUNDS_NAMES.LIGHTNING)
    SOUNDS.girl_help = sound_manager.add_sound(SOUNDS_NAMES.GIRL_1_HELP)
    SOUNDS.girl_heard = sound_manager.add_sound(SOUNDS_NAMES.GIRL_2_HEARD)
    SOUNDS.girl_she_all_i_have = sound_manager.add_sound(
        SOUNDS_NAMES.GIRL_4_SHE_ALL_I_HAVE)
    SOUNDS.bad_end = sound_manager.add_sound(SOUNDS_NAMES.BAD_END)
    SOUNDS.old_man = sound_manager.add_sound(SOUNDS_NAMES.OLD_MAN)
    SOUNDS.dagon_private = sound_manager.add_sound(SOUNDS_NAMES.DAGON_PRIVATE)

    SOUNDS.stage_2 = sound_manager.add_sound(SOUNDS_NAMES.STAGE_2)
    SOUNDS.stage_3 = sound_manager.add_sound(SOUNDS_NAMES.STAGE_3)
    SOUNDS.stage_4 = sound_manager.add_sound(SOUNDS_NAMES.STAGE_4)

    SOUNDS.stages.append(SOUNDS.stage_1)
    SOUNDS.stages.append(SOUNDS.stage_2)
    SOUNDS.stages.append(SOUNDS.stage_3)
    SOUNDS.stages.append(SOUNDS.stage_4)


    SOUNDS.prey = sound_manager.add_sound(SOUNDS_NAMES.PREY)
    SOUNDS.names = sound_manager.add_sound(SOUNDS_NAMES.NAMES)
    SOUNDS.picture = sound_manager.add_sound(SOUNDS_NAMES.PICTURE)
    SOUNDS.not_understand = sound_manager.add_sound(SOUNDS_NAMES.NOT_UNDERSTAND)
    SOUNDS.division = sound_manager.add_sound(SOUNDS_NAMES.DIVISION)
    SOUNDS.chest = sound_manager.add_sound(SOUNDS_NAMES.CHEST)
    SOUNDS.closet = sound_manager.add_sound(SOUNDS_NAMES.CLOSET)
    SOUNDS.he = sound_manager.add_sound(SOUNDS_NAMES.HE)
    SOUNDS.doll = sound_manager.add_sound(SOUNDS_NAMES.DOLL)

    # new, not added yet
    SOUNDS.begin = sound_manager.add_sound(SOUNDS_NAMES.BEGIN)
    SOUNDS.music_on_demon_wings = sound_manager.add_sound(SOUNDS_NAMES.MUSIC_ON_DEMON_WINGS)
    SOUNDS.first_coin = sound_manager.add_sound(SOUNDS_NAMES.FIRST_COIN)
    SOUNDS.begin_min_later = sound_manager.add_sound(SOUNDS_NAMES.BEGIN_MIN_LATER)
    SOUNDS.before_books_fall = sound_manager.add_sound(SOUNDS_NAMES.BEFORE_BOOKS_FALL)
    SOUNDS.after_books_fall = sound_manager.add_sound(SOUNDS_NAMES.AFTER_BOOKS_FALL)
    SOUNDS.fishing = sound_manager.add_sound(SOUNDS_NAMES.FISHING)
    SOUNDS.clock_sync = sound_manager.add_sound(SOUNDS_NAMES.CLOCK_SYNC)
    SOUNDS.second_coin = sound_manager.add_sound(SOUNDS_NAMES.SECOND_COIN)
    SOUNDS.knife_achieved = sound_manager.add_sound(SOUNDS_NAMES.KNIFE_ACHIEVED)
    SOUNDS.all_coins_on_place = sound_manager.add_sound(SOUNDS_NAMES.ALL_COINS_ON_PLACE)
    SOUNDS.after_skelet_door_open = sound_manager.add_sound(SOUNDS_NAMES.AFTER_SKELET_DOOR_OPEN)
    SOUNDS.cthulhu_appear = sound_manager.add_sound(SOUNDS_NAMES.CTHULHU_APPEAR)
    SOUNDS.operator_end = sound_manager.add_sound(SOUNDS_NAMES.OPERATOR_END)

    SOUNDS.lifesaver_end_first = sound_manager.add_sound(SOUNDS_NAMES.LIFESAVER_3_1_FIRST)
    SOUNDS.lifesaver_end_second = sound_manager.add_sound(SOUNDS_NAMES.LIFESAVER_3_1_SECOND)

    SOUNDS.girl_please_stop = sound_manager.add_sound(SOUNDS_NAMES.GIRL_PLEASE_STOP)
    SOUNDS.girl_who_are_you = sound_manager.add_sound(SOUNDS_NAMES.GIRL_WHO_ARE_YOU)
    SOUNDS.girl_hear_me = sound_manager.add_sound(SOUNDS_NAMES.GIRL_HEAR_ME)

def REQ_QUEST_INIT(master, task, game_state):
    init_sounds(game_state)
    # return True
    # close all boxes
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[
        DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_COIN] = DEVICES_TABLE.CLOSE
    sl_controlls[
        DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_PICTURE] = DEVICES_TABLE.CLOSE
    sl_controlls[DEVICES_TABLE.SL_CODE_LOCKS_LOCKER_LOCK] = DEVICES_TABLE.CLOSE
    sl_controlls[
        DEVICES_TABLE.SL_BOX_IN_CLOSET_WITH_KNIFE] = DEVICES_TABLE.CLOSE
    sl_controlls[DEVICES_TABLE.SL_BOX_UNDER_PICTURE] = DEVICES_TABLE.CLOSE
    sl_controlls[DEVICES_TABLE.SL_MIRROR_IN_CLOSET] = 0
    sl_controlls[DEVICES_TABLE.SL_FISHING_RODS_HOLDERS] = 0

    for scare_index in DEVICES_TABLE.SL_SCARE_IN_LOCKER:
        sl_controlls[scare_index] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    # init colors
    # init fish eyes
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    for eye_index in DEVICES_TABLE.SML_FISH_EYES:
        smart_leds.setOneLed(eye_index, COLORS.RED)

    # init lights in rooms
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    init_color = COLORS.ROOM_BLUE
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, init_color)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, init_color)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, init_color)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, init_color)

    # on lenin lamps
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 1
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    # lightning off
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        smart_leds.setOneLed(light_index, [0, 0, 0])

    # init head in window
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_MOTOR] = 1
    sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_ACTION] = DEVICES_TABLE.HEAD_ACTION_HIDE
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    time.sleep(1)
    sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_MOTOR] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    # init doors
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.OPEN
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_WITH_SKELET] = DEVICES_TABLE.CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

    # init picture on the wall
    CHANGE_MOVE_PICTURE(master, 0)

    # init GODS table
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = DEVICES_TABLE.OPEN
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)
    time.sleep(10)
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = DEVICES_TABLE.CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)
    time.sleep(2)

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

    if GLOBAL_VARIABLES.TABLE_CLOCK_VALUE >= 12:
        GLOBAL_VARIABLES.TABLE_CLOCK_VALUE = GLOBAL_VARIABLES.TABLE_CLOCK_VALUE - 12

    print("TABLE CLOCK VALUE: {}".format(GLOBAL_VARIABLES.TABLE_CLOCK_VALUE))

    # sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    # sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 1
    #
    # master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    # time.sleep(1)
    #
    # sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 0
    # master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ADD_TABLE_CLOCK_RING_OUT(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.TABLE_CLOCK_RING_OUT_ALWAYS)


def REQ_TABLE_CLOCK_RING_OUT_ALWAYS(master, task, game_state):
    REPEAT_RING_OUT = 8 # sec
    UNSET_RING_OUT = 1
    if task.stack == []:
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    time_passed = time.time() - start_time

    if time_passed < REPEAT_RING_OUT:
        pass

    elif REPEAT_RING_OUT < time_passed < REPEAT_RING_OUT + UNSET_RING_OUT:
        # ring out table clock
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    else:
        # unset ring out command
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 0
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
        start_time = time.time()

    if GLOBAL_VARIABLES.CLOCKS_SYNCHRONIZE:
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 0
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
        return True

    task.stack.append(start_time)
    return


def AC_TABLE_CLOCK_RING_OUT(master, task, game_state):
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    time.sleep(0.4)

    sl_controlls[DEVICES_TABLE.SL_TABLE_CLOCK_RING_OUT] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ADD_BACKGROUND_TABLE_CLOCK_JOB(master, task, game_state):
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
    INITIALIZATION_SET_12_TIME = 5

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
    print("WALL_CLOCK_INIT_12_VALUE: {}".format(
              GLOBAL_VARIABLES.WALL_CLOCK_REAL_12))

    return True


def AC_CHANGE_MOVE_PICTURE(master, task, game_state):
    CHANGE_MOVE_PICTURE(master)


def CHANGE_MOVE_PICTURE(master, picture_index=None):
    if GLOBAL_VARIABLES.CURRENT_MOVE_PICTURE is None:
        picture_index = 0
    elif picture_index is None:
        picture_index = GLOBAL_VARIABLES.CURRENT_MOVE_PICTURE + 1

    if picture_index >= len(DEVICES_TABLE.SL_MOVING_PICTURE):
        picture_index = 0

    print("Change picture move, index: {}".format(picture_index))
    GLOBAL_VARIABLES.CURRENT_MOVE_PICTURE = picture_index

    sl_control = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    for picture_value in DEVICES_TABLE.SL_MOVING_PICTURE:
        sl_control[picture_value] = 0
    sl_control[DEVICES_TABLE.SL_MOVING_PICTURE[picture_index]] = 1
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_control)

    # # off eddison lamp
    # sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    # sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 0
    # master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    # time.sleep(2)
    # sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    # sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 1
    # master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ADD_WAIT_START_QUEST(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.START_QUEST)


def REQ_START_QUEST(master, task, game_state):
    pass
    # return True

def AC_ADD_PLAY_INTRO(master, task, game_state):

    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_BEGIN)

def REQ_PLAY_INTRO(master, task, game_state):
    DELAY_TIME = 10
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.begin)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.begin)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)

def AC_ADD_PLAY_BEGINNING_AFTER_MINUTE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_BEGINNING_AFTER_MINUTE)

def REQ_PLAY_BEGINNING_AFTER_MINUTE(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()

    spend_time = time.time() - start_time
    if spend_time >  DEVICES_TABLE.TIMER_PLAY_BEGGINING_AFTER_MINUTE:
        game_state.sound_manager.play_sound(SOUNDS.begin_min_later)
        return True

    task.stack.append(start_time)
    return

def AC_OFF_EDDISON_LIGHT(master, task, game_state):
    # off lenin lamps
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ON_EDDISON_LIGHT(master, task, game_state):
    # on eddison
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 1
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_SOUND_BACKGROUND_STAGE_1(master, task, game_state):
    game_state.sound_manager.play_sound(SOUNDS.stage_1)


def AC_LIGHTNING(master, task, game_state):

    print("SML_ALL_LIGHTS in AC_LIGHTNING {}".format(
              DEVICES_TABLE.SML_ALL_LIGHTS))

    # SOUNDS.lightning.play()
    sml_control = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    last_lightning_value = []

    # SAVE COLORS
    # save all room colors
    all_smart_lights = []
    for light_index in DEVICES_TABLE.SML_ALL_LIGHTS:
        all_smart_lights.append(sml_control.getRgbLed(light_index))
        sml_control.setOneLed(light_index, COLORS.NONE)

    # set FISH eyes colors
    # for lig
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    for eye_index in DEVICES_TABLE.SML_FISH_EYES:
        smart_leds.setOneLed(eye_index, COLORS.FISH_LIGHTNING)

    # save lenin light color
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    lenin_ligth_value = sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT]
    # lenin off
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    # save lightning colors
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        last_lightning_value.append(sml_control.getRgbLed(light_index))

    # lightning off
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        sml_control.setOneLed(light_index, [0, 0, 0])

    time.sleep(0.2)

    # start play sound
    game_state.sound_manager.play_sound(SOUNDS.lightning)

    # lightning on
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        sml_control.setOneLed(light_index, [0xfff, 0xfff, 0xfff])

    print("Lightning!")
    time.sleep(0.4)

    # restore lightning colors
    for index_number, light_index in enumerate(DEVICES_TABLE.SML_LIGHTNING):
        print("last_lightning_value: {}".format(
            last_lightning_value[index_number]))
        sml_control.setOneLed(light_index, last_lightning_value[index_number])

    time.sleep(1)

    # RESTORE
    # restore room lights
    for index_number, light_index in enumerate(DEVICES_TABLE.SML_ALL_LIGHTS):
        print("last_romm_light_value: {}".format(
                  all_smart_lights[index_number]))
        sml_control.setOneLed(light_index, all_smart_lights[index_number])

    # restore lenin light value
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = lenin_ligth_value
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    time.sleep(1)
    print("Lightning off!")


def AC_SCARE_LIGHTNING(master, task, game_state):
    # For scare face only

    print("SML_ALL_LIGHTS in AC_LIGHTNING {}".format(
              DEVICES_TABLE.SML_SCARE_ALL_LIGHT))

    # SOUNDS.lightning.play()
    sml_control = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    last_lightning_value = []

    # SAVE COLORS
    # save all room colors
    all_smart_lights = []
    for light_index in DEVICES_TABLE.SML_SCARE_ALL_LIGHT:
        all_smart_lights.append(sml_control.getRgbLed(light_index))
        sml_control.setOneLed(light_index, COLORS.NONE)

    # set FISH eyes colors
    # for lig
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    for eye_index in DEVICES_TABLE.SML_FISH_EYES:
        smart_leds.setOneLed(eye_index, COLORS.FISH_LIGHTNING)

    # save lenin light color
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    lenin_ligth_value = sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT]
    # lenin off
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    # save lightning colors
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        last_lightning_value.append(sml_control.getRgbLed(light_index))

    # lightning off
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        sml_control.setOneLed(light_index, [0, 0, 0])

    time.sleep(0.2)

    # start play sound
    game_state.sound_manager.play_sound(SOUNDS.lightning)

    # lightning on
    for light_index in DEVICES_TABLE.SML_LIGHTNING:
        sml_control.setOneLed(light_index, [0xfff, 0xfff, 0xfff])

    print("Lightning!")
    time.sleep(0.4)

    # restore lightning colors
    for index_number, light_index in enumerate(DEVICES_TABLE.SML_LIGHTNING):
        print("last_lightning_value: {}".format(
            last_lightning_value[index_number]))
        sml_control.setOneLed(light_index, last_lightning_value[index_number])

    time.sleep(1)

    # RESTORE
    # restore room lights
    for index_number, light_index in enumerate(DEVICES_TABLE.SML_SCARE_ALL_LIGHT):
        print("last_romm_light_value: {}".format(
                  all_smart_lights[index_number]))
        sml_control.setOneLed(light_index, all_smart_lights[index_number])

    # restore lenin light value
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = lenin_ligth_value
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    time.sleep(1)
    print("Lightning off!")


def AC_ADD_PLAY_SOUND_HELP(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_HELP)


def REQ_PLAY_SOUND_HELP(master, task, game_state):
    TIME_TO_WAIT = 5 * 60
    if task.stack == []:
        task.stack.append(time.time())
    start_time = task.stack.pop()

    if time.time() - start_time > TIME_TO_WAIT:
        return True

    task.stack.append(start_time)


def AC_PLAY_SOUND_HELP(master, task, game_state):
    game_state.sound_manager.play_sound(SOUNDS.girl_help)


def AC_LIGHT_SHOW_WHERE_STATUE(master, task, game_state):
    print("(ACTION:{task_id}) show light where statue".format(task_id=task.id))
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, COLORS.ROOM_GREEN)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, COLORS.ROOM_GREEN)


def AC_ADD_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_STATUE_ON_LORDS_TABLE)


def REQ_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    PUT_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_RANGE
    NONE_RANGE = DEVICES_TABLE.LORDS_TABLE_STATUE_NONE_RANGE

    if task.stack == []:
        old_value = 0
        task.stack.append(old_value)

    old_value = task.stack.pop()
    lords_table_value = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()[
                                      DEVICES_TABLE.ADC_LORDS_TABLE_STATUE]
    if PUT_RANGE[0] <= lords_table_value <= PUT_RANGE[1]:
        print(
            "YES: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(
                lords_table_value))
        return True
    elif NONE_RANGE[0] <= lords_table_value <= NONE_RANGE[1]:
        if old_value != lords_table_value:
            # it's ok. statue just absent
            print(
                "NONE: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(
                    lords_table_value))
            old_value = lords_table_value
    else:
        # error - puzzle is broken
        if not master.debugMode():
            if old_value != lords_table_value:
                print(
                    "ERROR: REQ_PUT_STATUE_ON_LORDS_TABLE value: {}".format(
                        lords_table_value))
                old_value = lords_table_value

    task.stack.append(old_value)
    return False


def AC_TURN_LORDS_TABLE(master, task, game_state):
    print("(ACTION:{task_id})We turn lords table".format(task_id=task.id))
    time.sleep(2)
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_GODS_TABLE_MOTOR] = DEVICES_TABLE.OPEN
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)


def AC_PLAY_COINS_PULLED_US(master, task, game_state):
    print("(ACTION:{task_id}) Coins pulled us".format(task_id=task.id))
    # game_state.sound_manager.play_sound(SOUNDS.first_coin)

    GLOBAL_VARIABLES.SOUND_ARRAY.append({
          'sound': SOUNDS.first_coin,
          'delay': 0,
          'delay_start': False,
          'play_start': False,
          'play_done': False
    })


def AC_ADD_PUT_FIRST_COIN(master, task, game_state):
    time.sleep(4)
    game_state.add_active_task_with_id(TASKS_IDS.PUT_FIRST_COIN)


def check_coins_inserted(master, task, game_state, nubmer_of_coins):
    adc_list = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()

    adc_coins_values = (adc_list[DEVICES_TABLE.COIN_1],
                        adc_list[DEVICES_TABLE.COIN_2],
                        adc_list[DEVICES_TABLE.COIN_3],
                        adc_list[DEVICES_TABLE.COIN_4])

    inserted_coins_number = 0
    for index, coin_value in enumerate(adc_coins_values):
        print(
            "REQ: check_coins_inserted coin_id {} value: {}".format(
                index, coin_value))
        if DEVICES_TABLE.COIN_INSERTED_RANGE[
                0] <= coin_value <= DEVICES_TABLE.COIN_INSERTED_RANGE[1]:
            inserted_coins_number = inserted_coins_number + 1
        elif DEVICES_TABLE.COIN_NONE_RANGE[0] <= coin_value <= DEVICES_TABLE.COIN_NONE_RANGE[1]:
            # all ok, just monet not inserted
            pass
        else:
            if not master.debugMode():
                print(
                    "ERROR: check_coins_inserted coin_id {} value: {}".format(
                        index, coin_value))
    if inserted_coins_number >= nubmer_of_coins:
        return True
    return False


def REQ_PUT_FIRST_COIN(master, task, game_state):
    # time.sleep(5)
    # return check_coins_inserted(master, task, game_state, 1)
    return False


def AC_BAKE_FLARE_UP(master, task, game_state):
    print("(ACTION:{task_id}) Bake flare up".format(task_id=task.id))
    pass


def AC_PLAY_PICTURE(master, task, game_state):
    # game_state.sound_manager.play_sound(SOUNDS.picture)
    GLOBAL_VARIABLES.SOUND_ARRAY.append({
          'sound': SOUNDS.picture,
          'delay': 0,
          'delay_start': False,
          'play_start': False,
          'play_done': False
    })


def AC_ADD_PLAY_BEFORE_FALLING_BOOKS(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_BEFORE_FALLING_BOOKS)
    time.sleep(1) # becouse picture and falling books plays same time


def REQ_PLAY_BEFORE_FALLING_BOOKS(master, task, game_state):
    WAIT_TILL_PLAY = 3
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())


    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if game_state.sound_manager.is_playing(SOUNDS.picture):
        task.stack.append(sound_start)
        task.stack.append(time.time())
        return

    elif spend_time < WAIT_TILL_PLAY:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return

    elif not sound_start:
        buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
        dad_collected = buttons[DEVICES_TABLE.BTN_COLLECT_DAD_FISHING]
        if dad_collected: return True

        GLOBAL_VARIABLES.SOUND_ARRAY.append({
              'sound': SOUNDS.before_books_fall,
              'delay': 0,
              'delay_start': False,
              'play_start': False,
              'play_done': False
        })
        # return True
        # game_state.sound_manager.play_sound(SOUNDS.before_books_fall)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return

    else:
        playing = True
        sound_array = GLOBAL_VARIABLES.SOUND_ARRAY
        for sound_object in sound_array:
            if sound_object['sound'] == SOUNDS.before_books_fall:
                playing = not sound_object['play_done']

        if not playing:
            return True
        print("Sound before books still playing")

        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


def AC_ADD_FALLING_BOOK_RODS_TIMER(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.FALLING_BOOK_RODS_TIMER)


def REQ_FALLING_BOOK_RODS_TIMER(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()
    passed_time = time.time() - start_time

    if passed_time <= DEVICES_TABLE.FALLING_BOOK_RODS_TIMER:
        task.stack.append(start_time)
        return

    return True


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

    time.sleep(2)
    sl_controlls[DEVICES_TABLE.SL_FISHING_RODS_HOLDERS] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_LIGHT_SHOW_WHERE_COLLECT_DAD_FISHING(master, task, game_state):
    print("(ACTION:{task_id}) Light show where collect dad fishing".format(task_id=task.id))
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, COLORS.ROOM_GREEN)


def AC_PLAY_SHE_ALL_I_HAVE(master, task, game_state):
    time.sleep(8)
    game_state.sound_manager.play_sound(SOUNDS.girl_she_all_i_have)


def AC_ADD_COLLECT_DAD_FISHING(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.COLLECT_DAD_FISHING)


def REQ_COLLECT_DAD_FISHING(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    dad_collected = buttons[DEVICES_TABLE.BTN_COLLECT_DAD_FISHING]

    return dad_collected


def AC_ADD_PLAY_FISHING(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_FISHING)

def REQ_PLAY_SOUND_FISHING(master, task, game_state):
    if task.stack == []:
        task.stack.append(True)
        # game_state.sound_manager.play_sound(SOUNDS.fishing)
        GLOBAL_VARIABLES.SOUND_ARRAY.append({
              'sound': SOUNDS.fishing,
              'delay': 0,
              'delay_start': False,
              'play_start': False,
              'play_done': False
        })

    # playing = game_state.sound_manager.is_playing(SOUNDS.fishing)
    playing = True
    sound_array = GLOBAL_VARIABLES.SOUND_ARRAY
    for sound_object in sound_array:
        if sound_object['sound'] == SOUNDS.fishing:
            playing = not sound_object['play_done']

    if not playing:
        return True


def AC_TABLE_CLOCK_CHANGE_TIME(master, task, game_state):
    print("(ACTION:{task_id}) Table clock change time".format(task_id=task.id))
    # Time must set to random value
    TABLE_CLOCK_UP(master)


def AC_ADD_CLOCK_SYNCHRONIZATION(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CLOCK_SYNCHRONIZATION)

def eddison_lamp_blink(master, task, SLEEP_STATE_TIME):
    if task.stack == []:
        light_turn = False
        task.stack.append(light_turn)
        task.stack.append(time.time())
        state_id = 0
        task.stack.append(state_id)

    state_id = task.stack.pop()
    start_time = task.stack.pop()
    light_turn = task.stack.pop()

    if state_id >= len(SLEEP_STATE_TIME):
        return True

    # set lamp state
    if not light_turn:
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        if SLEEP_STATE_TIME[state_id]["state"] == "on":
            sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 1
        else:
            sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 0
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

        light_turn = True

    spend_time = time.time() - start_time
    if spend_time > SLEEP_STATE_TIME[state_id]["time"]:
        state_id = state_id + 1
        start_time = time.time()
        light_turn = False

    task.stack.append(light_turn)
    task.stack.append(start_time)
    task.stack.append(state_id)
    return

def AC_ADD_EDDISON_LAMP_BLINK(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.EDDISON_LAMP_BLINK)

def REQ_EDDISON_LAMP_BLINK(master, task, game_state):
    SLEEP_STATE_TIME = [
        {"state": "off", "time": 5},
        {"state": "on", "time": 1},
    ]

    return eddison_lamp_blink(master, task, SLEEP_STATE_TIME)


def AC_LIGHT_SHOW_WHERE_CLOCK_SYNCHRONIZATION(master, task, game_state):
    print("(ACTION:{task_id}) Light show where clock synchronization".format(task_id=task.id))
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)

    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, COLORS.ROOM_BLUE)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.ROOM_GREEN)

def AC_ALL_LIGHT_ON(master, task, game_state):
    # init lights in rooms
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    init_color = COLORS.ROOM_BLUE
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, init_color)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, init_color)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, init_color)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, init_color)

    # off lenin lamps
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 1
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ALL_LIGHT_OFF(master, task, game_state):
    # init lights in rooms
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    # init_color = COLORS.ROOM_BLUE

    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, COLORS.OFF)
    smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, COLORS.OFF)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.OFF)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, COLORS.OFF)

    # off lenin lamps
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_EDDISON_LIGHT] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def REQ_CLOCK_SYNCHRONIZATION(master, task, game_state):
    MAX_VALUE = 32767
    OVERFLOW_DELTA = 20
    if task.stack == []:
        overflow = 0

        last_value = [GLOBAL_VARIABLES.WALL_CLOCK_REAL_12]

        task.stack.append(overflow)
        task.stack.append(last_value)
        task.stack.append(time.time())

    last_time = task.stack.pop()
    time_passed = time.time() - last_time
    if time_passed < 0.1:
        task.stack.append(last_time)
        return

    wall_clock_values_list = task.stack.pop()
    last_value = wall_clock_values_list[-1]

    encoders = master.getEncoders(Devices.LOVECRAFT_DEVICE_NAME).get()
    current_value = encoders[DEVICES_TABLE.WALL_CLOCK]

    if current_value == last_value:
        task.stack.append(wall_clock_values_list)
        task.stack.append(time.time())
        return

    overflow = task.stack.pop()

    if last_value < OVERFLOW_DELTA and current_value > (MAX_VALUE - OVERFLOW_DELTA):
        overflow = overflow - 1
    elif last_value > (MAX_VALUE - OVERFLOW_DELTA) and current_value < OVERFLOW_DELTA:
        overflow = overflow + 1

    real_cur_value = current_value + (MAX_VALUE) * overflow

    INIT_VALUE = GLOBAL_VARIABLES.WALL_CLOCK_REAL_12

    if overflow >= 0:
        delta = abs(INIT_VALUE - real_cur_value)
    else:
        real_cur_value = abs(INIT_VALUE + abs(MAX_VALUE * overflow) - abs(current_value))
        delta = - real_cur_value
    # print("Overflow_value: {}, real_cur_value {}, delta {}".format(overflow, real_cur_value, delta))

    if INIT_VALUE <= real_cur_value:
        cur_time = 0 + delta/2  - int(delta/24) * 12
    else:
        cur_time = 12 - (delta/2 - int(delta/24) * 12)

    if cur_time == 12:
        cur_time = 0

    wall_clock_last_value = last_value
    wall_clock_time = cur_time
    wall_clock_value = current_value

    print("Wall clock TIME: {}".format(wall_clock_time))

    wall_clock_values_list.append(current_value)

    print("REQ_CLOCK_SYNCHRONIZATION: wall late value: {}, new_value: {}  init_real {}".format(
        wall_clock_last_value, wall_clock_value, GLOBAL_VARIABLES.WALL_CLOCK_REAL_12))
    print("REQ_CLOCK_SYNCHRONIZATION: wall list {}".format(wall_clock_values_list))
    print("REQ_CLOCK_SYNCHRONIZATION: table time: {}, wall time: {}".format(
              GLOBAL_VARIABLES.TABLE_CLOCK_VALUE, wall_clock_time))

    if GLOBAL_VARIABLES.TABLE_CLOCK_VALUE == wall_clock_time:
        print("(REQ:{task_id}) Clocks sync!".format(task_id=task.id))
        GLOBAL_VARIABLES.CLOCKS_SYNCHRONIZE = True
        return True

    task.stack.append(overflow)
    task.stack.append(wall_clock_values_list)
    # save time
    current_time = time.time()
    task.stack.append(current_time)

    return False

def AC_SET_CLOCK_SYNCHRONIZATION_TRUE(master, task, game_state):
    GLOBAL_VARIABLES.CLOCKS_SYNCHRONIZE = True


def AC_PLAY_CLOCK_OPEN(master, task, game_state):
    game_state.sound_manager.play_sound(SOUNDS.clock_sync)


def AC_BOX_UNDER_CLOCK_FACE_OPEN(master, task, game_state):
    print(
        "(ACTION:{task_id}) Lock under clock face opened".format(
            task_id=task.id))
    # What box is opened ? On Device table looks like it not my job
    time.sleep(2)
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_PICTURE] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def ADD_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.FAMILY_PICTURE_BARLEY_BREAK)


def REQ_FAMILY_PICTURE_BARLEY_BREAK(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    puzzle_collected = buttons[DEVICES_TABLE.BTN_PICTURE_BARLEY_BREAK]

    return puzzle_collected


def AC_PLAY_SOUND_GIRL_HEARD(master, task, game_state):
    time.sleep(2)
    game_state.sound_manager.play_sound(SOUNDS.girl_heard)


def AC_SECOND_COIN_FALL(master, task, game_state):
    print(
        "(ACTION:{task_id}) Second coin fall from clock".format(
            task_id=task.id))
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_WALL_CLOCK_LOCK_WITH_COIN] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def ADD_PUT_SECOND_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_SECOND_COIN)


def REQ_PUT_SECOND_COIN(master, task, game_state):
    # return check_coins_inserted(master, task, game_state, 2)
    return False

def AC_ADD_PLAY_ABOUT_COINS_AND_CLOSET(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_ABOUT_COINS_AND_CLOSET)

def REQ_PLAY_ABOUT_COINS_AND_CLOSET(master, task, game_state):
    DELAY_TIME = 0
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.second_coin)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.second_coin)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_ADD_PLAY_SHE_ALL_WHAT_I_HAVE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SHE_ALL_WHAT_I_HAVE)


def REQ_PLAY_SHE_ALL_WHAT_I_HAVE(master, task, game_state):
    DELAY_TIME = 2
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.girl_she_all_i_have)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.girl_she_all_i_have)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


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

    time.sleep(4)

    for scare_index in DEVICES_TABLE.SL_SCARE_IN_LOCKER:
        sl_controlls[scare_index] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_SOUND_BACKGROUND_STAGE_2(master, task, game_state):
    game_state.sound_manager.stop(SOUNDS.stage_1)
    game_state.sound_manager.play_sound(SOUNDS.stage_2)



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
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP] = 1

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    time.sleep(5)
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP] = 0

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    # maybe here play sound or in external action

def AC_ADD_PLAY_CLOSET(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_CLOSET)


def REQ_PLAY_CLOSET(master, task, game_state):
    DELAY_TIME = 5
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.closet)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.closet)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_ADD_PLAY_PRAY(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_PRAY)


def REQ_PLAY_PRAY(master, task, game_state):
    DELAY_TIME = 5
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.prey)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.prey)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_ADD_PLAY_GIRL_YOU_HEAR_ME(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_GIRL_YOU_HEAR_ME)


def REQ_PLAY_GIRL_YOU_HEAR_ME(master, task, game_state):
    DELAY_TIME = 20
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.girl_hear_me)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.girl_hear_me)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)

def REQ_PLACE_THE_BOTTLES(master, task, game_state):
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()

    bottles_placed = buttons[DEVICES_TABLE.BTN_BOTTLES]

    return bottles_placed


def AC_ADD_PUMPS_WATER(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.AQUARIUM_PUMP)


def REQ_AQUARIUM_PUMPS_WATER_TIMER(master, task, game_state):
    # find time experimental
    TIME_TO_WORK = DEVICES_TABLE.AQUARIUM_PUMP_TIME

    if task.stack == []:
        print("(REQ:{task_id}) Start aquarium pump".format(task_id=task.id))
        start_time = time.time()
        task.stack.append(start_time)
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_AQUARIUM_PUMP] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    start_time = task.stack.pop()

    passed_time = time.time() - start_time

    if passed_time < TIME_TO_WORK:
        task.stack.append(start_time)
        return

    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_AQUARIUM_PUMP] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    return True


def AC_STOP_AQUARIUM_PUMP(master, task, game_state):
    print("(ACTION:{task_id}) Stop aquarium pump".format(task_id=task.id))

    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_AQUARIUM_PUMP] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ADD_FILL_QUARIUM(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.AQUARIUM_FILL)


def REQ_FILL_AQUARIUM(master, task, game_state):
    # find time experimental
    TIME_TO_WORK = DEVICES_TABLE.AQUARIUM_FILL_TIME

    if task.stack == []:
        print("(REQ:{task_id}) Start fill aquarium".format(task_id=task.id))
        start_time = time.time()
        task.stack.append(start_time)
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP] = 1
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

    start_time = task.stack.pop()

    passed_time = time.time() - start_time

    if passed_time < TIME_TO_WORK:
        task.stack.append(start_time)
        return

    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    return True


def AC_STOP_AQUARIUM_FILL(master, task, game_state):
    print("(ACTION:{task_id}) Stop aquarium fill".format(task_id=task.id))

    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_DOLL_EYES_PUMP] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ADD_PUT_THIRD_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_THIRD_COIN)


def REQ_PUT_THIRD_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 3)


def AC_SOUND_BACKGROUND_STAGE_3(master, task, game_state):
    game_state.sound_manager.stop(SOUNDS.stage_2)
    game_state.sound_manager.play_sound(SOUNDS.stage_3)

def AC_CLOSE_THE_STOOREROOM_DOOR(master, task, game_state):
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.RELAY_CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

def AC_ADD_CLOSE_THE_DOOR(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.CLOSE_THE_DOOR)


def REQ_CLOSE_THE_DOOR(master, task, game_state):
    TIME_TO_CLOSE = 8
    TIME_TO_OPEN = 7
    TIME_TO_WAIT_PLAYERS_ACTIONS = 15
    TIME_BEFORE_CLOSE_AGAIN = 3
    NUMBER_DELTA = 20

    class Stages:
        CLOSE = 1
        OPEN = 2
        WAIT_PLAYERS_ACTIONS = 3
        WAIT_TILL_CLOSE = 4
        WAIT_TILL_OPEN = 5
        WAIT_TO_CLOSE_AGAIN = 6

    if task.stack == []:
        stage = Stages.CLOSE
        start_time = time.time()
        task.stack.append(stage)
        task.stack.append(start_time)

    start_time = task.stack.pop()
    stage = task.stack.pop()

    passed_time = time.time() - start_time

    if Stages.CLOSE == stage:
        print("(REQ:{task_id}) CLOSE_THE_DOOR!".format(task_id=task.id))

        # set signal to device for close door
        relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
        relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.RELAY_CLOSE
        master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

        start_time = time.time()
        # change state to wait till close
        stage = Stages.WAIT_TILL_CLOSE
        pass
    elif Stages.WAIT_TILL_CLOSE == stage:
        if passed_time > TIME_TO_CLOSE:
            # check is door really close, or something happend
            buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
            if buttons[DEVICES_TABLE.BTN_DOOR_OPEN]:
                print("(REQ:{task_id}) DOOR STILL OPEN."
                      " SOMETHING HAPPEND, need to open it!".format(
                            task_id=task.id))
                # door still open we must open doorPLAYERS NOT ACTIVE
                start_time = time.time()
                stage = Stages.OPEN
            else:
                print("(REQ:{task_id}) DOOR_CLOSED"
                      " WAIT PLAYERS ACTIONS!".format(
                        task_id=task.id))
                return True

    elif Stages.OPEN == stage:
        print("(REQ:{task_id}) OPEN_THE_DOOR!".format(task_id=task.id))
        start_time = time.time()

        relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
        relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.RELAY_OPEN
        master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

        stage = Stages.WAIT_TILL_OPEN

    elif Stages.WAIT_TILL_OPEN == stage:
        if passed_time > TIME_TO_OPEN:
            print(
                "(REQ:{task_id}) DOOR OPENED, WAIT_TO_CLOSE IT AGAIN!".format(
                    task_id=task.id))
            # door may be opened
            # we must start wait till close again
            start_time = time.time()
            stage = Stages.WAIT_TO_CLOSE_AGAIN


    elif Stages.WAIT_TO_CLOSE_AGAIN == stage:
        if passed_time > TIME_BEFORE_CLOSE_AGAIN:
            start_time = time.time()
            stage = Stages.CLOSE

    task.stack.append(stage)
    task.stack.append(start_time)


def AC_OPEN_MIRROR(master, task, game_state):
    # finaly close the door
    time.sleep(1)
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.RELAY_CLOSE
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

    sl_control = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_control[DEVICES_TABLE.SL_MIRROR_IN_CLOSET] = 1
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_control)
    time.sleep(1)
    sl_control[DEVICES_TABLE.SL_MIRROR_IN_CLOSET] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_control)


def AC_ADD_PLAY_DIVISION(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_DIVISION)


def REQ_PLAY_DIVISION(master, task, game_state):
    DELAY_TIME = 1
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.division)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.division)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_ADD_PLAY_DAGON_PRIVATE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_DAGON_PRIVATE)


def REQ_PLAY_DAGON_PRIVATE(master, task, game_state):
    DELAY_TIME = 3
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.dagon_private)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.dagon_private)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)



def AC_PERFORMANCE_GIRL_GONE(master, task, game_state):
    print("(ACTION:{task_id}) Performance - girl gone".format(task_id=task.id))
    pass


def AC_ADD_ANOMALOUS_PHENOMENA(master, task, game_state):
    game_state.add_active_task_with_id(
        TASKS_IDS.ANOMALOUS_PHENOMENA_ENTER_NUMBERS)




def REQ_ANOMALOUS_PHENOMENA_ENTER_NUMBERS(master, task, game_state):
    adcs = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()
    number_1 = adcs[DEVICES_TABLE.BOX_LOCK_SYMBOL_1]
    number_2 = adcs[DEVICES_TABLE.BOX_LOCK_SYMBOL_2]
    number_3 = adcs[DEVICES_TABLE.BOX_LOCK_SYMBOL_3]

    if not master.debugMode():
        print(
            "ANOMALOUS_PHENOMENA_ENTER_NUMBERS:\n number1: {}\tnumber2: {}\tnumber3: {}".format(
                number_1,
                number_2,
                number_3))

    number_ok_1 = DEVICES_TABLE.SYMBOL_1_VALUE_RANGE[
        0] <= number_1 <= DEVICES_TABLE.SYMBOL_1_VALUE_RANGE[1]
    number_ok_2 = DEVICES_TABLE.SYMBOL_2_VALUE_RANGE[
        0] <= number_2 <= DEVICES_TABLE.SYMBOL_2_VALUE_RANGE[1]
    number_ok_3 = DEVICES_TABLE.SYMBOL_3_VALUE_RANGE[
        0] <= number_3 <= DEVICES_TABLE.SYMBOL_3_VALUE_RANGE[1]
    print("numok 1: {} | 2: {} | 3: {}".format(
        number_ok_1, number_ok_2, number_ok_3))

    return number_ok_1 and number_ok_2 and number_ok_3


def AC_OPEN_CLOSET_BOX_WITH_KNIFE(master, task, game_state):
    print(
        "(ACTION:{task_id}) Closet box with knife opened".format(
            task_id=task.id))
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_BOX_IN_CLOSET_WITH_KNIFE] = DEVICES_TABLE.OPEN

    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def AC_ADD_PLAY_KNIFE_ACHIEVED(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_KNIFE_ACHIEVED)


def REQ_PLAY_KNIFE_ACHIEVED(master, task, game_state):
    DELAY_TIME = 3
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.knife_achieved)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.knife_achieved)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_ADD_PLAY_OLD_MAN_MONOLOG(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_OLD_MAN_MONOLOG)


def REQ_PLAY_OLD_MAN_MONOLOG(master, task, game_state):
    DELAY_TIME = 5
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.old_man)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.old_man)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_ADD_MARINE_TROPHIES(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.MARINE_TROPHIES)


class pColors:
    RED = COLORS.RED
    GREEN = COLORS.GREEN
    BLUE = COLORS.BLUE


def AC_SET_RANDOM_FISH_EYES(master, task, game_state):
    ALLOW_COLORS = [pColors.RED, pColors.GREEN, pColors.BLUE]

    for iteration in range(30):

        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        for index in range(5):
            smart_leds.setOneLed(
                DEVICES_TABLE.SML_FISH_EYES[index],
                ALLOW_COLORS[random.randint(0,2)])

        time.sleep(0.5)


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
    WINNER_EYES_CLOLORS = [pColors.RED] * 5
    if task.stack == []:

        knife_slots = [1] * len(DEVICES_TABLE.BTN_KNIFE_SLOTS)

        # init eyes
        # fishes_eyes = [pColors.RED] * 5
        fishes_eyes = [pColors.RED, pColors.GREEN, pColors.BLUE,
                       pColors.BLUE, pColors.GREEN]

        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        for index in range(len(knife_slots)):
            smart_leds.setOneLed(
                DEVICES_TABLE.SML_FISH_EYES[index],
                fishes_eyes[index])

        task.stack.append(knife_slots)
        task.stack.append(fishes_eyes)

    fishes_eyes = task.stack.pop()
    old_knife_slots = task.stack.pop()

    # get knife slots status
    buttons = master.getButtons(Devices.LOVECRAFT_DEVICE_NAME).get()
    knife_slots = []
    for slot_index in range(len(DEVICES_TABLE.BTN_KNIFE_SLOTS)):
        knife_slots.append(
                buttons[DEVICES_TABLE.BTN_KNIFE_SLOTS[slot_index]])

    if knife_slots != old_knife_slots:
        for index in range(len(knife_slots)):
            if (knife_slots[index] != old_knife_slots[
                    index]) and (knife_slots[index] == 0):
                fishes_eyes[index] = toggleEyeColor(fishes_eyes[index])
                if index == 0:
                    fishes_eyes[index + 1] = toggleEyeColor(
                        fishes_eyes[index + 1])
                elif index == len(fishes_eyes) - 1:
                    fishes_eyes[index - 1] = toggleEyeColor(
                        fishes_eyes[index - 1])
                else:
                    fishes_eyes[index - 1] = toggleEyeColor(
                        fishes_eyes[index - 1])
                    fishes_eyes[index + 1] = toggleEyeColor(
                        fishes_eyes[index + 1])

        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        for index in range(len(knife_slots)):
            smart_leds.setOneLed(
                DEVICES_TABLE.SML_FISH_EYES[index],
                fishes_eyes[index])

    if knife_slots != old_knife_slots:
        print("(REQ:{task_id}) Knife slots changed: {slots}".format(
                  task_id=task.id, slots=knife_slots))
        print(
            "(REQ:{task_id}) Knife slots changed: colors {eyes}".format(
                task_id=task.id,
                eyes=fishes_eyes))
        old_knife_slots = knife_slots

    if WINNER_EYES_CLOLORS == fishes_eyes:
        print("(REQ:{task_id}) Fishes eyes done!!!!: {slots}".format(
                  task_id=task.id, slots=knife_slots))
        return True

    task.stack.append(old_knife_slots)
    task.stack.append(fishes_eyes)


def AC_ADD_OPEN_STOORE_ROOM_DOOR(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.OPEN_STOORE_ROOM_DOOR)

def REQ_OPEN_STOORE_ROOM_DOOR(master, task, game_state):
    DELAY_TIME = 5
    if task.stack == []:
        sound_start = False
        task.stack.append(time.time())

    start_time = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(start_time)
        return

    print("(ACTION:{task_id}) Open door with skelet".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_WITH_SKELET] = DEVICES_TABLE.RELAY_OPEN
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)
    return True

def AC_OPEN_DOOR_WITH_SKELET(master, task, game_state):
    print("(ACTION:{task_id}) Open door with skelet".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_WITH_SKELET] = DEVICES_TABLE.RELAY_OPEN
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

def AC_ADD_PLAY_AFTER_SKELET_DOOR_OPEN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_AFTER_SKELET_DOOR_OPEN)

def REQ_PLAY_AFTER_SKELET_DOOR_OPEN(master, task, game_state):
    DELAY_TIME = 3
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.after_skelet_door_open)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.after_skelet_door_open)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)


def AC_OPEN_CLOSET_DOOR(master, task, game_state):
    print("(ACTION:{task_id}) Open closet".format(task_id=task.id))
    relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
    relays[DEVICES_TABLE.RELAY_CLOSET_DOOR_1] = DEVICES_TABLE.RELAY_OPEN
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)


def AC_ADD_PUT_FOURTH_COIN(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_FOURTH_COIN)


def REQ_PUT_FOURTH_COIN(master, task, game_state):
    return check_coins_inserted(master, task, game_state, 4)


def AC_ADD_PLAY_ALL_COINS_ON_PLACE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_ALL_COINS_ON_PLACE)

def REQ_PLAY_ALL_COINS_ON_PLACE(master, task, game_state):
    DELAY_TIME = 0
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.all_coins_on_place)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.all_coins_on_place)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)

def AC_SOUND_BACKGROUND_STAGE_4(master, task, game_state):
    game_state.sound_manager.stop(SOUNDS.stage_3)
    game_state.sound_manager.play_sound(SOUNDS.stage_4)


def AC_PERFORMANCE_CULMINATION(master, task, game_state):
    print("(ACTION:{task_id}) Performance culmination".format(task_id=task.id))



def AC_ADD_THE_FINAL(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.THE_FINAL)


def REQ_THE_FINAL(master, task, game_state):
    pass


def AC_ADD_PLAY_CHEST(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_CHEST)

def REQ_PLAY_CHEST(master, task, game_state):
    DELAY_TIME = 0
    if task.stack == []:
        sound_start = False
        task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    if spend_time < DELAY_TIME:
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return
    elif not sound_start:
        game_state.sound_manager.play_sound(SOUNDS.chest)
        sound_start = True
        task.stack.append(sound_start)
        task.stack.append(start_time)
        return


    playing = game_state.sound_manager.is_playing(SOUNDS.chest)

    if not playing:
        return True

    task.stack.append(sound_start)
    task.stack.append(start_time)

def AC_THE_FINAL(master, task, game_state):
    print("(ACTION:{task_id}) The final".format(task_id=task.id))

def AC_LIGHT_SHOW_WHERE_PICTURE_BOX(master, task, game_state):
    print("(ACTION:{task_id}) show light where locker".format(task_id=task.id))
    smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.ROOM_GREEN)
    smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, COLORS.ROOM_GREEN)

def AC_OPEN_PICTURE_BOX(master, task, game_state):
    print("(ACTION:{task_id}) Open picture box".format(task_id=task.id))

    sl_control = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_control[DEVICES_TABLE.SL_BOX_UNDER_PICTURE] = DEVICES_TABLE.OPEN
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_control)


def AC_ADD_TIMER_PLAY_LIFESAVER_END(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.TIMER_PLAY_LIFESAVER_END)

def AC_ADD_TIMER_PLAY_BAD_END(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.TIMER_PLAY_BAD_END)

def REQ_TIMER_PLAY_LIFESAVER_END(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()
    passed_time = time.time() - start_time

    if passed_time <= DEVICES_TABLE.TIMER_PLAY_LIFESAVER_END:
        task.stack.append(start_time)
        return

    return True


def REQ_TIMER_PLAY_BAD_END(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()
    passed_time = time.time() - start_time

    if passed_time <= DEVICES_TABLE.TIMER_PLAY_BAD_END:
        task.stack.append(start_time)
        return

    return True


def AC_PLAY_BAD_END(master, task, game_state):
    print("(ACTION:{task_id}) Play Bad end".format(task_id=task.id))
    game_state.sound_manager.play_sound(SOUNDS.bad_end)


def AC_PLAY_LIFESAVER_END(master, task, game_state):
    print("(ACTION:{task_id}) Play lifesaver end".format(task_id=task.id))
    game_state.sound_manager.play_sound(SOUNDS.lifesaver_end)


def AC_ADD_TIMER_SCARE_WINDOW(master, task, game_state):
    print("(ACTION:{task_id}) Timer start for SCARE in WINDOW".format(task_id=task.id))
    game_state.add_active_task_with_id(TASKS_IDS.TIMER_SCARE_WINDOW)


def REQ_TIMER_SCARE_WINDOW(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()
    passed_time = time.time() - start_time

    if passed_time <= DEVICES_TABLE.TIMER_SCARE_WINDOW:
        task.stack.append(start_time)
        return

    return True


def AC_SCARE_WINDOW(master, task, game_state):
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_SCARE_WINDOW] = 1
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    time.sleep(3)
    sl_controlls[DEVICES_TABLE.SL_SCARE_WINDOW] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)


def AC_ADD_TIMER_SCARE_HEAD(master, task, game_state):
    print("(ACTION:{task_id}) Timer start for SCARE HEAD".format(task_id=task.id))
    game_state.add_active_task_with_id(TASKS_IDS.TIMER_SCARE_HEAD)


def REQ_TIMER_SCARE_HEAD(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()
    passed_time = time.time() - start_time

    if passed_time <= DEVICES_TABLE.TIMER_SCARE_HEAD:
        task.stack.append(start_time)
        return

    return True

def AC_SCARE_HEAD_APPEARANCE(master, task, game_state):
    sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
    sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_MOTOR] = 1
    sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_ACTION] = DEVICES_TABLE.HEAD_ACTION_APPEAR
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
    time.sleep(0.5)
    sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_MOTOR] = 0
    master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

def AC_ADD_TIMER_PICTURE_BOX(master, task, game_state):
    print("(ACTION:{task_id}) Timer start for OPEN PICTURE BOX".format(task_id=task.id))
    game_state.add_active_task_with_id(TASKS_IDS.TIMER_PICTURE_BOX)


def REQ_TIMER_PICTURE_BOX(master, task, game_state):
    if task.stack == []:
        start_time = time.time()
        task.stack.append(start_time)

    start_time = task.stack.pop()
    passed_time = time.time() - start_time

    if passed_time <= DEVICES_TABLE.TIMER_PICTURE_BOX:
        task.stack.append(start_time)
        return

    return True


def AC_ADD_PLAY_DOLL_HELP(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_DOLL_HELP)

def REQ_PLAY_DOLL_HELP(master, task, game_state):
    DELAY_TIME = 7
    if task.stack == []:
        game_state.sound_manager.play_sound(SOUNDS.doll)
        # task.stack.append(sound_start)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    # sound_start = task.stack.pop()
    spend_time = time.time() - start_time

    playing = game_state.sound_manager.is_playing(SOUNDS.doll)
    if playing:
        task.stack.append(time.time())
        return

    if spend_time < DELAY_TIME:
        task.stack.append(start_time)
        return

    GLOBAL_VARIABLES.SOUND_ARRAY.append({
          'sound': SOUNDS.girl_help,
          'delay': 3,
          'delay_start': False,
          'play_start': False,
          'play_done': False
    })

    # game_state.sound_manager.play_sound(SOUNDS.girl_help)
    return True


def AC_ADD_PLAY_BACKGROUND_SOUND(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_BACKGROUND_SOUND)

def REQ_PLAY_BACKGROUND_SOUND(master, task, game_state):

    playing = game_state.sound_manager.is_playing(SOUNDS.stage_1)
    if not playing:
        game_state.sound_manager.play_sound(SOUNDS.stage_1)


def AC_ADD_FINAL_DAGON(master, task, game_state):
    print("ACTION: Add final dagon")
    game_state.add_active_task_with_id(TASKS_IDS.FINAL_DAGON)


def REQ_FINAL_DAGON(master, task, game_state):
    # TIME
    OPERATOR_SOUND_DELAY = 10

    class Stages:
        COLOR_OFF = 1
        CTHULHU_APPEAR = 2
        LIGHTNING = 3
        RED_LIGHT_ON_CTHULHU = 4
        CTHULHU_START_TALKING = 5
        CTHULHU_TALK = 6
        LIGHT_OFF_CTHULHU_DISAPPEAR = 7
        LIGHTNING_AGAIN = 8
        TURN_ON_RED_LIGHT = 9
        # RADIO_1_START
        PLAY_RADIO_1 = 10
        PLAY_RADIO_2 = 11
        FINALE_MUSIC = 12
        FINALE_OPERATOR = 13
        WAIT_TILL_OPERATOR_END = 14

    if task.stack == []:
        stage = Stages.COLOR_OFF
        start_time = time.time()
        task.stack.append(stage)
        task.stack.append(start_time)

    start_time = task.stack.pop()
    stage = task.stack.pop()

    passed_time = time.time() - start_time

    if Stages.COLOR_OFF == stage:
        AC_OFF_EDDISON_LIGHT(master, task, game_state)
        # off all light-diod
        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        init_color = COLORS.OFF
        smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, init_color)
        smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, init_color)
        smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, init_color)
        smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, init_color)

        stage = Stages.CTHULHU_APPEAR

    elif Stages.CTHULHU_APPEAR == stage:
        AC_SCARE_HEAD_APPEARANCE(master, task, game_state)

        stage = Stages.LIGHTNING

    elif Stages.LIGHTNING == stage:
        AC_LIGHTNING(master, task, game_state)

        stage = Stages.RED_LIGHT_ON_CTHULHU

    elif Stages.RED_LIGHT_ON_CTHULHU == stage:
        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.ROOM_RED)

        stage = Stages.CTHULHU_START_TALKING

    elif Stages.CTHULHU_START_TALKING == stage:
        game_state.sound_manager.play_sound(SOUNDS.cthulhu_appear)

        stage = Stages.CTHULHU_TALK

    elif Stages.CTHULHU_TALK == stage:
        playing = game_state.sound_manager.is_playing(SOUNDS.cthulhu_appear)
        if not playing:
            stage = Stages.LIGHT_OFF_CTHULHU_DISAPPEAR

    elif Stages.LIGHT_OFF_CTHULHU_DISAPPEAR == stage:

        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, COLORS.OFF)

        # head turn back
        sl_controlls = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()
        sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_MOTOR] = 1
        sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_ACTION] = DEVICES_TABLE.HEAD_ACTION_HIDE
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)
        time.sleep(1)
        sl_controlls[DEVICES_TABLE.SL_HEAD_WINDOW_MOTOR] = 0
        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sl_controlls)

        stage = Stages.LIGHTNING_AGAIN

    elif Stages.LIGHTNING_AGAIN == stage:
        AC_LIGHTNING(master, task, game_state)

        stage = Stages.TURN_ON_RED_LIGHT

    elif Stages.TURN_ON_RED_LIGHT == stage:
        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)
        init_color = COLORS.ROOM_RED
        smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, init_color)
        smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, init_color)
        smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, init_color)
        smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, init_color)

        stage = Stages.PLAY_RADIO_1

    elif Stages.PLAY_RADIO_1 == stage:
        if task.stack == []:
            game_state.sound_manager.play_sound(SOUNDS.lifesaver_end_first)
            task.stack.append(None)
        task.stack.pop()
        playing = game_state.sound_manager.is_playing(SOUNDS.lifesaver_end_first)

        if not playing:
            stage = Stages.PLAY_RADIO_2
        else:
            task.stack.append(None)


    elif Stages.PLAY_RADIO_2 == stage:
        if task.stack == []:
            game_state.sound_manager.play_sound(SOUNDS.lifesaver_end_second)
            task.stack.append(None)
        task.stack.pop()
        playing = game_state.sound_manager.is_playing(SOUNDS.lifesaver_end_second)

        if not playing:
            stage = Stages.FINALE_MUSIC
        else:
            task.stack.append(None)

    elif Stages.FINALE_MUSIC == stage:
        game_state.sound_manager.play_sound(SOUNDS.music_on_demon_wings)

        stage = Stages.FINALE_OPERATOR
        start_time = time.time()

    elif Stages.FINALE_OPERATOR == stage:
        if passed_time > OPERATOR_SOUND_DELAY:
            game_state.sound_manager.play_sound(SOUNDS.operator_end)
            stage = Stages.WAIT_TILL_OPERATOR_END


    elif Stages.WAIT_TILL_OPERATOR_END == stage:
        playing = game_state.sound_manager.is_playing(SOUNDS.operator_end)

        if not playing:
            AC_ON_EDDISON_LIGHT(master, task, game_state)
            return True

    task.stack.append(stage)
    task.stack.append(start_time)

def AC_ADD_PLAY_SOUND_ARRAY(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PLAY_SOUND_ARRAY)


def REQ_PLAY_SOUND_ARRAY(master, task, game_state):
    """ SOUND_ARRAY FORMAT:
        [
            {
                sound: sound,
                delay: "delay in sec",
                delay_start: "True|False",
                play_start: "True|False",
                play_done: "True|False",
            }
        ]
    """
    if task.stack == []:
        delay = 0
        task.stack.append(delay)
        task.stack.append(time.time())

    start_time = task.stack.pop()
    delay = task.stack.pop()
    spend_time = time.time() - start_time
    if spend_time < delay:
        task.stack.append(delay)
        task.stack.append(start_time)
        return

    if GLOBAL_VARIABLES.SOUND_ARRAY == []:
        task.stack.append(delay)
        task.stack.append(start_time)
        return

    sounds_list = GLOBAL_VARIABLES.SOUND_ARRAY
    for sound_object in sounds_list:
        if sound_object['play_done']:
            continue
        if sound_object['play_start']:
            playing = game_state.sound_manager.is_playing(sound_object['sound'])
            if playing:
                task.stack.append(delay)
                task.stack.append(start_time)
                return
            sound_object['play_start'] = False
            sound_object['play_done'] = True
            print("Stop play sound ")

    # now if no one sound is playing we can find some one who not play yet
    for sound_object in sounds_list:
        if sound_object['play_done']:
            continue
        if not sound_object['play_start']:
            if sound_object['delay_start']:
                sound_object['delay_start']= False
                game_state.sound_manager.play_sound(sound_object['sound'])
                sound_object['play_start'] = True
                print("Start play sound ")
            else:
                sound_object['delay_start']= True
                delay = sound_object['delay']
                start_time = time.time()
                print("Start delay {}s for sound".format(delay))
            break


    task.stack.append(delay)
    task.stack.append(start_time)
    return


