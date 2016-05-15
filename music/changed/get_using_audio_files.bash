cat ./convert_music_all.bash | awk -F '/' '{name_line=$3; split(name_line,subfields,-map_channel); if ($1 ~ /ffmpeg/) print subfields[1]}' > ./using_audio_temp.txt
awk -F'-map_channel' '{print $1 }' ./using_audio_temp.txt > ./using_audio_temp2.txt
awk 'sub("$", "\r")' ./using_audio_temp2.txt > ../original/using_audio.txt
