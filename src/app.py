from flask import Flask
from event import event_controller

app = Flask(__name__)

app.register_blueprint(event_controller.bp)
