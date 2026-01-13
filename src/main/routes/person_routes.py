from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer

person_blueprint = Blueprint("person_routes", __name__)


@person_blueprint.route("/people", methods=["POST"])
def create_person():
    req = HttpRequest(body=request.json)
    view = person_creator_composer()
    res = view.handle_request(req)
    return jsonify(res.body), res.status_code


@person_blueprint.route("/people/<int:person_id>", methods=["GET"])
def find_person(person_id):
    req = HttpRequest(params={"person_id": person_id})
    view = person_finder_composer()
    res = view.handle_request(req)
    return jsonify(res.body), res.status_code
