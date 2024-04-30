from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/api/test')
def test():
    return "API connected and is currently available"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)