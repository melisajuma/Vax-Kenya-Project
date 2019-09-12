from flask import render_template
from  app.main.__init__ import main

@main.route('/')
def index():
    title = "Home"
    return render_template('index.html', title=title)

@main.route('/child/register')
def registerChild():
    return render_template('child.html', title = 'Form | Child Registration')