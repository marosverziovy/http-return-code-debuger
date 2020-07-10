#!/usr/bin/python
# coding: utf-8

from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return jsonify({"status": "ok", "rc": 200, "errors": []}), 200

@app.route('/<return_code>')
def return_code(return_code):
    reponse = {"rc": return_code}
    return jsonify(reponse), return_code

@app.route('/',)
def index():

    random_number = random.randint(0,99)

    # return 500
    if random_number <= int(os.environ['HTTP_500']):
        random_500 = random.randint(500, 504)
        return {"rc": random_500}, random_500

    # return 400-404
    if random_number <= int(os.environ['HTTP_400']) + int(os.environ['HTTP_500']):
        random_400 = random.randint(400, 404)
        return {"rc": random_400}, random_400

    # return 301-302
    if random_number <= int(os.environ['HTTP_300']) + int(os.environ['HTTP_400']) + int(os.environ['HTTP_500']):
        random_300 = random.randint(301,302)
        return {"rc": random_300}, random_300

    # if not matched any aboved, return 200
    return {"rc": 200}, 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
