# 🛠️ Maximo Helpdesk Assistant (Rule-based Chatbot)

The **Maximo Helpdesk Assistant** is a rule-based chatbot designed to provide support for users working with IBM Maximo. It handles frequently asked questions using a simple CSV-driven Q&A approach and fuzzy string matching.

---

## 📌 Features

- Rule-based responses powered by a question-answer CSV file
- Fuzzy matching using Python's `difflib` to handle variations in user input
- Flask-based web interface for user-friendly interaction
- Easy to extend and maintain using a simple `.csv` knowledge base

---

## 🧠 Example Use Cases

- Troubleshooting Maximo login issues
- Guidance on raising support tickets
- Understanding user roles and responsibilities
- Common errors and their resolutions
- Step-by-step instructions for using features

---

## 📁 Project Structure

```
01 Maximo Helpdesk Assistant/
├── mhaenv/                    # (Optional) Virtual environment
├── static/
│   └── style.css             # Custom CSS for chatbot UI
├── templates/
│   └── chat.html             # HTML UI template for chatbot
├── app.py                    # Flask web interface with fuzzy logic
├── maximo_it_helpdesk_qna_full.csv   # Q&A knowledge base
└── readMe.md                 # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
cd /path/to/your/projects
mkdir "01 Maximo Helpdesk Assistant"
cd "01 Maximo Helpdesk Assistant"
```

(Manually place your files if not using Git)

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv mhaenv
source mhaenv/bin/activate  # On Windows: mhaenv\Scripts\activate
```

### 3. Install Flask

```bash
pip install Flask
```

### 4. Run the Flask App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🔍 How It Works

- The chatbot reads a CSV file (`maximo_it_helpdesk_qna_full.csv`) containing questions and answers.
- When a user enters a query:
  - If it **matches exactly** (case-insensitive), the bot responds with the correct answer.
  - If not, it uses `difflib` to **fuzzily match** the closest question and asks for confirmation.
  - If no match is found, the bot replies with a fallback message.

---

## 📑 CSV Format (maximo\_it\_helpdesk\_qna\_full.csv)

```csv
Question,Answer
How to reset my Maximo password?,Go to login screen and click on 'Forgot Password'.
Maximo is down. What should I do?,Immediately report to IT Operations and raise a P1 support ticket.
...
```

---

## 🚀 Future Enhancements

- Integration with live support chat APIs
- Multi-turn conversation support
- Admin dashboard to manage FAQs
- NLP-powered suggestions

---

## ✅ Status

This project is complete for CLI and Flask web interface using rule-based Q&A logic. Feedback and extensions are welcome!

