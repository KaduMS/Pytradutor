from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text_input = request.form['text_input']
    translator = Translator()
    translated = translator.translate(text_input, src='en', dest='pt')
    return render_template('index.html', translated=translated.text)

if __name__ == '__main__':
    app.run()