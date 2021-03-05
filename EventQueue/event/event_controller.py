from flask import Blueprint, request, jsonify
from EventQueue.event.event_model import Event
from EventQueue.event.event_schema import EventSchema

bp = Blueprint("event", __name__, url_prefix="/event")


@bp.route('/', methods=["GET"])
def read_list():
    events = Event.query.all()
    schema = EventSchema(many=True)
    result = schema.dump(events)
    return {"events": result}


@bp.route('/<int:id>', methods=["GET"])
def read_individual(id):
    event = Event.query.get(id)
    schema = EventSchema()
    result = schema.dump(event)
    return result
   

@bp.route('/', methods=["POST"])
def create():
    pass


@bp.route('/<int:id>', methods=["PUT"])
def update():
    pass


@bp.route('/<int:id>', methods=["DELETE"])
def delete():
    pass
