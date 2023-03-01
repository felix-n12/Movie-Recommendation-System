# importing class Flask,render_template from flask module
from flask import Flask, render_template, url_for
# instastiate a Flask object to give a unique name by using __name__
app=Flask(__name__)
# use a decorator an make a REQUEST to the endpoint inside the brackets
@app.route('/')
def home():
    return render_template('index.html')
app.run(port = 5000)
