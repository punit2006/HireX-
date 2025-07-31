Here's your **interactive README.md** file for the **HireX: Smart AI Hiring Assistant** project. It guides users through setup, usage, and features with clear structure and clickable instructions.

---

## 📘 README.md — HireX: Smart AI Hiring Assistant

````markdown
# 👩‍💼 HireX: Smart AI Hiring Assistant

HireX is an interactive Streamlit app powered by LLMs that helps generate **coding-based interview questions** tailored to a user's experience and tech stack — with solutions, thinking exercises, and more.

---

## 🚀 Features

- ✅ 7 coding interview questions generated from user input
- 🔍 Option to reveal **detailed solutions**
- 💡 Option to attempt 5 **thinking-only questions** (no answers)
- 🎨 Light/Dark theme toggle for better UX
- 📥 Easy form to input candidate details
- 🌐 Deployed using Streamlit + ngrok (for Colab users)

---

## 🖥️ How It Works

1. User fills in a short form (name, experience, tech stack, etc.)
2. App generates **7 fundamental/intermediate coding questions**
3. Then user chooses to:
   - 🔍 View answers with explanations
   - 💡 Practice 5 fresh thinking questions
4. ✅ End the conversation gracefully

---

## 🧑‍💻 Getting Started

### ✅ Prerequisites

Install dependencies:

```bash
pip install streamlit requests python-dotenv pyngrok
````

Set your [Groq API key](https://console.groq.com/) in a `.env` file:

```
APII=your_actual_groq_api_key_here
```

---

### ▶️ Run Locally

```bash
streamlit run app.py
```

---

### 📦 Run on Google Colab

1. Upload the files: `app.py`, `prompts.py`, and `.env`
2. Add this in a Colab cell:

```python
!pip install -q streamlit pyngrok python-dotenv requests
from pyngrok import ngrok

!pkill ngrok  # Kill any existing tunnels
!streamlit run app.py &>/content/log.txt &

public_url = ngrok.connect(8501)
print(\"Your app is live at:\", public_url)
```

---

## 🧠 Example LLM Prompt Used

> Generate 7 coding interview questions that assess fundamental and intermediate programming concepts, ensuring each question focuses on practical problem-solving using core data structures and algorithms.

---

## 📁 Project Structure

```
HireX/
├── app.py            # Main Streamlit app logic
├── prompts.py        # Prompt logic for question generation
├── .env              # API key (not committed to repo)
├── README.md         # You're here!
```

---

## 🎨 Screenshots

| 📋 Interview Questions                                     | 💬 Solutions View                                        | 🧠 Thinking Questions                                      |
| ---------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| ![Q](https://via.placeholder.com/300x200?text=7+Questions) | ![A](https://via.placeholder.com/300x200?text=Solutions) | ![T](https://via.placeholder.com/300x200?text=Thinking+Qs) |

---

## ✨ Future Improvements

* Resume parsing to auto-fill form
* Export questions to PDF
* Email the report to candidate
* Admin dashboard for recruiters

---

## 🤝 Contributing

Pull requests are welcome. Open an issue for feature ideas or bugs.

---

## 📜 License

MIT License. © 2025 HireX Team

```

---

Would you like me to save this README as a `README.md` file and download it for you?
```
