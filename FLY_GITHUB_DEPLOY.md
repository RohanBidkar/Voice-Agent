# 🚀 Deploy to Fly.io via GitHub Actions

## Step 1: Sign Up for Fly.io

1. Go to: https://fly.io/app/sign-up
2. Sign up with your email or GitHub
3. Verify your email

---

## Step 2: Install Fly CLI (One-time setup)

**Windows (PowerShell - Run as Administrator):**
```powershell
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

**After installation:**
- Close and reopen your terminal
- Verify: `fly version`

---

## Step 3: Login and Create App

```bash
# Login to Fly.io
fly auth login

# Navigate to your project
cd "C:\Users\rohan\OneDrive\Desktop\Twilio Voice Agent"

# Launch the app (creates it on Fly.io)
fly launch --no-deploy

# Answer the prompts:
# - Choose app name (or press Enter for auto-generated)
# - Choose region: sin (Singapore) or closest to you
# - Would you like to set up a Postgresql database? NO
# - Would you like to set up an Upstash Redis database? NO
# - Would you like to deploy now? NO
```

---

## Step 4: Set Secrets on Fly.io

```bash
fly secrets set GROQ_API_KEY="your-groq-key-from-env-file"
fly secrets set TWILIO_ACCOUNT_SID="your-twilio-sid-from-env-file"
fly secrets set TWILIO_AUTH_TOKEN="your-twilio-token-from-env-file"
fly secrets set ELEVENLABS_API_KEY="your-elevenlabs-key-from-env-file"
```

**Get these values from your `.env` file!**

---

## Step 5: Get Fly.io API Token for GitHub

```bash
# Generate a token
fly tokens create deploy

# Copy the token that's displayed
```

---

## Step 6: Add Token to GitHub Secrets

1. Go to your repository on GitHub:
   https://github.com/RohanBidkar/Voice-Agent

2. Click **Settings** → **Secrets and variables** → **Actions**

3. Click **New repository secret**

4. Add:
   - **Name**: `FLY_API_TOKEN`
   - **Secret**: Paste the token from Step 5

5. Click **Add secret**

---

## Step 7: Push and Auto-Deploy! 🚀

```bash
git add .
git commit -m "Add Fly.io deployment workflow"
git push
```

**That's it!** GitHub Actions will automatically:
- Detect the push to main
- Deploy to Fly.io
- Your app will be live!

---

## 📊 Monitor Deployment

**Watch GitHub Actions:**
- Go to: https://github.com/RohanBidkar/Voice-Agent/actions
- You'll see the deployment running

**Check Fly.io Logs:**
```bash
fly logs
```

**Get Your App URL:**
```bash
fly status
```

Your app will be at: `https://your-app-name.fly.dev`

---

## 🔄 Future Updates

Just commit and push - auto-deployment happens every time!

```bash
git add .
git commit -m "Your changes"
git push
```

GitHub Actions → Fly.io → Live! ✨

---

## ✅ Deployment Checklist

- [ ] Signed up on Fly.io
- [ ] Installed Fly CLI locally
- [ ] Ran `fly auth login`
- [ ] Ran `fly launch --no-deploy`
- [ ] Set all 4 secrets with `fly secrets set`
- [ ] Generated deploy token with `fly tokens create deploy`
- [ ] Added `FLY_API_TOKEN` to GitHub Secrets
- [ ] Committed and pushed workflow file
- [ ] Checked GitHub Actions - deployment running
- [ ] Got app URL from `fly status`
- [ ] Updated Twilio webhooks
- [ ] Made test call! 📞

---

## 🎯 Advantages

✅ **Auto-deploy** on every git push
✅ **Free tier** available
✅ **Global CDN**
✅ **Auto-scaling**
✅ **Easy rollbacks**
✅ **Built-in monitoring**

---

**Your workflow file is ready!** Just follow the steps above to set up Fly.io and GitHub Actions. 🚀
