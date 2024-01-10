# Title: WhatsApp Video Splitter
#### Video Demo: https://youtu.be/S8l2LFglzhc

## Overview
The WhatsApp Video Splitter is a Python-based tool developed to simplify the process of sharing larger video files on WhatsApp by automatically segmenting them into smaller clips that comply with WhatsApp's file size limitations. The tool provides a user-friendly interface for selecting a video file and specifying segment durations or sizes.

## Key Features
- **GUI Interface:** Utilizes tkinter to create an intuitive graphical interface for users.
- **File Selection:** Integrates filedialog to enable users to select the video file they want to split.
- **Video Processing:** Employs moviepy's VideoFileClip module to handle video file manipulation, allowing the tool to load, process, and split video clips.
- **Segmentation:** Uses ffmpeg_extract_subclip from moviepy.video.io.ffmpeg_tools to split the video into smaller segments based on user-defined durations or file size.
- **Output:** Generates multiple smaller video clips that adhere to WhatsApp's file size constraints.

## Implementation
The tool offers a straightforward process: users launch the application, select a video file through the GUI, specify the segment duration or size, and the program then splits the video into smaller clips. It uses ffmpeg under the hood for efficient video processing.

## Purpose
The primary aim of this project is to streamline the sharing of large video files on WhatsApp by providing a convenient tool that automates the process of splitting videos into smaller, shareable segments. It caters to users who encounter difficulties sending large videos on the platform due to file size restrictions.

## Usage
To use the WhatsApp Video Splitter:
1. Install necessary dependencies (tkinter, moviepy). pip install moviepy
2. Run the Python script.
3. Use the GUI to select the video file and set the segment duration or size.
4. Generate smaller clips for sharing on WhatsApp.

## Project owener
- [Sherif Moustafa AKA Ackles](https://github.com/SherifAckles)



