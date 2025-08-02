# 👩‍💼 HireX: Smart Hiring Assistant

HireX is an AI-powered Streamlit app that generates tailored technical interview questions based on a candidate’s tech stack and experience. It's perfect for recruiters, hiring managers, or developers preparing for interviews.

---

## 🔧 Features

- Collects candidate details via a simple form
- Generates 5 technical coding questions
- Provides detailed solutions with code and explanations
- Adds 5 "thinking" (open-ended) questions for deeper evaluation
- Fully automated using the Groq API and LLaMA 3

---

## 🚀 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/hirex-ai.git
cd hirex-ai
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Setup environment variables**

Rename `.env.template` to `.env` and add your Groq API key:

```env
APII=your_groq_api_key_here
```

---

## 🧠 Usage

To run the app locally:

```bash
streamlit run app.py
```

Once started, open the app in your browser at `http://localhost:8501`

To expose it publicly using ngrok (optional, for testing):

```python
from pyngrok import ngrok
public_url = ngrok.connect(8501)
print("Your app is live at:", public_url)
```

---

## 🗂 Project Structure

```
.
├── app.py
├── prompts.py
├── requirements.txt
├── Procfile
├── .env.template
└── README.md
```

---

## 🔒 Environment Variables

| Key  | Description       |
| ---- | ----------------- |
| APII | Your Groq API key |

---

## 👨‍💻 Built With

* [Streamlit](https://streamlit.io/)
* [Groq API](https://console.groq.com/)
* [LLaMA 3](https://llama.meta.com/)
* [Python](https://www.python.org/)

---

## ▶️ Try it in Google Colab

Want to run HireX directly in your browser?

https://colab.research.google.com/drive/12_S3D5CH6cBSphN746thNs5yPzK2dkq8?usp=sharing
