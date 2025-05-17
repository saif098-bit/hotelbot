from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

class OllamaLLM:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "mistral"  # or llama3, codellama, etc.

    def send_prompt(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(self.url, json=payload)
        if response.ok:
            return response.json()['response']
        else:
            return "Error: " + response.text

llm = OllamaLLM()

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    reply = llm.send_prompt(user_message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
