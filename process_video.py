import whisper
import os

print("Loading Whisper Model...")
model = whisper.load_model("base")
print("Model Loaded Successfully!")

video_folder = "videos"
transcript_folder = "transcripts"

os.makedirs(transcript_folder, exist_ok=True)

# Change this to the video you want to process
video_name = "Concepts of Chemistry Class.mp4"

video_path = os.path.join(video_folder, video_name)

print(f"Processing: {video_name}")
print("Please wait...")

result = model.transcribe(video_path)

transcript_name = os.path.splitext(video_name)[0] + ".txt"
transcript_path = os.path.join(transcript_folder, transcript_name)

with open(transcript_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\nTranscript saved: {transcript_name}")
print("Done!")