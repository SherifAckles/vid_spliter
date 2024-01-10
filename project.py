import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def check_input_video(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: The input video file '{input_file}' does not exist.")
        return False
    return True


def split_video(input_vid, output_dir, segment_duration=30):
    try:
        video = VideoFileClip(input_vid)
        total_duration = video.duration
        os.makedirs(output_dir, exist_ok=True)

        for start_time in range(0, int(total_duration), segment_duration):
            end_time = min(start_time + segment_duration, total_duration)
            output_file = os.path.join(
                output_dir, f"segment_{start_time}_{end_time}.mp4")

            ffmpeg_extract_subclip(input_vid, start_time,
                                   end_time, targetname=output_file)

        print("Video segments have been successfully created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_input_path():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename()
    return file_path


def get_output_path():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    folder_path = filedialog.askdirectory()
    return folder_path


def main():
    print("Please select the input video file:")
    input_vid = get_input_path()

    if input_vid:
        print("Please select the output directory:")
        output_dir = get_output_path()

        if output_dir:
            if check_input_video(input_vid):
                split_video(input_vid, output_dir)


if __name__ == "__main__":
    main()
