from twilio.rest import Client
import os
import logging

logger = logging.getLogger(__name__)

def notify_user(caller, summary):
    """Send WhatsApp notification with call summary"""
    try:
        # Initialize client with environment variables
        client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
        
        message = client.messages.create(
            from_="whatsapp:+14155238886",  # Twilio sandbox
            to="whatsapp:+918007780051",   # YOUR number
            body=f"📞 Missed Call\nFrom: {caller}\n\n{summary}"
        )
        logger.info(f"WhatsApp message sent successfully. SID: {message.sid}, Status: {message.status}")
        return message
    except Exception as e:
        logger.error(f"Failed to send WhatsApp message: {str(e)}", exc_info=True)
        raise
