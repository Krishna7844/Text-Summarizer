from flask import Flask, request, jsonify,render_template
from google import genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key="AIzaSyAs8EMft6ie2aAsFuZIqghjQdJkIzQ1RBo")
chat = client.chats.create(
    model="gemini-2.5-flash"
    )

def text_summarization(role, message):
    chat.send_message(role)
    response = chat.send_message(message)
    return response.text

@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/chat", methods = ["POST"])
def chat_api():
    data = request.get_json()
    
    role = "Summarize the given input text and mark important lines in bullet points"
    message = data['message']

    response_text = text_summarization(role, message)
    return jsonify({
        "role": role,
        "message": message,
        "response": response_text
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)