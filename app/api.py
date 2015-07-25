from flask import Blueprint, jsonify, request

from model import CoffeeShop

from . import db

api = Blueprint('api', __name__)

@api.route('/coffeeshops/')
def get_coffeeshops():
    coffeeshops = CoffeeShop.query.all()
    coffeeshops_json = [coffeeshop.to_json() for coffeeshop in coffeeshops]
    return jsonify(coffeeshops=coffeeshops_json)

@api.route('/coffeeshops/', methods=['POST'])
def add_coffeeshop():
    coffeeshop = CoffeeShop.from_json(request.json)
    db.session.add(coffeeshop)
    db.session.commit()
    return 201

