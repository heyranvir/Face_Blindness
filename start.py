from flask import Flask, render_template
import os

app = Flask(__name__)

Level = 1

@app.rout('/get_level')
def get_level():
    return render_template('get_level.html')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
