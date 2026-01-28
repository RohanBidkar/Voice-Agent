from fastapi import FastAPI
from app.twilio_routes import router as twilio_router
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI Voicemail Agent",
    version="1.0.0"
)

app.include_router(twilio_router, prefix="/voice")

@app.get("/")
def health():
    return {"status": "ok"}
