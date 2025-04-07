from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return 'About'

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(f"./static/{path}")
