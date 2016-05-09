from SoundManager import *
import time
import sys

sm = SoundManager()
sm.daemon = True
sm.start()

sm.play_sound(sys.argv[1])
sm.play_sound(sys.argv[2])

while True:
    time.sleep(1)
