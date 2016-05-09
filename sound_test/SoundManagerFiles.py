from __future__ import print_function
import threading
import time
import pygame
import sys
# from Sound import Sound
from SoundCallbackFiles import Sound
# from SounFiles import Sound
# from settings import SOUNDS_NAMES
# from full_quest import SOUNDS

# def play_sound(sound_name):
#     if SOUNDS_NAMES.GIRL_1_HELP == sound_name:
#         SOUNDS.girl_1_help.play()

def run_in_thread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

class SoundManager(threading.Thread):

    def __init__(self):
        # beep = Sound('sounds/keyboard_1.wav')
        time = 0
        self.sound_stream = None
        super(SoundManager, self).__init__()


    def run(self):
        while True:
            pass
            time.sleep(1)


    def create_stream(self, sound_name):
        self.sound_stream = Sound(sound_name)

    @run_in_thread
    def play_sound(self):
        self.sound_stream.play()

    def add_sound(self, sound_name):
        self.sound_stream.addSound(sound_name)
    # def play_keyboard_beep(self):
    #     self.beep.play()
