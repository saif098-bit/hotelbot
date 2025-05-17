from flask import Flask, render_template, request
import sqlite3
import difflib
import string
from datetime import datetime
import requests
import json
import re

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3:mini"

def clean_text(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation))

def log_unanswered_question(user_input):
    with open("unanswered_queries.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - {user_input}\n")

def call_ollama_api(user_input):
    headers = {"Content-Type": "application/json"}

    system_instruction = (
        "You are a hotel assistant for The Velvet Orchid Hotel located in Abbottabad. "
        "Provide clear, concise answers about bookings, pricing, check-in/check-out, services, amenities, rules, or facilities. "
        "Avoid personal opinions. Never mention you're an AI. Never fabricate details. "
        "If a question is unrelated to hotel services, politely redirect the user back. "
        "Keep your tone professional and helpful. Limit your answer to 4 to 5 lines maximum.\n\n"
        f"User: {user_input}\nAssistant:"
    )

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": system_instruction,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        reply = data.get("response", "Sorry, no response from model.")
    except json.JSONDecodeError:
        try:
            response = requests.post(OLLAMA_API_URL, json=payload, headers=headers, stream=True)
            reply = ""
            for line in response.iter_lines():
                if line:
                    json_line = json.loads(line.decode('utf-8'))
                    reply += json_line.get("response", "")
        except Exception as e:
            print(f"Stream decoding error: {e}")
            return "Sorry, I'm having trouble answering right now."
    except Exception as e:
        print(f"Ollama API error: {e}")
        return "Sorry, I'm having trouble answering right now."

    reply = re.sub(r"(User:|Assistant:)", "", reply, flags=re.IGNORECASE).strip()
    reply = re.sub(r"(?i)(what are your amenities\?|can you tell me about your .+?\?)", "", reply).strip()

    if reply.lower().startswith("sorry"):
        log_unanswered_question(user_input)

    return reply

def get_answer(user_input):
    cleaned_input = clean_text(user_input)

    try:
        with sqlite3.connect("hostel_chatbot.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT question, answer FROM FAQ")
            faq_list = cursor.fetchall()
    except Exception as e:
        print(f"Database error: {e}")
        faq_list = []

    questions_clean = [clean_text(q) for q, _ in faq_list]
    matches = difflib.get_close_matches(cleaned_input, questions_clean, n=1, cutoff=0.6)

    if matches:
        matched_question = matches[0]
        for q, a in faq_list:
            if clean_text(q) == matched_question:
                return a

    return call_ollama_api(user_input)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = get_answer(user_input)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
