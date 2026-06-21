
from youtube_transcript_api import YouTubeTranscriptApi

# YouTube video ID (from your URL)
video_id = "Y9hB-XRL5DU"

try:
    # Get transcript (English)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

    # Save as text file
    with open("subtitle.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            f.write(entry["text"] + "\n")

    print("Subtitle downloaded successfully as subtitle.txt")

except Exception as e:
    print("Error:", e)