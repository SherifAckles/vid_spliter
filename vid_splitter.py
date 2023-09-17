from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Define the input and output file directories
input_vid = r"C:\Users\sheri\Desktop\split-input\Reggie.mp4"  # Use a raw string for Windows paths
output_dir = r"C:\Users\sheri\Desktop\split-output\\"  # Use a raw string for Windows paths and double backslashes

# Check if the input video file exists
if not os.path.isfile(input_vid):
    print(f"Error: The input video file '{input_vid}' does not exist.")
else:
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Calculate the total duration of the video in seconds
        video = VideoFileClip(input_vid)
        total_duration = video.duration

        # Split the video into 30-second segments
        segment_duration = 30  # in seconds

        # Define the range for splitting the video based on segment duration
        for start_time in range(0, int(total_duration), segment_duration):
            # Calculate the end time of the current segment
            end_time = start_time + segment_duration

            # Define the output file name for the current segment
            output_file = f"{output_dir}segment_{start_time}_{end_time}.mp4"

            # Extract the segment using ffmpeg_extract_subclip
            ffmpeg_extract_subclip(input_vid, start_time, end_time, targetname=output_file)

        print("Video segments have been successfully created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
