from google import genai

client = genai.Client(api_key="AIzaSyAs8EMft6ie2aAsFuZIqghjQdJkIzQ1RBo")
chat = client.chats.create(
    model="gemini-2.5-flash"
    )

def text_summarization(role, message):
# role = "From now on, you are UltraSpark, a superhero with tech powers and a charming sense of humor. Act accordingly in all responses."

    chat.send_message(role)
    response = chat.send_message(message)
    return response.text

role = input("Enter the role you want to assign: ") 
message = input("enter a message: ")
print(text_summarization(role, message))



# from flask import Flask, request, jsonify,render_template
# from google import genai

# app = Flask(__name__)

# client = genai.Client(api_key="AIzaSyAs8EMft6ie2aAsFuZIqghjQdJkIzQ1RBo")
# chat = client.chats.create(
#     model="gemini-2.5-flash"
#     )

# def text_summarization(role, message):
#     chat.send_message(role)
#     response = chat.send_message(message)
#     return response.text

# @app.route("/")
# def index():
#     return render_template("/index.html")


# @app.route("/chat", methods = ["POST"])
# def chat_api():
#     data = request.get_json()
    
#     role = "Summarize the given input text and mark important lines in bullet points"
#     message = data['message']

#     response_text = text_summarization(role, message)
#     return jsonify({
#         "role": role,
#         "message": message,
#         "response": response_text
#     })


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)