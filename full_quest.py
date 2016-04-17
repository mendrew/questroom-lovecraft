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
    master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, [1,1,1,1])

    # AC_ENABLE_INIT_LIGHTS(master, task, game_state)
    return True

def AC_ADD_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    game_state.add_active_task_with_id(TASKS_IDS.PUT_STATUE_ON_LORDS_TABLE)

def REQ_PUT_STATUE_ON_LORDS_TABLE(master, task, game_state):
    PUT_RANGE = [20, 40]

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

# =====================================================
# =====================================================
# =====================================================
# =====================================================
# =====================================================
# =====================================================
