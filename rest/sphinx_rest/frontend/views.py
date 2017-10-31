# Later we may add Bundle() functions


from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template('index.html') # it's in /templates

