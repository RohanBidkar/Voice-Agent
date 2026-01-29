# Railway Deployment Guide

## Quick Deploy to Railway

### Prerequisites
1. Railway account (sign up at [railway.app](https://railway.app))
2. GitHub repository with your code pushed
3. Environment variables ready

### Deployment Steps

#### Option 1: Deploy from GitHub (Recommended)
1. **Connect GitHub Repository**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your GitHub
   - Select this repository

2. **Configure Environment Variables**
   Railway will automatically detect the Dockerfile. Add these environment variables:
   - `GROQ_API_KEY` - Your Groq API key
   - `TWILIO_ACCOUNT_SID` - Your Twilio Account SID
   - `TWILIO_AUTH_TOKEN` - Your Twilio Auth Token
   - `TWILIO_PHONE_NUMBER` - Your Twilio phone number
   - Any other environment variables from your `.env` file

3. **Deploy**
   - Railway will automatically build and deploy using your Dockerfile
   - Wait for deployment to complete
   - Copy your public URL from Railway dashboard

4. **Update Twilio Webhook**
   - Go to Twilio Console
   - Update your phone number's webhook URL to: `https://your-railway-url.railway.app/voice`

#### Option 2: Deploy with Railway CLI
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Add environment variables
railway variables set GROQ_API_KEY=your_groq_api_key
railway variables set TWILIO_ACCOUNT_SID=your_twilio_sid
railway variables set TWILIO_AUTH_TOKEN=your_twilio_token
railway variables set TWILIO_PHONE_NUMBER=your_twilio_number

# Deploy
railway up
```

### Post-Deployment

1. **Get Your Railway URL**
   - Find it in the Railway dashboard under "Settings" → "Domains"
   - Format: `https://your-app-name.railway.app`

2. **Update Twilio Webhook**
   - Voice URL: `https://your-railway-url.railway.app/voice`
   - Status Callback URL (optional): `https://your-railway-url.railway.app/status`

3. **Test Your Setup**
   - Call your Twilio number
   - Check Railway logs for any errors

### Monitoring

- **View Logs**: Railway Dashboard → Your Project → Logs
- **Metrics**: Railway Dashboard → Your Project → Metrics
- **Environment Variables**: Railway Dashboard → Your Project → Variables

### Troubleshooting

**Deployment Fails:**
- Check Railway build logs for errors
- Ensure all dependencies are in `requirements.txt`
- Verify Dockerfile syntax

**Voice Agent Not Responding:**
- Verify Twilio webhook is set correctly
- Check Railway logs for incoming requests
- Ensure environment variables are set correctly

**Cold Starts:**
- Railway free tier may have cold starts
- Consider upgrading to a paid plan for better performance

### Cost

- Railway offers $5 free credits per month
- After free credits, you pay for usage
- Typical voice agent usage is minimal for low traffic

### Auto-Deployment

Once connected to GitHub, Railway will automatically redeploy on every push to your main branch!
