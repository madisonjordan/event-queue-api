from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from EventQueue.event import event_controller


@app.route('/')
def index():
    return "Hello World"


app.register_blueprint(event_controller.bp)
