import random
import string

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
