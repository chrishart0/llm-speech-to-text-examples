import whisper
import os

base_file_path = "audio/"
file_name = "test.mp3"
file_path = base_file_path + file_name

# Available models: "tiny", "small", "medium", "large"
# Read more here: https://pypi.org/project/openai-whisper/20231117/
# model = whisper.load_model("tiny")
model = whisper.load_model("large")

result = model.transcribe(file_path)
print(result["text"])

# Split text into sentences by adding a new line after each sentence
result["text"] = result["text"].replace(". ", ".\n")

# Write the transcribed text to a file
# Make dir if not exists
if not os.path.exists("transcribed_text"):
    os.makedirs("transcribed_text")

# Write transcript to file
with open(f"transcribed_text/{file_name}.txt", "w") as file:
    file.write(result["text"])