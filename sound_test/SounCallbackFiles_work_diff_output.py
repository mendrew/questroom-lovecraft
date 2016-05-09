import pyaudio
import wave
import time
import sys
import numpy
from fractions import Fraction
import threading

from wavefile import WaveReader

def run_in_thread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

class Sound:
    CHUNK = 512

    def __init__(self):
        self.playing_files = []
        self.playing_files_buffers_for_read = {}
        self.store_buffers = []
        self.player_lib = pyaudio.PyAudio()
        self._volume = 1
        self.stream = None
        self.mixed = None
        self.max_channels = 0


        # self.wf = wave.open(sound_name, 'rb')
        # self.p = pyaudio.PyAudio()
        # self.device_index, self.max_channels = self.get_valid_device_info(self.p)

    def addSound(self, sound_name):
        sound_file = WaveReader(sound_name)
        self.playing_files.append(sound_file)
        self.max_channels = max(self.max_channels, sound_file.channels)
        self.playing_files_buffers_for_read[sound_file] = numpy.zeros((sound_file.channels,512), numpy.float32, order='F')
        self.store_buffers.append([None])
        self.data_list = numpy.zeros((len(self.playing_files), self.max_channels,512), numpy.float32, order='F')

    def callback(self, in_data, frame_count, time_info, status):

        for file_index, sound_file in enumerate(self.playing_files):
            nframes = sound_file.read(self.playing_files_buffers_for_read[sound_file])
            self.data_list[file_index][:sound_file.channels,:nframes] = self.playing_files_buffers_for_read[sound_file][:sound_file.channels, :nframes]

        mixed = numpy.mean(self.data_list, axis=0, out=self.mixed)

        return (mixed, pyaudio.paContinue)

    def open_stream(self):
        stream = self.player_lib.open(
            format = pyaudio.paFloat32,
            channels = self.max_channels,
            rate = self.playing_files[0].samplerate,
            frames_per_buffer = 512,
            output=True,
            stream_callback=self.callback)
        return stream

    # @run_in_thread
    def play(self, repeat_count = 1):
        if self.stream is None:
            self.stream = self.open_stream()
            self.stream.start_stream()

        # print("File: {} playing".format(self.sound_name))
        while self.stream.is_active():
            time.sleep(1)
            sys.stdout.write("."); sys.stdout.flush()
            for file_index, file in enumerate(self.playing_files):
                print("File {} nframes {}".format(file_index, file.frames))
        # stream.stop_stream()
        # stream.close()
        # self.sound_file.close()
        # self.player_lib.terminate()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self._volume_fraction = Fraction(self._volume).limit_denominator()

