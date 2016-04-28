#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Global:
    SCENARY_FILE = "./full_quest.yml"
    GET_TTY_USB_SCRIPT = "./get_ttyUSB.sh"
    INIT_TASK_ID = 0

class Devices:
    DEVICE = "DEVICE"
    LOVECRAFT_DEVICE_NAME = "LOVECRAFT_DEVICE_NAME"
    LOVECRAFT_USB_SERIAL_NUMBER = "A4033KK5"
    LOVECRAFT_DEVICE_COM_PORT_WIN = "COM3"

class Buttons:
    # CASKET_BOX =  # "Ящик под картиной?"
    pass

class DEVICES_TABLE:
    #ADC
    ADC_LORDS_TABLE_STATUE = 0
    LORDS_TABLE_STATUE_RANGE = (115, 90)
    LORDS_TABLE_STATUE_NONE_RANGE = (116, 150)

    COIN_1 = 1
    COIN_2 = 2
    COIN_3 = 3
    COIN_4 = 4
    COIN_INSERTED_RANGE = (33, 35)
    COIN_NONE_RANGE = (36, 100)

    #RELAY
    RELAY_GODS_TABLE_MOTOR = 2
    RELAY_PUSH = 3

    #Btn
    BTN_COLLECT_DAD_FISHING = 1;
    BTN_PICTURE_BARLEY_BREAK = 5;
    BTN_CODE_LOCKS_CODE_BUTTONS = 2
    BTN_CODE_LOCKS_ELSE_BUTTONS = 3

    # SimpleLeds
    SL_TABLE_CLOCK_ZERO_CMD = 0
    SL_TABLE_CLOCK_NEXT_TIME_CMD = 1

    SL_FISHING_RODS_HOLDERS = 13

    SL_WALL_CLOCK_LOCK_WITH_PICTURE = 11 # LOCK - 1
    SL_WALL_CLOCK_LOCK_WITH_COIN = 10 # LOCK - 2

    # Encoders
    WALL_CLOCK = 2

class TASKS_IDS:
    PUT_STATUE_ON_LORDS_TABLE = 1
    PUT_FIRST_COIN = 2
    COLLECT_DAD_FISHING = 3
    BACKGROUND_TABLE_CLOCK = 4
    CLOCK_SYNCHRONIZATION = 5
    FAMILY_PICTURE_BARLEY_BREAK = 6
    PUT_SECOND_COIN = 7
    CODE_LOCK = 8



