import csv
import difflib
from flask import Flask, request, render_template

app = Flask(__name__)

# Load Q&A from CSV
def load_qa_from_csv(file_path):
    qa_pairs = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question = row['Question'].strip()
            answer = row['Answer'].strip()
            qa_pairs[question] = answer
    return qa_pairs

# Fuzzy match logic
def get_best_match(user_input, questions, cutoff=0.5):
    user_input = user_input.lower()
    lower_questions = [q.lower() for q in questions]
    matches = difflib.get_close_matches(user_input, lower_questions, n=1, cutoff=cutoff)
    if matches:
        index = lower_questions.index(matches[0])
        return questions[index]
    return None

qa_pairs = load_qa_from_csv('maximo_it_helpdesk_qna_full.csv')
questions = list(qa_pairs.keys())

@app.route("/", methods=["GET", "POST"])
def chat():
    user_input = ""
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"].strip()
        matched_question = next((q for q in questions if q.lower() == user_input.lower()), None)

        if matched_question:
            response = qa_pairs[matched_question]
        else:
            match = get_best_match(user_input, questions)
            if match:
                response = f"Did you mean: '<b>{match}</b>'?<br><br><strong>Answer:</strong> {qa_pairs[match]}"
            else:
                response = "Sorry, I couldn’t find anything similar. Please rephrase or contact live support."

    return render_template("chat.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
