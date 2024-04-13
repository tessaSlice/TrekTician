from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # more stuff here
    return "<p>Hello, world!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
