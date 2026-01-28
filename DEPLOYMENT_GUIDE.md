# Deployment & Testing Guide

## 🌐 Local Testing with ngrok

Twilio needs a **public URL** to send webhooks. Use ngrok to expose your local server.

### 1. Install ngrok

**Download:**
https://ngrok.com/download

**Or via Chocolatey (Windows):**
```powershell
choco install ngrok
```

### 2. Start Your FastAPI Server
```bash
cd "C:\Users\rohan\OneDrive\Desktop\Twilio Voice Agent"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Start ngrok (in a NEW terminal)
```bash
ngrok http 8000
```

You'll see:
```
Forwarding  https://abc123.ngrok.io -> http://localhost:8000
```

**Copy that https URL!** (e.g., `https://abc123.ngrok.io`)

---

## 📞 Configure Twilio Phone Number

### 1. **Go to Twilio Console**
https://console.twilio.com/us1/develop/phone-numbers/manage/active

### 2. **Select Your Phone Number**
Click on the phone number you want to use

### 3. **Configure Voice Webhooks**

#### **A CALL COMES IN:**
- **Webhook:** `https://abc123.ngrok.io/voice/incoming`
  (Replace `abc123.ngrok.io` with your actual ngrok URL)
- **HTTP Method:** `POST`

#### **RECORDING STATUS CALLBACK:**
- **Webhook:** `https://abc123.ngrok.io/voice/recording`
- **HTTP Method:** `POST`

### 4. **Save Configuration**
Click "Save" at the bottom

---

## 🧪 End-to-End Testing

### Test Flow:

1. **Verify Server Running**
   ```bash
   # Terminal 1: Check FastAPI is running
   curl http://localhost:8000/
   # Should return: {"status":"ok"}
   ```

2. **Verify ngrok Running**
   ```bash
   # Check ngrok dashboard
   # Visit: http://localhost:4040
   # You'll see all webhook requests here
   ```

3. **Call Your Twilio Number**
   - Call the number from any phone
   - You should hear: "Rohan is unavailable. Please state the purpose of your call after the beep."
   - Leave a message (up to 20 seconds)
   - Hang up

