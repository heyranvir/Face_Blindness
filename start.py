from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)


name_file = open("static/Names.txt","r")
content_of_name_file = name_file.readlines()
Names = [n.replace("\n", "") for n in content_of_name_file]

Levels = {
    1 : 10,
    2 : 25,
    3 : 50,
    4 : 100,
    5 : 200
}

Level = 1

@app.route('/get_level')
def get_level():
    return render_template('get_level.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/practice/<int:level>')
def practice(level):
    l = Levels[level]
    names = Names[:l]
    data = {"names" : names}
    return render_template('practice.html',data = data)

@app.route('/test/<int:level>')
def test(level):
    l = Levels[level]
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
