#!/bin/bash

_FORCE='-y'

## Channels:
# 0 - STORE_ROOM
# 1 - HALL
# 5 - RADIO

# lifesaver_begin
ffmpeg $_FORCE -i ../original/Спасатель_2.1.mp3 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel 0.0.1 -map_channel -1 -ac 6 -ar 44100 lifesaver_2_1.wav
# lifesaver_end
ffmpeg $_FORCE -i ../original/Спасатель_3.1.mp3 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel 0.0.1 -map_channel -1 -ac 6 -ar 44100 lifesaver_3_1.wav

ffmpeg $_FORCE -i ../original/LIGHTNING-THUNDER.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 lightning_thunder.wav
ffmpeg $_FORCE -i ../original/ЭМБ_МБ_1_Шепот_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_one_whisper.wav
ffmpeg $_FORCE -i ../original/ЭМБ_МБ_2_Зов_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_two_call.wav
ffmpeg $_FORCE -i ../original/ЭМБ_МБ_3_Крик_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_three_shout.wav
ffmpeg $_FORCE -i ../original/ЭМБ_МБ_4_Безуие_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_four_madness.wav

ffmpeg $_FORCE -i ../original/1_Помоги....mp3 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_1_help.wav
ffmpeg $_FORCE -i ../original/2_Я\ слышала....mp3 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_2_i_heard.wav
ffmpeg $_FORCE -i ../original/4_Она\ всё....mp3 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_4_she_all_i_have.wav

# in hall
ffmpeg $_FORCE -i ../original/Монолог\ старика.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 old_man_monolog.wav
# in storeroom
ffmpeg $_FORCE -i ../original/Дагон_Личное_Безумие.mp3 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 dagon.wav

# in hall
ffmpeg $_FORCE -i ../original/Плохой\ конец_1.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 bad_end.wav
