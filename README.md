# Example Whisper usage to do text to speech
<https://github.com/openai/whisper>


Install ffmpeg
```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

Install prereqs
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --upgrade
```

Run the python script which starts the API, as shown below.
```
python app.py
```


## Notes
mp4 -> mp3 command

```
ffmpeg -i lecture-1.mp4 -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 lecture-1.mp3
```




