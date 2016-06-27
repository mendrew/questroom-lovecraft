#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import tornado.websocket
# from GameState import GameState
from quest_core import GameState
from time import sleep
# from SoundManager import SoundManager
from quest_room import QuestRoom
# from sound_manager import play_sound

from tornado.options import define, options, parse_command_line
import json

define("port", default=8888, help="run on the given port", type=int)

clients = dict()
quest_room = None
# sound_manager = None
keyboard_listener = None

# class IndexHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         self.render('index.html')


class DashboardHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.render('public/dashboard.html')


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self, *args):
        self.id = self.get_argument("Id")
        self.stream.set_nodelay(True)
        if self.id in clients:
            del clients[self.id]
        clients[self.id] = {"id": self.id, "object": self}

        id_str = str(self.id)
        # print("quest last_sended_messages: {}".format(
        #     quest_room.last_sended_messages))

        init_data = {'init': 'True'}
        self.write_message(init_data)

        if id_str in quest_room.last_sended_messages:
            last_data = quest_room.last_sended_messages[id_str]
            self.write_message(last_data)

        quest_room.send_state(None)

    def on_message(self, jsonMessage):
        message = json.loads(jsonMessage)
        print(message)
        print(message['message'])

        if "play_sound" == message['message']:
            sound_id = message['sound']
            quest_room.play_sound(sound_id)

        if "door" == message['message']:
            door_id = int(message['door_id'])
            door_state = message['state']
            print("Set door state {}   {}".format(door_id, door_state))
            quest_room.set_door_state(door_id, door_state)

        if "box" == message['message']:
            box_id = int(message['box_id'])
            box_state = message['state']
            quest_room.set_box_state(box_id, box_state)

        if "moving_picture" == message['message']:
            picture_id = int(message['picture_id'])
            print("Change picture with id: {}".format(picture_id))
            quest_room.change_picture(picture_id)

        if "skip_task" in message['message']:
            if message['task_id'].isdigit():
                task_id = int(message['task_id'])
                quest_room.toggle_skiped_task(task_id)

        if "add_task" in message['message']:
                quest_room.add_task(message['task'])

        if "light" == message['message']:
            quest_room.turn_light(message['light_id'], message['action'])

        if "scare_face_turn" == message['message']:
            quest_room.scare_face_turn(int(message['action']))

        if "table_ring_out" == message['message']:
            quest_room.table_ring_out()

        if "mirror_on" == message['message']:
            quest_room.mirror_on()

        if "set_room_light" == message['message']:
            room_led = message['room_led_id']
            rgb_color_str = message['color']
            rgb_color = [
                int(char_h + char_l, 16) for char_h,
                char_l in zip(rgb_color_str[0:: 2],
                              rgb_color_str[1:: 2])]
            print(
                "We receive set_room_light with room_led_id:"
                " {} and color {} = {}".format(
                    room_led, rgb_color_str, rgb_color))

            quest_room.set_room_light(room_led, rgb_color)

        if "aquarium_pump" == message['message']:
            pump_action = message['action']
            quest_room.pump_out(int(pump_action))

        if "eyes_pump" == message['message']:
            pump_action = message['action']
            quest_room.pump_in(int(pump_action))

        if "aquarium_pump_in" == message['message']:
            quest_room.aquarium_pump_in()

        if "aquarium_pump_out" == message['message']:
            quest_room.aquarium_pump_out()

    def on_close(self):
        if self.id not in clients:
            return
        del clients[self.id]

app = tornado.web.Application([
    # (r'/', IndexHandler),
    (r'/dashboard', DashboardHandler),
    (r'/socket', WebSocketHandler),
    ],
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    autoreload=True,
)

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    # sound_manager = SoundManager()
    # sound_manager.daemon = True
    # sound_manager.start()
    quest_room = QuestRoom(clients)
    # quest_room.sound_manager = sound_manager
    quest_room.start()
    tornado.ioloop.IOLoop.instance().start()
