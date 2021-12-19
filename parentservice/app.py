# Developed by Vincent Claes
# vincent@cteq.eu
# 23/04/2021


from flask import Flask, json, Response, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import json
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/getroute')
def test_route():
    return requests.get('http://childservice/getroute').json()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8889)