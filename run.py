from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(dict(request.headers)), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)