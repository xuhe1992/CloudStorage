# -*- coding: utf-8 -*-

"""
@date: 2020/1/5
@creator: he.xu
@description: 
"""

from storage.start import app
from flask import render_template


@app.route("/upload/", methods=["GET"])
def upload():
    return render_template("upload.html")


@app.route("/upload/", methods=["POST"])
def upload():
    pass
