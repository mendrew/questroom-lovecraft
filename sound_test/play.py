from SoundCallbackFiles import Sound
import sys
import time

sound = Sound()

sound_name = sys.argv[1]
print("Add Sound: {}".format(sound_name))
first_sound = sound.addSound(sound_name)
sound.play()
sound.play_sound(first_sound)
# stream = sound.open_stream()

time.sleep(4)
sound.stop(first_sound)
for sound_name in sys.argv[2:]:
    print("Add Sound: {}".format(sound_name))
    last_sound = sound.addSound(sound_name)
    sound.play_sound(last_sound)

while True:
    time.sleep(1)
    pass