4. **Watch the Logs**

   **Terminal 1 (uvicorn):**
   ```
   INFO - Incoming call received
   INFO - Recording received - CallSID: CAxxxx, From: +1234567890
   INFO - Agent processing queued in background
   INFO - Fetching recording: https://...
   INFO - Downloaded 245632 bytes
   INFO - Starting transcription...
   INFO - Transcription complete: Hi this is John...
   INFO - Generating summary...
   INFO - Summary generated: Caller John mentioned...
   INFO - Sending WhatsApp notification...
   INFO - Notification sent successfully
   ```

   **ngrok Dashboard (http://localhost:4040):**
   - Shows 2 POST requests:
     - `/voice/incoming` → 200 OK
     - `/voice/recording` → 204 No Content

5. **Check Your WhatsApp**
   - You should receive a message on `+918007780051`
   - Format:
     ```
     📞 Missed Call
     From: +1234567890
     
     [AI-generated summary of the call]
     ```

---

## 🐛 Troubleshooting

### ❌ No Voice Prompt When Calling

**Possible Causes:**
1. Webhook URL incorrect in Twilio console
2. ngrok not running
3. FastAPI server not running

**Check:**
```bash
# Test webhook manually
curl -X POST https://abc123.ngrok.io/voice/incoming
# Should return XML with <Say> tag
```

### ❌ Recording Not Processing

**Check ngrok dashboard:**
- Did `/voice/recording` webhook get hit?
- What was the status code?

**Check FastAPI logs:**
- Do you see "Recording received" message?
- Are there any errors?

**Common Issues:**
- Recording URL requires authentication (see ISSUES_AND_FIXES.md #6)
- ElevenLabs API quota exceeded
- Groq API key invalid

### ❌ No WhatsApp Message

**Check:**
1. Did you join the sandbox? (See WHATSAPP_SETUP.md)
2. Check Twilio messaging logs: https://console.twilio.com/us1/monitor/logs/sms
3. Check FastAPI logs for "Sending WhatsApp notification..." and any errors

**Test WhatsApp separately:**
```bash
python -c "from twilio.rest import Client; import os; from dotenv import load_dotenv; load_dotenv(); client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN']); msg = client.messages.create(from_='whatsapp:+14155238886', to='whatsapp:+918007780051', body='Test'); print(msg.sid)"
```

### ❌ Transcription Failed

**Check:**
- ElevenLabs API key valid?
- Recording file downloaded successfully? (check byte size in logs)
- Audio format compatible? (Twilio uses .wav)

**Test ElevenLabs separately:**
```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.elevenlabs.io/v1/speech-to-text"
headers = {"xi-api-key": os.getenv("ELEVENLABS_API_KEY")}

# Test with a small audio file
with open("test_audio.wav", "rb") as f:
    files = {"file": ("audio.wav", f, "audio/wav")}
    response = requests.post(url, headers=headers, files=files, data={"model_id": "scribe_v1"})
    print(response.json())
```

### ❌ Summarization Failed

**Check:**
- Groq API key valid?
- Transcript not empty?

**Test Groq separately:**
```python
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))
result = llm.invoke("Summarize: John called about the project deadline")
print(result.content)
```

---

## 📊 Monitoring Dashboard

### ngrok Request Inspector:
http://localhost:4040

**Shows:**
- All webhook requests from Twilio
- Request headers, body
- Response status, headers, body
- Very useful for debugging!

### Twilio Call Logs:
https://console.twilio.com/us1/monitor/logs/calls

**Shows:**
- Every call to your number
- Webhook URLs called
- Webhook responses
- Any errors

### Twilio Messaging Logs:
https://console.twilio.com/us1/monitor/logs/sms

**Shows:**
- WhatsApp message delivery status
- Error codes if failed
- Delivery timestamps

---

## 🚀 Production Deployment

For production (not just testing):

### Option 1: Deploy to Cloud (Recommended)

**Render.com (Free Tier):**
```bash
# Add to repository
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo>
git push

# On Render:
# 1. New Web Service
# 2. Connect GitHub repo
# 3. Build command: pip install -r requirements.txt
# 4. Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
# 5. Add environment variables from .env
```

**Railway.app:**
Similar process, very easy deployment

### Option 2: Keep ngrok Running

**Requirements:**
- Computer must stay on
- ngrok must keep running
- Server must keep running

**Make Stable:**
- Use ngrok paid plan for permanent URL
- Or use ngrok config for custom subdomain

---

## 🎯 Quick Start Commands

### Start Everything:
```bash
# Terminal 1: Start server
cd "C:\Users\rohan\OneDrive\Desktop\Twilio Voice Agent"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Start ngrok
ngrok http 8000

# Browser: Copy ngrok URL and update Twilio webhooks
# Then call your number!
```

### Stop Everything:
```bash
# Terminal 1: Ctrl+C (stop uvicorn)
# Terminal 2: Ctrl+C (stop ngrok)
```

---

## ✅ Pre-Flight Checklist

Before testing:
- [ ] WhatsApp sandbox joined (WHATSAPP_SETUP.md)
- [ ] `.env` file has valid API keys
- [ ] `python-dotenv` installed
- [ ] FastAPI server running
- [ ] ngrok running and URL copied
- [ ] Twilio webhooks configured with ngrok URL
- [ ] Phone ready to make test call

🎉 **Ready to test!** Call your Twilio number and watch the magic happen!

---

## 📞 Support

If issues persist:
1. Check all logs (FastAPI, ngrok, Twilio)
2. Review ISSUES_AND_FIXES.md
3. Test each component separately (WhatsApp, STT, LLM)
4. Verify all API keys are valid
5. Check API quotas/limits

Good luck! 🚀
