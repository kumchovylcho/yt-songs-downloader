# YouTube Downloader with yt-dlp

This project is a Python script that uses `yt-dlp` to download audio from YouTube. It allows users to:

- Download audio files in high-quality MP3 format.
- Use a text file to batch-download multiple YouTube links.

---

## Features

1. **Audio Downloading**:
   - Download the best quality audio as MP3.

2. **Batch Downloading**:
   - Provide a text file containing YouTube URLs, and the script will download them all.

3. **Automatic Directory Management**:
   - Automatically creates output directories if they don't exist.

---

## Prerequisites

1. **Python**:
   - Install Python 3.x on your WSL environment.
   - Ensure `python3-venv` is installed for creating virtual environments.

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

2. **FFmpeg**:
   - Install FFmpeg to handle audio and video processing:
     ```bash
     sudo apt install ffmpeg
     ```

---

## How to Use

### Step 1: Clone the Repository

Clone the project or copy the script into your working directory.

```bash
git clone https://github.com/kumchovylcho/yt-songs-downloader
cd youtube-downloader
```

### Step 2: Create and Activate a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Customization

1. **Output Directory**:
   - Update the `output_directory` variable in the script to specify your desired folder.

   Example:
   `/mnt/` to access windows.
   ```python
   output_directory = "/mnt/d/my_folder"
   ```
---

## Known Issues and Troubleshooting

1. **Files Not Saving in the Correct Directory**:
   - Ensure the Windows path is correctly mounted in WSL (e.g., `/mnt/`). `mnt` is used to access windows path from wsl.

2. **Permissions Error**:
   - Run the script with sufficient permissions if accessing restricted directories.

3. **FFmpeg Missing**:
   - Ensure FFmpeg is installed and accessible in the WSL environment.

