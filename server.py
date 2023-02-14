import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    with open('example_json.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
