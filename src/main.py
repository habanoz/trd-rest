from flask import Flask, jsonify
from flask import abort
from flask import request
from tinydb import TinyDB

app = Flask(__name__)

@app.route('/trd/stats/add', methods=['POST'])
def add_stats():
    if not request.json or not 'stats' in request.json:
        abort(400)

    db.insert(request.json)

    return jsonify({'stats': 'ok'}), 201

@app.errorhandler(400)
def uflr(e):
    return e, 400


if __name__ == '__main__':
    db = TinyDB('db.json')
    app.run(host='34.74.27.213', port=8080,debug=False)