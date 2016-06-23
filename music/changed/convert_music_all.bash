#!/bin/bash

_FORCE='-y'

## Channels:
# 0 - STORE_ROOM
# 1 - HALL
# 5 - RADIO

BUTTONS="buttons"
HELP_SOUNDS="help_sounds"

# lifesaver_begin
ffmpeg $_FORCE -i ../original/Спасатель_2.1.mp3 -map_channel -1 -map_channel -1 -map_channel 0.0.1 -map_channel 0.0.1 -map_channel 0.0.1 -map_channel 0.0.1 -ac 6 -ar 44100 lifesaver_2_1.wav
# lifesaver_end
ffmpeg $_FORCE -i ../original/Спасатель_3.1.mp3 -map_channel -1 -map_channel -1 -map_channel 0.0.1 -map_channel 0.0.1 -map_channel 0.0.1 -map_channel 0.0.1 -ac 6 -ar 44100 lifesaver_3_1.wav

# operator_end
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/14.\ Оператор,\ после\ Ктулху.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 operator_end.wav
# cthulhu_appear
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/13.\ Древний\ ужас_дагон.wav -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 cthulhu_appear.wav
# music daemon
ffmpeg $_FORCE -i ../original/13.\ Древний\ ужас_дагон.wav -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 cthulhu_appear.wav

# begin
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/1.\ Начало,\ голос\ рассказчика.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 begin.wav
# prey
ffmpeg $_FORCE -i ../original/$BUTTONS/Жертва.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 prey.wav
# names
ffmpeg $_FORCE -i ../original/$BUTTONS/Имена.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 names.wav
# picture
ffmpeg $_FORCE -i ../original/$BUTTONS/Картина.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 picture.wav
# not_understand
ffmpeg $_FORCE -i ../original/$BUTTONS/Не\ понимали.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 not_understand.wav
# division
ffmpeg $_FORCE -i ../original/$BUTTONS/Разделение.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 division.wav
# chest
ffmpeg $_FORCE -i ../original/$BUTTONS/Сундук.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 chest.wav
# closet
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/8.\ Шкаф,\ через\ 5\ сек\ после\ открытия\ шкафа.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 closet.wav
# he
ffmpeg $_FORCE -i ../original/$BUTTONS/ОН.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 he.wav


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
