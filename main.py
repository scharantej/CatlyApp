
# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/cats')
def cats():
    return render_template('cats.html')

if __name__ == '__main__':
    app.run(debug=True)
