
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from EventQueue.event import event_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Hello World"


app.register_blueprint(event_controller.bp)
