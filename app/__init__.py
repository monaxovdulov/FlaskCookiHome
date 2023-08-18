from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from app.controllers import home_controller
from app.controllers import support_controller
from app import routes, errors, cookies
