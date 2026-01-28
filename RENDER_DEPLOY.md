# 🚀 Deploy to Render from GitHub (Easiest Method!)

## Step 1: Push to GitHub

1. **Create a new repository on GitHub:**
   - Go to: https://github.com/new
   - Repository name: `twilio-voice-agent` (or whatever you prefer)
   - **Make it PRIVATE** (you have API keys in your commits)
   - Don't initialize with README, .gitignore, or license
   - Click "Create repository"

2. **Push your code:**
   ```bash
   cd "C:\Users\rohan\OneDrive\Desktop\Twilio Voice Agent"
   git remote add origin https://github.com/YOUR_USERNAME/twilio-voice-agent.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Deploy on Render

1. **Sign up/Login to Render:**
   - Go to: https://render.com/
   - Sign up with GitHub (easiest)

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub account (if not already)
   - Select your `twilio-voice-agent` repository
   - Click "Connect"

3. **Configure the service:**
   
   **Name:** `twilio-voice-agent` (or your choice)
   
   **Region:** `Singapore` (or closest to you)
   
   **Branch:** `main`
   
   **Root Directory:** (leave blank)
   
   **Runtime:** `Python 3`
   
   **Build Command:**
   ```
   pip install -r requirements.txt
   ```
   
   **Start Command:**
   ```
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
   
   **Instance Type:** `Free`

4. **Add Environment Variables:**
   
   Click "Advanced" → "Add Environment Variable" and add these **from your `.env` file**:
   
   | Key | Value |
   |-----|-------|
   | `GROQ_API_KEY` | Get from your `.env` file |
   | `TWILIO_ACCOUNT_SID` | Get from your `.env` file |
   | `TWILIO_AUTH_TOKEN` | Get from your `.env` file |
   | `ELEVENLABS_API_KEY` | Get from your `.env` file |

5. **Click "Create Web Service"**

   Render will:
   - Build your app (takes 2-3 minutes)
   - Deploy it
   - Give you a URL like: `https://twilio-voice-agent-xxxx.onrender.com`

---

## Step 3: Configure Twilio Webhooks

Once your app is deployed and shows "Live" status:

1. Copy your Render URL (e.g., `https://twilio-voice-agent-xxxx.onrender.com`)

2. Go to Twilio Console:
   https://console.twilio.com/us1/develop/phone-numbers/manage/active

3. Click your phone number

4. Set webhooks:
   - **A CALL COMES IN:**
     - URL: `https://your-render-url.onrender.com/voice/incoming`
     - Method: `POST`
   
   - **Primary handler fails:** (optional but recommended)
     - URL: `https://your-render-url.onrender.com/voice/recording`
     - Method: `POST`

5. **Save**

---

## Step 4: Test! 📞

1. Call your Twilio number
2. Leave a message after the beep
3. Check Render logs: Dashboard → Logs
4. Check your WhatsApp for the summary!

---

## 🎯 Important Notes

### Free Tier Limits:
- ✅ 750 hours/month (plenty for voice agent)
- ⚠️ **Auto-sleeps after 15 min of inactivity**
- ⚠️ **Takes ~30 seconds to wake up on first call**

### First Call Behavior:
- First call after sleep: Twilio might timeout
- Call again immediately: Works perfectly!
- Or upgrade to paid ($7/month) for always-on

### Keeping it Awake (Optional):
If you want instant response, upgrade to paid tier OR use a service like:
- https://uptimerobot.com/ (free) to ping your app every 5 minutes

---

## 🔄 Updating Your App

After you make code changes:

```bash
git add .
git commit -m "Update: description of changes"
git push
```

Render will **auto-deploy** the new version!

---

## 📊 Monitoring

**View Logs:**
- Dashboard → Your Service → Logs

**View Metrics:**
- Dashboard → Your Service → Metrics

**Check Status:**
- Dashboard → Your Service (should say "Live")

---

## ✅ Quick Checklist

- [ ] Created GitHub repository (PRIVATE!)
- [ ] Pushed code to GitHub
- [ ] Signed up on Render
- [ ] Created Web Service from GitHub repo
- [ ] Added all 4 environment variables
- [ ] Deployment succeeded ("Live" status)
- [ ] Copied Render URL
- [ ] Updated Twilio webhooks
- [ ] Made test call
- [ ] Received WhatsApp summary! 🎉

---

## 🎊 Advantages of This Approach

✅ **Free tier** available
✅ **Auto-deploy** from GitHub
✅ **Easy to update** (just git push)
✅ **Built-in logging** and monitoring
✅ **Automatic HTTPS**
✅ **No CLI tools** needed
✅ **Beautiful dashboard**

---

**That's it! Your voice agent will be live in ~5 minutes!** 🚀
