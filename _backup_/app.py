from flask import Flask, render_template, request, jsonify
from my_openai import generate_text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

print(os.getenv("OPENAI_SECRET_KEY"))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    question = request.json['question']
    answer = generate_text(question)
    return jsonify(answer=answer)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
