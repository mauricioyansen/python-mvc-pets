from flask import Blueprint, jsonify

pets_blueprint = Blueprint("pets_routes", __name__)


@pets_blueprint.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"pets": ["dog", "cat", "parrot"]}), 200
