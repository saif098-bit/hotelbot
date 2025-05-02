from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Get bot response function
def get_answer(user_input):
    conn = sqlite3.connect("hostel_chatbot.db")
    cursor = conn.cursor()
    words = user_input.lower().split()

    for word in words:
        cursor.execute("SELECT answer FROM FAQ WHERE question LIKE ?", (f"%{word}%",))
        result = cursor.fetchone()
        if result:
            conn.close()
            return result[0]

    conn.close()
    return "Sorry, I couldn't find an answer."

# Home route
@app.route('/')
def home():
    return render_template('chat.html')  # This will look for 'chat.html' in the templates folder

# Get bot response route
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = get_answer(user_input)
    return response

if __name__ == "__main__":  # This starts the app
    app.run(host='0.0.0.0', port=5050, debug=True)

