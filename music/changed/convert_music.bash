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
# lifesaver_end_first
ffmpeg $_FORCE -i ../original/Спасатель_3.1\ Первая\ часть.mp3 -map_channel -1 -map_channel -1 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel 0.0.0 -ac 6 -ar 44100  lifesaver_3_1_first.wav
ffmpeg $_FORCE -i ../original/Спасатель_3.1\ Вторая.mp3 -map_channel -1 -map_channel -1 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel 0.0.0 -ac 6 -ar 44100 lifesaver_3_1_second.wav


# girl
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/Девочка_остановись.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_please_stop.wav
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/Девочка_кто_ты.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_who_are_you.wav
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/Девочка_слышите_меня.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_hear_me.wav
# music_on_demon_wings



# begin
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/1.\ Начало,\ голос\ рассказчика.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 begin.wav
# music_on_demon_wings
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/Bohren\ \ -\ On\ Demon\ Wings.wav -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 music_on_demon_wings.wav
# begin_min_later
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/2.\ через\ 1\ мин\ после\ начала.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 begin_min_later.wav
# first_coin
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/Первая\ монета.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 first_coin.wav
# before_books_fall
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/3.\ перд\ падением\ книг.wav -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 before_books_fall.wav
# after_books_fall
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/4.\ как\ только\ книги\ упали.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 after_books_fall.wav
# fishing
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/5.\ На\ рыбалку\ -\ сразу\ же.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 fishing.wav
# clock_sync
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/6.\ Часы,\ сразу.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 clock_sync.wav
# second_coin
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/7.\ \ Вторая\ монета.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 second_coin.wav
# closet
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/8.\ Шкаф,\ через\ 5\ сек\ после\ открытия\ шкафа.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 closet.wav
# knife_achieved
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/9.\ как\ только\ получен\ нож.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 knife_achieved.wav
# all_coins_on_place
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/11.все\ монеты\ на\ месте.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 all_coins_on_place.wav
# after_skelet_door_open
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/12.\ Труп,\ через\ 3\ сек\ после\ открытия\ второй\ двери.mp3 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 after_skelet_door_open.wav
# cthulhu_appear
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/13.\ Древний\ ужас_дагон.wav -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 cthulhu_appear.wav
# operator_end
ffmpeg $_FORCE -i ../original/$HELP_SOUNDS/14.\ Оператор,\ после\ Ктулху.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 operator_end.wav

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
# he
ffmpeg $_FORCE -i ../original/$BUTTONS/ОН.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 he.wav
# doll
ffmpeg $_FORCE -i ../original/$BUTTONS/Кукла.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 doll.wav


ffmpeg $_FORCE -i ../original/LIGHTNING-THUNDER.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 lightning_thunder.wav
# ffmpeg $_FORCE -i ../original/ЭМБ_МБ_1_Шепот_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_one_whisper.wav
# ffmpeg $_FORCE -i ../original/ЭМБ_МБ_2_Зов_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_two_call.wav
# ffmpeg $_FORCE -i ../original/ЭМБ_МБ_3_Крик_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_three_shout.wav
# ffmpeg $_FORCE -i ../original/ЭМБ_МБ_4_Безуие_Зов.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 stage_four_madness.wav

ffmpeg $_FORCE -i ../original/1_Помоги....mp3 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_1_help.wav
ffmpeg $_FORCE -i ../original/2_Я\ слышала....mp3 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_2_i_heard.wav
ffmpeg $_FORCE -i ../original/4_Она\ всё....mp3 -map_channel 0.0.0 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 girl_4_she_all_i_have.wav

# in hall
ffmpeg $_FORCE -i ../original/Монолог\ старика.mp3 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 old_man_monolog.wav
# in storeroom
ffmpeg $_FORCE -i ../original/Дагон_Личное_Безумие.mp3 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 dagon.wav

# in hall
ffmpeg $_FORCE -i ../original/Плохой\ конец_1.mp3 -map_channel -1 -map_channel 0.0.0 -map_channel -1 -map_channel -1 -map_channel -1 -map_channel -1 -ac 6 -ar 44100 bad_end.wav
