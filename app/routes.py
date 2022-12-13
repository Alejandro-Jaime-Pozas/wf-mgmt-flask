from . import app
from flask import render_template

@app.route('/') # no methods here like GET or POST
def index():
    return render_template('index.html') # automatically looks to the templates folder in the app folder, no need to specify