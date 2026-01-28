import requests
import logging
from app.services.stt import transcribe_audio
from app.services.summarizer import summarize_text
from app.services.notifier import notify_user

logger = logging.getLogger(__name__)


def fetch_and_transcribe(state):
    """Download recording from Twilio and transcribe it"""
    try:
        logger.info(f"Fetching recording: {state['recording_url']}")
        audio = requests.get(state["recording_url"] + ".wav", timeout=30).content
        logger.info(f"Downloaded {len(audio)} bytes")
        
        logger.info("Starting transcription...")
        state["transcript"] = transcribe_audio(audio)
        logger.info(f"Transcription complete: {state['transcript'][:100]}...")
        return state
    except Exception as e:
        logger.error(f"Error in fetch_and_transcribe: {str(e)}", exc_info=True)
        state["transcript"] = f"[Transcription failed: {str(e)}]"
        return state


def summarize(state):
    """Generate summary from transcript using LLM"""
    try:
        logger.info("Generating summary...")
        state["summary"] = summarize_text(state["transcript"])
        logger.info(f"Summary generated: {state['summary']}")
        return state
    except Exception as e:
        logger.error(f"Error in summarize: {str(e)}", exc_info=True)
        state["summary"] = f"Summary failed: {state['transcript']}"
        return state


def notify(state):
    """Send WhatsApp notification with call summary"""
    try:
        logger.info("Sending WhatsApp notification...")
        notify_user(
            caller=state["caller_number"],
            summary=state["summary"]
        )
        logger.info("Notification sent successfully")
        return state
    except Exception as e:
        logger.error(f"Error in notify: {str(e)}", exc_info=True)
        return state
