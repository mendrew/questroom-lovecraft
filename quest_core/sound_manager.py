import pyaudio
import time
import sys
import numpy
from fractions import Fraction
import threading

from wavefile import WaveReader

"""
    SOUNDS BUGS
    If we have only one sound file in files - than we may be hear any second time 
        some creak sound on the first channel
    Looks like it's all because of my volume managment
    now i deprecated volume
"""

def run_in_thread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

class SoundFile:
    def __init__(self, name, frame_size=512):
        self.file_pointer = WaveReader(name)
        self.name = name
        self.channels = self.file_pointer.channels
        self.data = numpy.zeros((self.channels, frame_size), numpy.float32, order='F')
        self.nframes = 1
        self.volume = 1

        self.frame_size = frame_size
        self.samplerate = self.file_pointer.samplerate

    def set_volume(self, volume=100):
        self.volume = volume / 100

    def read(self):
        self.nframes = self.file_pointer.read(self.data)
        # self.data = self.data * self.volume
        return self.data[:self.channels, :self.nframes]

class SoundManager:
    CHUNK = 512

    def __init__(self):
        self.files = []
        self.playing_files = []
        self.player_lib = pyaudio.PyAudio()
        self._volume = 1
        self.stream = None
        self.mixed = None
        self.max_channels = 0
        self.lock = threading.RLock()

        self.playing_data_list = numpy.zeros((len(self.files), self.max_channels, self.CHUNK), numpy.float32, order='F')

    def add_sound(self, sound_name):
        new_sound_file = SoundFile(sound_name)

        for sound in self.files:
            if sound.nframes == 0:
               self.files.remove(sound)

        self.files.append(new_sound_file)

        self.max_channels = max(self.max_channels, new_sound_file.channels)


        return new_sound_file


    def set_volume(self, sound, volume):
        if sound not in self.files:
            return
        sound.set_volume(volume)

    def play_sound(self, sound):
        if sound not in self.files:
            self.add_sound(sound)

        self.playing_data_list = numpy.zeros((len(self.files), self.max_channels, self.CHUNK), numpy.float32, order='F')

        # sound.file_pointer.seek(0)
        self.playing_files.append(sound)

        if self.stream is None:
            self.play()


    def stop(self, sound):
        if sound not in self.playing_files:
            return
        self.playing_data_list = numpy.zeros((len(self.files), self.max_channels, self.CHUNK), numpy.float32, order='F')
        if len(self.playing_files) == 1:
            print("Len of playing_files == 1")
            # self.stream.stop_stream()
            # self.stream.close()
            # self.stream = None
        # with self.lock:
        print("Remove playing file")
        self.playing_files.remove(sound)


    def callback(self, in_data, frame_count, time_info, status):

        # with self.lock:
        for file_index, sound_file in enumerate(self.playing_files):
            sound_file.read()
            self.playing_data_list[file_index][:sound_file.channels, :sound_file.nframes] = sound_file.data[:sound_file.channels, :sound_file.nframes]

        mixed = numpy.mean(self.playing_data_list, axis=0, out=self.mixed)

        return (mixed, pyaudio.paContinue)

    def open_stream(self):
        stream = self.player_lib.open(
            format = pyaudio.paFloat32,
            channels = self.max_channels,
            rate = self.files[0].samplerate,
            frames_per_buffer = 512,
            output=True,
            stream_callback=self.callback)
        return stream

    # @run_in_thread
    def play(self, repeat_count = 1):
        if self.stream is None:
            self.stream = self.open_stream()
            self.stream.start_stream()
        return self.stream

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self._volume_fraction = Fraction(self._volume).limit_denominator()

