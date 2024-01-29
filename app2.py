from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is second app! </h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
