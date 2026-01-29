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

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            raise ValueError(
                "ElevenLabs API key is invalid or missing. "
                "Please check ELEVENLABS_API_KEY environment variable."
            ) from e
        raise
    
    return response.json()["text"]
