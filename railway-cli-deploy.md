# Railway CLI Deployment Fix

## The "workspaceId" Error Fix

The error "You must specify a workspaceId to create a project" occurs when Railway CLI doesn't have proper context.

### Solution: Use `railway link` instead of `railway init`

```bash
# 1. Login to Railway (if not already logged in)
railway login

# 2. Create a new project on Railway Dashboard FIRST
# - Go to https://railway.app
# - Click "New Project" → "Empty Project"
# - Give it a name (e.g., "twilio-voice-agent")

# 3. Link your local project to the Railway project
railway link

# 4. Select the project you just created from the list

# 5. Add environment variables
railway variables set GROQ_API_KEY=your_groq_api_key
railway variables set TWILIO_ACCOUNT_SID=your_twilio_sid
railway variables set TWILIO_AUTH_TOKEN=your_twilio_token
railway variables set TWILIO_PHONE_NUMBER=your_twilio_number

# 6. Deploy
railway up
```

## OR: Simpler CLI Approach

If you have multiple workspaces, you need to specify the workspace:

```bash
# List your workspaces
railway whoami

# You'll see your workspaces listed
# Then create project with workspace context:
railway project create --name twilio-voice-agent

# Then continue with variables and deployment
railway variables set GROQ_API_KEY=your_key
railway up
```

## Recommended: Use Dashboard Instead

The web dashboard is much simpler and less error-prone:
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variables in the UI
5. Done! ✅
