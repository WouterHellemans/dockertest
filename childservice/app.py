# Developed by Vincent Claes
# vincent@cteq.eu
# 23/04/2021

import json
from flask import Flask, json, Response, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/getroute', methods = ['GET'])
def test_route():
    print("it works")
    return jsonify("Hello World!")
    
@app.route('/testroute')
def hello():
    return "test!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)