from __future__ import print_function

from quest_core import parse
from quest_core import Requirement
from quest_core import Task
from quest_core import GameState
from quest_core import SoundManager

from settings import Devices
from settings import Global
from settings import DEVICES_TABLE
from settings import SOUNDS_NAMES
from settings import SOUNDS
from settings import COLORS


from deviceMaster.devicemaster import DeviceMaster

import time
import threading
import tornado
import subprocess
# import pygame
import platform

from full_quest import *



clients = None
master = None
class QuestRoom(threading.Thread):

    def __init__(self, cli):
        global clients
        clients = cli
        self.game_state = None

        self.last_sended_messages = {}

        super(QuestRoom, self).__init__()

    def run(self):
        print("quest room thread start")
        global master
        master = DeviceMaster()

        if platform.system() == 'Windows':
            lovecraft_comport = Devices.LOVECRAFT_DEVICE_COM_PORT_WIN
        else:
            if master.debugMode():
                lovecraft_comport = Devices.LOVECRAFT_DEVICE_COM_PORT_WIN
            else:
                lovecraft_comport = "/dev/ttyUSB2"
                bashCommand = Global.GET_TTY_USB_SCRIPT + Devices.LOVECRAFT_USB_SERIAL_NUMBER
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

                lovecraft_comport = process.communicate()[0]
            print("Use COM-port: {}".format(lovecraft_comport))

        self.lovecraft_device = master.addSlave(Devices.LOVECRAFT_DEVICE_NAME, lovecraft_comport, 1, boudrate=4)

        master.start()

        self.game_state = parse(Global.SCENARY_FILE)

        self.game_state.device_master = master
        self.game_state.slave = self.lovecraft_device
        self.game_state.quest_room = self
        self.game_state.sound_manager = SoundManager()
        # self.sound_manager.play()
        self.game_state.start_game_loop(self.send_state)


    def set_door_state(self, door_id, door_state):
        relays = master.getRelays(Devices.LOVECRAFT_DEVICE_NAME).get()
        print("Set door state in set_door_state in quest_room {}   {}".format(door_id, door_state))
        relays[door_id] = door_state
        master.setRelays(Devices.LOVECRAFT_DEVICE_NAME, relays)

    def set_box_state(self, box_id, box_state):
        smartLeds = master.getSmartLeds(self.hallwayPuzzles)
        if(box_state == 0):
            smartLeds.setOneLed(box_id + 8, COLORS.BLUE)
        else:
            smartLeds.setOneLed(box_id + 8, COLORS.RED)
        relays = master.getRelays(self.hallwayPuzzles).get()
        relays[box_id] = box_state
        master.setRelays(self.hallwayPuzzles, relays)

    def send_ws_message(self, client_id, message):
        # print("send_ws_message: to client {}".format(client_id))
        str_id = str(client_id)
        if str_id not in clients: return
        if 'progress_visible' not in message: message['progress_visible'] = True
        if 'countdown_active' not in message: message['countdown_active'] = True

        clients[str_id]['object'].write_message(message)

        # save last sended message
        self.last_sended_messages[str_id] = message

    def send_state(self, message):
        if self.game_state is None:
            return

        message = {'message': [u" ({}).{}".format(x.id, x.title).encode('utf-8') for x in self.game_state.active_tasks]}
        message = tornado.escape.json_encode(message)
        try:
            if '42' in clients:
                clients['42']['object'].write_message(message)
        except:
            pass

    def toggle_skiped_task(self, task_id):
        """ Skip or unskip task from questlogic"""
        for task in self.game_state.tasks:
            if task_id == task.id:
                if task in self.game_state.skipped_tasks:
                    self.game_state.skipped_tasks.remove(task)
                else:
                    self.game_state.skipped_tasks.append(task)

    def turn_light(self, light_id, action):
        global master
        sm_leds = master.getSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME).get()

        if light_id == "eddisson_lamp":
            sm_leds[DEVICES_TABLE.SL_EDDISON_LIGHT] = int(action)

        if light_id == "lightning":
            AC_LIGHTNING(master, None, self.game_state)

        master.setSimpleLeds(Devices.LOVECRAFT_DEVICE_NAME, sm_leds)

    def set_room_light(self, room_led_id, in_color):
        # convert color range from 255 to 4096
        color = [value * 16 for value in in_color]
        rooms_colors = [ color[2], color[1], color[0] ]
        fish_colors= [ color[0], color[2], color[1] ]
        # print("Color {} in new range {}".format(in_color, color))
        smart_leds = master.getSmartLeds(Devices.LOVECRAFT_DEVICE_NAME)

        if room_led_id == "storeroom":
            smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM, rooms_colors)

        elif room_led_id == "secret_storeroom":
            smart_leds.setOneLed(DEVICES_TABLE.SML_STOREROOM_SECRET, rooms_colors)

        elif room_led_id == "hall_begin":
            smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_BEGIN, rooms_colors)

        elif room_led_id == "hall_end":
            smart_leds.setOneLed(DEVICES_TABLE.SML_HALL_END, rooms_colors)

        elif room_led_id == "fishes":
            for index in DEVICES_TABLE.SML_FISH_EYES:
                smart_leds.setOneLed(index, fish_colors)
        else:
            print("Error in set_room_light in quest_room: unknown room led {}".format(room_led_id))

    def change_picture(self, picture_id):
        if picture_id == 100:
            CHANGE_MOVE_PICTURE(master, None)
        else:
            CHANGE_MOVE_PICTURE(master, picture_id)

    def button_pressed(self, button_id):
        self.game_state.state['pressed_buttons'].append(button_id)
        print(self.game_state.state)

    def play_robot(self, sound):
        self.sound_manager.play_sound(sound)

    def play_sound(self, sound_id):
        # stages
        print("Sound_id in quest_room play_sound: {}".format(sound_id))
        if sound_id in SOUNDS_NAMES.STAGE_1:
            self.play_stage_sound(SOUNDS.stage_1)

        elif sound_id in SOUNDS_NAMES.STAGE_2:
            self.play_stage_sound(SOUNDS.stage_2)

        elif sound_id in SOUNDS_NAMES.STAGE_3:
            self.play_stage_sound(SOUNDS.stage_3)

        elif sound_id in SOUNDS_NAMES.STAGE_4:
            self.play_stage_sound(SOUNDS.stage_4)

        elif sound_id in SOUNDS_NAMES.GIRL_1_HELP:
            self.game_state.sound_manager.play_sound(SOUNDS.girl_help)

        elif sound_id in SOUNDS_NAMES.GIRL_2_HEARD:
            self.game_state.sound_manager.play_sound(SOUNDS.girl_heard)

        elif sound_id in SOUNDS_NAMES.GIRL_4_SHE_ALL_I_HAVE:
            self.game_state.sound_manager.play_sound(SOUNDS.girl_she_all_i_have)

        elif sound_id in SOUNDS_NAMES.LIGHTNING:
            self.game_state.sound_manager.play_sound(SOUNDS.lightning)

        elif sound_id in SOUNDS_NAMES.LIFESAVER_1:
            self.game_state.sound_manager.play_sound(SOUNDS.lifesaver_begin)


    def play_stage_sound(self, stage_sound_file):
        for stage_sound in SOUNDS.stages:
            self.game_state.sound_manager.stop(stage_sound)
        self.game_state.sound_manager.play_sound(stage_sound_file)

