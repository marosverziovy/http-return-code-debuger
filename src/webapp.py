#!/usr/bin/python
# coding: utf-8

from flask import Flask
import os
import random

app = Flask(__name__)

@app.route('/')
def index():

    random_number = random.randint(0,99)

    # return 500
    if random_number <= int(os.environ['HTTP_500']):
        random_500 = random.randint(500, 504)
        return "500", random_500
        # return str(random_500), random_500

    # return 400-404
    if random_number <= int(os.environ['HTTP_400']) + int(os.environ['HTTP_500']):
        random_400 = random.randint(400, 404)
        return "400", random_400
        # return str(random_400), random_400

    # return 301-302
    if random_number <= int(os.environ['HTTP_300']) + int(os.environ['HTTP_400']) + int(os.environ['HTTP_500']):
        random_300 = random.randint(301,302)
        return "300", random_300
        # return str(random_300), random_300

    # if not matched any aboved, return 200
    return "200", 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
