from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response.get('choices', [{}])[0].get('message', {}).get('content', "I'm not sure how to respond.")
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
