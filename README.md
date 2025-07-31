# HireX-
HireX is an AI-powered hiring assistant app built with Python and Streamlit. It creates customized technical interview questions and solutions based on your skills, helping users prepare for and evaluate interviews quickly and easily. 

# HireX: Smart AI Hiring Assistant

**HireX** is an AI-powered hiring assistant web app built using Python, Streamlit, and LLM APIs. It generates customized technical interview questions and solutions based on user input, helping candidates prepare and recruiters assess skills.

## Features

- 🔑 Secure API key management using `.env` file  
- ✏️ User registration and information form  
- ✨ Automatic generation of technical and coding interview questions  
- 📝 Solutions and explanations to coding questions  
- 💡 Additional thinking/interview questions on demand  
- 🌐 Easy-to-use Streamlit web UI  
- 🚀 Quick sharing with ngrok public URL

## Quick Start

### 1. Install Requirements

```bash
pip install streamlit pyngrok requests python-dotenv
```

### 2. Set Environment Variables

Set your **Groq API key** and (optionally) ngrok auth token in the code:
```python
api_key = "YOUR_GROQ_API_KEY"
ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")
```
- By default, these are automatically set in `.env` by the script.

### 3. Run the App

Run the Python script—on Colab or locally:

```bash
python pgagi_project-2.py
```

This script:
- Generates prompt and app code files.
- Installs dependencies.
- Starts Streamlit as a background process.
- Launches a public URL via ngrok.

The URL will output as:
```
✅ Your chatbot is live at: https://xxxx.ngrok.io
```

## How It Works

1. **Landing Page:** Introduction and “Start” button.
2. **Information Form:** User enters their details (name, contact, experience, tech stack, etc.).
3. **Question Generation:** 
    - 5 technical questions generated for user's stack & experience.
    - Optionally, view solutions and extra “thinking” questions.
4. **Close:** End conversation, show thank-you message.

**All logic is handled via the `app.py` file and prompt templates in `prompts.py`, auto-created by the script.**

## File Structure

```
- pgagi_project-2.py      # Main setup & runner script
- app.py                  # Streamlit app (auto-generated)
- prompts.py              # Prompt templates (auto-generated)
- .env                    # Stores API secret (auto-generated)
```

## Notes

- **API Keys:** Never share sensitive API keys. Use environment variables or `.env` file for production.
- The Streamlit app uses the Groq LLM API with the `llama3-8b-8192` model.
- Ngrok is used to make your local app accessible on the web.

## License

For educational/demo use. Replace with your own license as needed.

#### Enjoy using **HireX** to revolutionize technical interviews!

Let me know if you want a Markdown code version suitable for direct copy-paste!

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/87200246/d649a7af-ec04-4ea8-bb4c-f49f614cde8a/pgagi_project-2.py
