import requests

response = requests.post(
    "http://127.0.0.1:5000/chat",
    headers={"Content-Type": "application/json"},
    json={"message": "Hello hotel chatbot!"}
)

print(response.status_code)
print(response.json())
