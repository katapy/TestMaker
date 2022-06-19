# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('html/index.html')

@app.route("/table")
def table():
    return render_template('html/custamized_table.html')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    