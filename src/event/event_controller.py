
from flask import Blueprint, request, jsonify

bp = Blueprint("event", __name__, url_prefix="/event")


@bp.route('/', methods=["GET"])
def read_list():
    result = [
        {
            "id": 1,
            "name": "The best event ever",
            "date": "2020-03-08" 
        },
        {
            "id": 2,
            "name": "The worst event ever",
            "date": "2020-03-09"
        }
    ]
    return jsonify(result)


@bp.route('/<id>', methods=["GET"])
def read_individual(id):
    pass


@bp.route('/', methods=["POST"])
def create():
    pass


@bp.route('/<id>', methods=["PUT"])
def update():
    pass


@bp.route('/<id>', methods=["DELETE"])
def delete():
    pass
