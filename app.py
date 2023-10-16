from flask import Flask, render_template, request, jsonify
from my_openai import generate_text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

print(os.getenv("OPENAI_SECRET_KEY"))
app = Flask(__name__)

@app.route('/base')
def base():
    return render_template('base.html')
    


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        question = data['question']
        response_text = generate_text(question, 'eingangsbereich')
        return jsonify({'answer': response_text})
    else:
        return render_template('index.html')



@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/aktuelles')
def aktuelles():
    return render_template('aktuelles.html')

@app.route('/hellsehen', methods=['GET', 'POST'])
def hellsehen():
    if request.method == 'POST':
        question = request.json['question']
        answer = generate_text(question, 'hellsehen')
        return jsonify({'answer': answer})  # Verwenden Sie hier {'answer': answer}
    else:
        return render_template('hellsehen.html')


@app.route('/horoskop', methods=['GET', 'POST'])
def horoskop():
    if request.method == 'POST':
        question = request.json['question']
        answer = generate_text(question, 'horoskop')
        return jsonify({'answer': answer})
    else:
        return render_template('horoskop.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/psychologie', methods=['GET', 'POST'])
def psychologie():
    if request.method == 'POST':
        question = request.json['question']
        answer = generate_text(question, 'psychologie')
        return jsonify({'answer': answer})
    else:
        return render_template('psychologie.html')

@app.route('/traumdeutung', methods=['GET', 'POST'])
def traumdeutung():
    if request.method == 'POST':
        question = request.json['question']
        answer = generate_text(question, 'traumdeutung')
        return jsonify({'answer': answer})
    else:
        return render_template('traumdeutung.html')

if __name__ == '__main__':
    #app.run(port=5000, debug=True)   #Start auf localhost
    app.run(host='0.0.0.0', port=5000, debug=True) #Start im Wlan
