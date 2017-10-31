# Will do based on the projects: 
# - https://github.com/mattupstate/overholt/blob/master/overholt
# - https://github.com/imwilsonxu/fbone/tree/master/fbone

# Flask layout:
# - http://exploreflask.com/en/latest/organizing.html
# - http://blog.sampingchuang.com/structure-a-large-flask-api-backend-app/

# Blueprint:
# - http://flask.pocoo.org/docs/0.12/blueprints/

# CSS:
# - css is referred to in the html file
# - http://html.net/tutorials/css/lesson2.php
# - https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/How_CSS_works

from flask import Flask
from frontend.views import frontend

def create_app():

    app = Flask(__name__)
    app.register_blueprint(frontend)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port='5002')