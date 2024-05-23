import flask
from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def start():
    return render_template('opening.html')
@app.route('/read_more', methods=['GET', 'POST'])
def read_more_func():
    return render_template('index.html')
@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template('feedback.html')
@app.route('/startup', methods=['GET', 'POST'])
def startup():
    return render_template('opening.html')
