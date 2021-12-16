from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL


app = Flask(__name__)
CORS(app)

orders = [
          {
          "car_type": "sedan",
          "car_brand": "skoda",
          "car_model": "octavia",
          "problem": "auto nestartuje",
          "first_name": "Amanda",
          "last_name": "Green",
          "tel_number": "0912345678",
          "email": "green@gmail.com"     
          },
          {
          "car_type": "hatchbag",
          "car_brand": "volkswagen",
          "car_model": "passat",
          "problem": "nejdu stierace",
          "first_name": "feri",
          "last_name": "zhrabovca",
          "tel_number": "09128521",
          "email": "feri@gmail.com"     
          }
          ]

@app.route("/", methods=["GET"])
def main():
  return jsonify(orders),200

@app.route("/vytvorit", methods=["POST"])
def create():
    data = request.get_json(force=True)
    data_dict = dict(data)
    orders.append(data_dict)
    return jsonify("created"),201

@app.route("/upravit/<id>", methods=["PUT"])
def update(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    ovocie[int(id)] = data_dict["upravit"]
    return jsonify("updated"),201

@app.route("/vymazat/<id>", methods=["DELETE"])
def delete(id):
    del orders[int(id)]
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
