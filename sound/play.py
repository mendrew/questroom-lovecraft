from quest_core import SoundManager
import sys
import time

sound = SoundManager()

sound_name = sys.argv[1]
print("Add Sound: {}".format(sound_name))
first_sound = sound.add_sound(sound_name)
sound.play()
sound.play_sound(first_sound)
# stream = sound.open_stream()

# time.sleep(2)
# sound.stop(first_sound)
# time.sleep(2)
# sound_name = sys.argv[2]
# mayday = sound.add_sound(sound_name)
# sound.play_sound(mayday)
# for sound_name in sys.argv[3:]:
#     print("Add Sound: {}".format(sound_name))
#     last_sound = sound.add_sound(sound_name)
#     sound.play_sound(last_sound)
#
# time.sleep(2)
# sound.setVolume(mayday,400)
while True:
    time.sleep(1)
    sys.stdout.write("."); sys.stdout.flush()
    pass
