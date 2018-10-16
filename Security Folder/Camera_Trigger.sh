#!/bin/bash

python piCameraCapture.py

VideoPath="$(find .  -name \*.h264)"

var1=${VideoPath%.h264}

ffmpeg -r 30 -i "$VideoPath" -vcodec copy "$var1".mp4

rm "$VideoPath"
