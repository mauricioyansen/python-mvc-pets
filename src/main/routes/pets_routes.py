from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer

pets_blueprint = Blueprint("pets_routes", __name__)


@pets_blueprint.route("/pets", methods=["GET"])
def list_pets():
    req = HttpRequest()
    view = pet_lister_composer()
    res = view.handle_request(req)

    return jsonify(res.body), res.status_code


@pets_blueprint.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    req = HttpRequest(params={"name": name})
    view = pet_deleter_composer()
    res = view.handle_request(req)
    return "", res.status_code
