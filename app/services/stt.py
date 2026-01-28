import requests
import io
import os

def transcribe_audio(audio_bytes: bytes) -> str:
    url = "https://api.elevenlabs.io/v1/speech-to-text"

    files = {
        "file": ("audio.wav", io.BytesIO(audio_bytes), "audio/wav")
    }

    headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY")
    }

    response = requests.post(
        url,
        headers=headers,
        files=files,
        data={
            "model_id": "scribe_v1"  # multilingual STT
        },
        timeout=30
    )

    response.raise_for_status()
    return response.json()["text"]
