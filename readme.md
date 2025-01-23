# Video Conversion Script

This Python script recursively converts video files in a directory to H.265 (HEVC) format at 30fps using `ffmpeg`. It skips files that are already in H.265 format and overwrites the original files in place.

---

## Features

- **Recursive Directory Traversal**: Processes all video files in a directory and its subdirectories.
- **H.265 Conversion**: Converts videos to H.265 (HEVC) format at 30fps.
- **Skip Existing H.265 Files**: Detects if a video is already in H.265 format and skips it.
- **Real-Time Output**: Displays `ffmpeg` output in real-time during conversion.
- **Overwrite Original Files**: Overwrites the original video files after successful conversion.

---

## Requirements

- Python 3.x
- `ffmpeg` installed on your system.

### Install `ffmpeg`:

- On Debian/Ubuntu:
  ```bash
  sudo apt install ffmpeg
  

### Notes

Backup Your Files: The script overwrites the original video files. Make sure to back up your files before running the script.

Performance: Conversion speed depends on your system's hardware and the size of the video files.

### License

This project is licensed under the MIT License. See the LICENSE file for details.