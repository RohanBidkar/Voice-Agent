# WhatsApp Setup Instructions

## ⚠️ IMPORTANT: WhatsApp Sandbox Activation

Your code uses Twilio's **WhatsApp Sandbox**. This requires one-time setup!

## Steps to Activate:

### 1. **Open Twilio Console**
Go to: https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

### 2. **Find Your Sandbox Name**
You'll see something like:
```
Send this message to your sandbox number:
join <your-sandbox-name>

From: +918007780051
To: +14155238886
```

### 3. **Send the Activation Message**
1. Open WhatsApp on your phone
2. Start a new chat with: **+1 415 523 8886**
3. Send the message: `join <your-sandbox-name>`
   (Replace `<your-sandbox-name>` with the actual name shown in console)

### 4. **Wait for Confirmation**
You should receive a reply from Twilio saying:
```
✅ Joined <your-sandbox-name>
Your Sandbox is ready!
```

---

## Testing WhatsApp Separately

Before testing the full voice agent, test WhatsApp messaging:

### Test Script:
```python
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.environ["TWILIO_ACCOUNT_SID"],
    os.environ["TWILIO_AUTH_TOKEN"]
)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    to="whatsapp:+918007780051",
    body="🧪 Test Message from Twilio Voice Agent Setup"
)

print(f"Message sent! SID: {message.sid}")
print(f"Status: {message.status}")
```

### Run Test:
```bash
cd "C:\Users\rohan\OneDrive\Desktop\Twilio Voice Agent"
python -c "from twilio.rest import Client; import os; from dotenv import load_dotenv; load_dotenv(); client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN']); msg = client.messages.create(from_='whatsapp:+14155238886', to='whatsapp:+918007780051', body='Test from setup'); print(f'Sent: {msg.sid}')"
```

---

## Common Issues

### ❌ Error: "To number is not a valid WhatsApp number"
**Solution:** You haven't joined the sandbox. Complete steps 1-4 above.

### ❌ Error: "21211: Invalid 'To' Phone Number"
**Solution:** Check the phone number format in `notifier.py`:
- Must include `whatsapp:` prefix
- Must include country code
- Format: `whatsapp:+918007780051`

### ❌ Error: "21608: The 'From' number... is not a valid WhatsApp enabled number"
**Solution:** You're using the wrong sandbox number. Use: `whatsapp:+14155238886`

---

## Checking Message Status

### In Twilio Console:
1. Go to: https://console.twilio.com/us1/monitor/logs/sms
2. Filter by "WhatsApp"
3. Look for your messages
4. Check status: `delivered`, `failed`, `undelivered`, etc.

### Programmatically:
```python
message = client.messages.get('SM...')  # Your message SID
print(f"Status: {message.status}")
print(f"Error code: {message.error_code}")
print(f"Error message: {message.error_message}")
```

---

## Upgrading to Production WhatsApp

When ready for production (not sandbox):

1. **Apply for WhatsApp Business Account**
   - Go to Twilio Console → Messaging → Senders → WhatsApp senders
   - Click "Create new WhatsApp Sender"
   - Submit business verification
   - Wait 3-7 days for approval

2. **Update Code**
   ```python
   # Change from sandbox:
   from_="whatsapp:+14155238886"
   
   # To your approved number:
   from_="whatsapp:+1234567890"  # Your Twilio WhatsApp number
   ```

3. **No More Join Required**
   - Users don't need to "join" anymore
   - Works like regular WhatsApp messaging

---

## Quick Test Checklist

- [ ] Joined WhatsApp sandbox (sent `join <name>`)
- [ ] Received confirmation from Twilio
- [ ] Ran test message script
- [ ] Received test message on phone
- [ ] Checked Twilio logs show "delivered"

✅ If all checked, your WhatsApp setup is ready!

---

## Next: Voice Agent Testing

Once WhatsApp works, proceed to test the full voice agent flow:
1. Set up ngrok (see main README)
2. Configure Twilio phone number webhooks
3. Call your Twilio number
4. Leave a message
5. Check logs and wait for WhatsApp summary

Good luck! 🚀
