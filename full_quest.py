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
    return True

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

def REQ_PUT_FIRST_COIN(master, task, game_state):
    adc_list = master.getAdc(Devices.LOVECRAFT_DEVICE_NAME).get()

    adc_coins_values = (adc_list[DEVICES_TABLE.COIN_1],
            adc_list[DEVICES_TABLE.COIN_2],
            adc_list[DEVICES_TABLE.COIN_3],
            adc_list[DEVICES_TABLE.COIN_4])

    inserted_coins_number = 0
    for index, coin_value in adc_coins_values:
        if DEVICES_TABLE.COIN_INSERTED_RANGE(0) <= coin_value <= DEVICES_TABLE.COIN_INSERTED_RANGE(1):
            inserted_coins_number = inserted_coins_number + 1

    if inserted_coins_number >= 1:
        return True
    return True

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



# =====================================================
# =====================================================
# =====================================================
# =====================================================
# =====================================================
# =====================================================
