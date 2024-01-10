from project import check_input_video, split_video
import os


def test_check_input_video_exists():
    input_vid = r"C:\Users\sheri\Desktop\split-input\Reggie.mp4"
    assert check_input_video(input_vid) == True


def test_check_input_video_not_exists():
    test_file = r"path\to\a\nonexistent\video.mp4"  # Provide a non-existent file path
    assert check_input_video(test_file) == False


def test_split_video():
    input_vid = r"C:\Users\sheri\Desktop\split-input\Reggie.mp4"
    # Adjust the output path for testing
    output_dir = r"C:\Users\sheri\Desktop\split-output\\test\\"
    os.makedirs(output_dir, exist_ok=True)

    split_video(input_vid, output_dir)
    # Add assertions or additional checks here based on your specific needs
