from SoundManagerFiles import *
import time
import sys

sm = SoundManager()
sm.daemon = True
sm.start()

sm.create_stream(sys.argv[1])
sm.add_sound(sys.argv[2])
sm.play_sound()

while True:
    time.sleep(1)
