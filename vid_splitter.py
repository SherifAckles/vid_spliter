from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#let's define the input and output file directory
#input vid
input_vid="input_vid.mp4"

#output dir
output_dir="output_segments/"

# Create the output directory if it doesn't exist
import os
os.makedirs(output_dir, exist_ok=True)

# Calculate the total duration of the video in seconds
from moviepy.video.io.VideoFileClip import VideoFileClip
video = VideoFileClip(input_vid)
total_duration = video.duration

# Split the video into 30-second segments
segment_duration = 30  # in seconds


