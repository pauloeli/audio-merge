# Audio Merger GUI Application

This project is a simple graphical user interface (GUI) application for merging multiple audio files into one. It
supports audio files in various formats (such as MP3, OGG, WAV), and exports the merged file in MP3 format with
selectable output quality.

## Features

- Add multiple audio files (MP3, OGG, WAV) to merge.
- Remove selected audio files from the list.
- Select the desired output quality (bitrate) for the merged file.
- Save the merged file as an MP3.

## Requirements

- Python 3.x
- PyQt5
- pydub
- ffmpeg (for handling audio files)

## Installation

1. Clone the repository:

   ```sh
   git clone <repository_url>
   ```

2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Make sure `ffmpeg` is installed and accessible through your system's PATH. You can download `ffmpeg`
   from [ffmpeg.org](https://ffmpeg.org/download.html).

## Usage

1. Run the application:

   ```sh
   python audio_merger.py
   ```

2. Use the `Add Audio Files` button to select multiple audio files to merge.
3. Use the `Remove Selected` button to remove any unwanted files from the list.
4. Choose the desired output quality (bitrate).
5. Click the `Merge and Export` button to merge the files and save the output.

## Dependencies

All dependencies are listed in the `requirements.txt` file.

## requirements.txt

```
PyQt5
pydub
```

Note: You need to have `ffmpeg` installed and accessible in your system's PATH for `pydub` to work properly.

## License

This project is licensed under the MIT License.