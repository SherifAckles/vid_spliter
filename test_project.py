import os
import pytest
from project import check_input_video, split_video


@pytest.fixture(scope="module")
def sample_video(tmpdir_factory):
    # Creating a sample video file for testing purposes
    sample_vid_path = tmpdir_factory.mktemp("data").join("sample_video.mp4")
    with open(sample_vid_path, 'w') as f:
        # Write some content to the sample video file
        f.write("Sample video content")
    return str(sample_vid_path)


def test_check_input_video_existing_file(sample_video):
    # Test when an existing video file is provided
    assert check_input_video(sample_video) == True


def test_check_input_video_nonexistent_file():
    # Test when a non-existing video file is provided
    assert check_input_video(
        r"C:\Users\sheri\Desktop\split-input\Reggie.mp4") == True


def test_split_video(tmpdir):
    # Test the functionality of split_video function
    output_dir = str(tmpdir)

    sample_input_file = r"C:\Users\sheri\Desktop\split-input\Reggie.mp4"
    split_video(sample_input_file, output_dir)

    # Assertions to check if the video segments were created in the output directory
    assert os.path.exists(os.path.join(output_dir, "segment_0_30.mp4"))
    assert os.path.exists(os.path.join(output_dir, "segment_30_60.mp4"))
