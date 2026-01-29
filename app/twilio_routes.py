from fastapi import APIRouter, Request, BackgroundTasks
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse
from app.agent.graph import run_agent
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/incoming")
async def incoming_call():
    """Handle incoming call and instruct Twilio to record the message"""
    logger.info("Incoming call received")
    response = VoiceResponse()
    response.say(
        "I am Rohan's assistant he's unavailable. बीप के बाद मुज़हे कॉल करने की वजह बताये",
        voice="alice"
    )
    response.record(
        max_length=20,
        play_beep=True,
        action="/voice/recording"
    )
    return Response(content=str(response), media_type="application/xml")


@router.post("/recording")
async def recording_callback(request: Request, background_tasks: BackgroundTasks):
    """Handle recording callback and process in background"""
    try:
        form = await request.form()

        recording_url = form.get("RecordingUrl")
        caller = form.get("From")
        call_sid = form.get("CallSid")

        logger.info(f"Recording received - CallSID: {call_sid}, From: {caller}, URL: {recording_url}")

        # Run LangGraph in background to avoid blocking Twilio's webhook
        background_tasks.add_task(
            run_agent,
            call_sid=call_sid,
            caller_number=caller,
            recording_url=recording_url
        )

        logger.info("Agent processing queued in background")
        return Response(status_code=204)
    
    except Exception as e:
        logger.error(f"Error in recording callback: {str(e)}", exc_info=True)
        return Response(status_code=500)
