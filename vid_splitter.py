from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# let's define the input and output file directory
# input vid
input_vid = "input_vid.mp4"

# output dir
output_dir = "output_segments/"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Calculate the total duration of the video in seconds
video = VideoFileClip(input_vid)
total_duration = video.duration

# Split the video into 30-second segments
segment_duration = 30  # in seconds

# Define the range for splitting the video based on segment duration
for start_time in range(0, int(total_duration), segment_duration):

    # Calculate the end time of the current segment
    end_time = start_time + segment_duration

   
