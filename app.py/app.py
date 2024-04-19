from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    longitud = int(request.form.get('longitud', 12))
    password = generar_password(longitud)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
