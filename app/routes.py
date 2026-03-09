from flask import Blueprint, request, jsonify
from app.services import calculate_calories, get_programs

api = Blueprint("api", __name__)


@api.route("/programs", methods=["GET"])
def programs():
    return jsonify(get_programs())


@api.route("/calories", methods=["POST"])
def calories():
    data = request.get_json()
    weight = data.get("weight")
    program = data.get("program")

    calories = calculate_calories(weight, program)

    return jsonify({
        "program": program,
        "weight": weight,
        "calories": calories
    })