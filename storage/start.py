# -*- coding: utf-8 -*-

"""
@date: 2020/1/5
@creator: he.xu
@description: 
"""

import os

import flask
from flask import render_template, url_for

app = flask.Flask(__name__, static_folder="static", template_folder="template")


@app.route("/")
def index():
    return render_template("upload.html")


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == "__main__":
    app.run(debug=True)
