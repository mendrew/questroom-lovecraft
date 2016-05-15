cat ./convert_music_all.bash | awk -F '/' '{name_line=$3; split(name_line,subfields,-map_channel); if ($1 ~ /ffmpeg/) print subfields[1]}'
