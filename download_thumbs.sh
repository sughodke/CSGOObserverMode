#!/bin/bash
source ~/Documents/Env/video/bin/activate

# download_thumbs <YT Link> <Start Time> <Duration> <Output Name>


# Get the 1080p MP4 link for the given Youtube Link
URL=`python get_stream.py $1`

# Create the Output dir
mkdir $4
ffmpeg=/Users/sidghodke/Downloads/ffmpeg/ffmpeg

# Seek to the start time, 
# grab only the I-Frames
# crop to the middle horizontal third
# save as png to the output dir
# repeat for the specified duration

$ffmpeg -ss $2 -i $URL -t $3 \
  -vf "
    fps=5,
    crop=640:1080:640:0" \
  -vsync vfr $4/thumb%t.png

##  select='eq(pict_type,PICT_TYPE_I)',
##  -vsync vfr $4/thumb%05d.png

