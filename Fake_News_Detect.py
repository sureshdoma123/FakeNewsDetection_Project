from flask import Flask, render_template, request, url_for
import pandas as pd

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index123.html')

@app.route('/About')
def about():
    return render_template('About_Us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)