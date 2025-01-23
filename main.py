import os
import subprocess


def is_h265(file):
    """
    Checks if a video file is already encoded in H.265 (HEVC).
    """
    # FFmpeg command to inspect the video codec
    command = [
        "ffmpeg",
        "-i", file,  # Input file
        "-c", "copy", # Copy codec (no re-encoding)
        "-f", "null", # No output file
        "-"           # Output to null
    ]

    # Run the FFmpeg command and capture stderr
    result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    # Check if "hevc" (H.265) is in the output
    return "hevc" in result.stderr.decode().lower()


def convert_video_to_h265(file):
    """
    Converts a video file to H.265 (HEVC) at 30fps using ffmpeg.
    Overwrites the original file in place.
    """
    # Temporary file for conversion
    temp_file = f"{os.path.splitext(file)[0]}.temp{os.path.splitext(file)[1]}"

    # FFmpeg command to convert the video
    command = [
        "ffmpeg",
        "-i", file,               # Input file
        "-c:v", "libx265",        # Video codec: H.265
        "-vf", "fps=30",          # Set frame rate to 30fps
        "-c:a", "copy",           # Copy audio stream without re-encoding
        temp_file,                # Output to temporary file
        "-y"                      # Overwrite temporary file if it exists
    ]

    print("\n\n\n\n")
    print("*"*100)
    print(f"Converting {file} to H.265")
    print(command)


    # Run the FFmpeg command
    result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    # Check if the conversion was successful
    if result.returncode == 0:
        # Overwrite the original file with the converted file
        os.replace(temp_file, file)
        print(f"Converted: {file}")
    else:
        # Remove the temporary file if conversion failed
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"Failed to convert: {file}")
        print(f"ERROR: {result.stderr.decode()}")
    print("*" * 100)


def process_directory(directory):
    """
    Recursively walks through a directory and processes video files.
    """
    # Supported video file extensions
    video_extensions = (".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv")

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(video_extensions):
                file_path = os.path.join(root, file)

                if is_h265(file_path):
                    print(f"Skipping {file}")
                    continue
                else:
                    print(f"Processing {file}")
                    convert_video_to_h265(file_path)


if __name__ == "__main__":
    # Directory containing the videos
    video_directory = "your directory here"
    # Process the directory
    process_directory(video_directory)