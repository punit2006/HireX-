### 📘 `README.md` — HireX: AI-Powered Hiring Assistant

---

## 💼 Project Name: **HireX – Smart AI Hiring Assistant**

**HireX** is an AI-powered Streamlit application designed to generate personalized technical interview questions (with or without answers) based on the candidate's experience and tech stack. It uses **Groq's LLaMA3 model** via API for LLM responses.

---

## 🚀 Features

* 🔍 Generates **10 technical interview questions** based on tech stack + experience.
* 🧠 Offers **detailed, educational solutions** to help candidates learn.
* 💭 Option to generate **thinking-based open-ended questions**.
* 🧾 Form requires all candidate details to proceed (validation included).
* 🎯 Streamlit-based UI with interactive steps.

---

## 🛠️ Tech Stack

* `Streamlit` – UI framework
* `Groq API` – Large Language Model (LLaMA3)
* `pyngrok` – To expose local Streamlit app on Colab
* `dotenv` – To manage environment variables

---

## 📁 File Structure

```bash
.
├── app.py              # Main Streamlit app logic
├── prompts.py          # Prompt engineering for LLM
├── .env                # Contains API key securely
└── README.md           # You're here!
```

---

## ✅ Setup Instructions (Colab)

1. **Install dependencies:**

```python
!pip install -q streamlit pyngrok requests python-dotenv
```

2. **Add your Groq API key**:

```python
import os
api_key = "your_groq_api_key_here"
os.environ["APII"] = api_key
with open(".env", "w") as f:
    f.write(f"APII={api_key}")
```

3. **Run the app and expose via ngrok:**

```python
from pyngrok import ngrok
!pkill ngrok
!streamlit run app.py &>/content/log.txt &
public_url = ngrok.connect(8501)
print("✅ Your app is live at:", public_url)
```

---

## 💡 How to Use

1. Fill out all **7 required fields** in the form.
2. View **10 personalized questions**.
3. Click `Show Practical Solutions` to see **detailed answers**.
4. Optionally click `Show Thinking Questions` for more advanced ones.
5. End conversation once done.

---

## 🔐 API Notes

* You **must** save the Groq API Key in `.env` as `APII`.
* Example:

```
APII=gsk_your_actual_groq_key
```

---

## 👨‍💻 Maintainer

Built by **Punit Jain**
**Project**: B.Tech Final Year - GenAI Hackathon
**Use Case**: AI for Interview Assistant (LLaMA3 on Groq)

---

Let me know if you'd like a downloadable version of this `README.md`.
