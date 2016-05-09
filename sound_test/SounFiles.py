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

    def __init__(self, sound_name):
        self.sound_name = sound_name
        sound_file = WaveReader(sound_name)
        self.playing_files = []
        self.playing_files.append(sound_file)
        print("playing_files = {}".format(self.playing_files))
        self.player_lib = pyaudio.PyAudio()
        self._volume = 1
        self.stream = None


        # self.wf = wave.open(sound_name, 'rb')
        # self.p = pyaudio.PyAudio()
        # self.device_index, self.max_channels = self.get_valid_device_info(self.p)

    def addSound(self, sound_name):
        sound_file = WaveReader(sound_name)
        self.playing_files.append(sound_file)

    def callback(self, in_data, frame_count, time_info, status):
        data_list = []
        for sound_file in self.playing_files:
            data = sound_file.buffer(512)
            nframes = sound_file.read(data)
            sound_data = data[:, :nframes]
            data_list.append(sound_data)

        mixed = []
        max_channels_num = max( (len(element) for element in data_list) )
        max_elements_in_channel = 0
        # max_elements for
        # for frame_element in data_list:
        #     for frame_channel in frame_element:
        #         max_elements_in_channel = max(max_elements_in_channel, len(frame_channel))
        max_elements_in_channel = 512

        mixed = numpy.zeros([max_channels_num, max_elements_in_channel], dtype = data_list[0].dtype) * -1

        for frame_index, frame_data in enumerate(data_list):
            # print("Frame data {} __ {}".format(frame_index, frame_data))
            for channel_index, channel_data in enumerate(frame_data):
                mixed[channel_index][:len(frame_data[channel_index])] += frame_data[channel_index] / len(data_list)

        # print("Resuld mixed {}\ndata_list {}".format(mixed, data_list[0]))
        # mixed = data_list[0]
        data_list = data_list[0]
        # for channel_index, channel_data in enumerate(mixed):
        #     for element_index, element in enumerate(channel_data):
        #         if element != data_list[channel_index][element_index]:
        #             print("Channel: {}, el index {} not equal! mix {} data{}".format(channel_index, element_index, element, data_list[channel_index][element_index]))
        # mixed = data_list
        return (mixed, pyaudio.paContinue)


    def open_stream(self):
        # stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
        #     channels=min(self.wf.getnchannels(), self.max_channels),
        #     output_device_index=1,
        #     rate=self.wf.getframerate(),
        #     output=True)
        # return stream
        #
        stream = self.player_lib.open(
            format = pyaudio.paFloat32,
            channels = self.playing_files[0].channels,
            rate = self.playing_files[0].samplerate,
            frames_per_buffer = 512,
            output=True)
            # stream_callback=self.callback)
        return stream

    @run_in_thread
    def play(self, repeat_count = 1):
        stream = self.open_stream()
        stream.start_stream()
        # while repeat_count != 0:
        while True:
            repeat_count -= 1
            data_list = []
            for sound_file in self.playing_files:
                data = sound_file.buffer(512)
                nframes = sound_file.read(data)
                sound_data = data[:, :nframes]
                data_list.append(sound_data)

            mixed = []
            max_channels_num = max( (len(element) for element in data_list) )
            max_elements_in_channel = 0
            # max_elements for
            # for frame_element in data_list:
            #     for frame_channel in frame_element:
            #         max_elements_in_channel = max(max_elements_in_channel, len(frame_channel))
            max_elements_in_channel = 512

            mixed = numpy.zeros([max_channels_num, max_elements_in_channel], dtype = data_list[0].dtype) * -1

            for frame_index, frame_data in enumerate(data_list):
                # print("Frame data {} __ {}".format(frame_index, frame_data))
                for channel_index, channel_data in enumerate(frame_data):
                    mixed[channel_index][:len(frame_data[channel_index])] += frame_data[channel_index] / len(data_list)
                # data = self.wf.readframes(self.CHUNK)
            frame = mixed
            stream.write(frame, frame.shape[1])

            # self.wf.rewind()
            # self.sound_file.seek(0)
            # data = self.wf.readframes(self.CHUNK)

        stream.stop_stream()
        stream.close()
        self.sound_file.close()
        self.player_lib.terminate()
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self._volume_fraction = Fraction(self._volume).limit_denominator()

