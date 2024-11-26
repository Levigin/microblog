# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'user': 'levigin'}
    posts = [
        {
            'author': {'user': 'Jon'},
            'body': "Beautiful day in Portland!"
        },
        {
            'author': {'user': 'Mary'},
            'body': "the Avengers movie was so cool"
        }
    ]
    return render_template("index.html", user=user, posts=posts)
