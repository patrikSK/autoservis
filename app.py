from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL


app = Flask(__name__)
CORS(app)


@app.route('/getOrders', methods=['GET'])			
def main():
  myDb = MYSQL.connect(host="147.232.40.14", user="mk257st", passwd="Zeayohk7", database="mk257st")
  cursor = myDb.cursor()
  with open("ddl/car/selectAllCarOwner.ddl") as ddl_file:
    query = ddl_file.read()
  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  vysledok = []
  for i in result:
    vysledok.append('{'+'"car_id":"{}","owner_id":"{}","date":"{}","type":"{}","brand":"{}","model":"{}","problem":"{}","name":"{}","surname":"{}","phone":"{}","email":"{}"'.format(i[0],i[6],i[1],i[2],i[3],i[4],i[5],i[8],i[9],i[10],i[11])+'}')
  vys = []
  for k in range(len(vysledok)):
    vys.append(eval(vysledok[k]))
  return jsonify(vys),200






@app.route("/createOrder", methods=["POST"])
def create():
  data = request.get_json(force=True)
  data_dict = dict(data)
  myDb = MYSQL.connect(host="147.232.40.14", user="mk257st", passwd="Zeayohk7", database="mk257st")

  cursor = myDb.cursor()
  with open("ddl/owner/selectIdPhone.ddl") as ddl_file:
    query = ddl_file.read()
  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  orders = []
  for i in result:
  	orders.append('{'+'"id":{},"phone":"{}"'.format(i[0],i[1])+'}')
  owners = []
  for i in range(len(orders)):
  	owners.append(eval(orders[i]))
  for i in owners:
    if i["phone"] == data_dict["phone"]:
      cursor = myDb.cursor()
      with open("ddl/car/insert.ddl") as ddl_file:
        query = ddl_file.read()
      query = query.format(data_dict['type'],data_dict['brand'],data_dict['model'],data_dict['problem'],i['id'])
      cursor.execute(query)
      cursor.close()
      break
  else:
    id = 1
    for j in owners:
      if id == j["id"]:
        id = j["id"] + 1
    cursor = myDb.cursor()
    with open("ddl/owner/insert.ddl") as ddl_file:
        query = ddl_file.read()
    query = query.format(id,data_dict['name'],data_dict['surname'],data_dict['phone'],data_dict['email'])
    cursor.execute(query)
    myDb.commit()
    cursor.close()

    cursor = myDb.cursor()
    with open("ddl/car/insert.ddl") as ddl_file:
        query = ddl_file.read()
    query = query.format(data_dict['type'],data_dict['brand'],data_dict['model'],data_dict['problem'],id)
    cursor.execute(query)
    cursor.close()


  myDb.commit()
  myDb.close()
  return jsonify("created"),201






@app.route("/updateOrder/<id>", methods=["PUT"])
def update(id):
  data = request.get_json(force=True)
  data_dict = dict(data)
  myDb = MYSQL.connect(host="147.232.40.14", user="mk257st", passwd="Zeayohk7", database="mk257st")

  cursor = myDb.cursor()
  with open("ddl/owner/update.ddl") as ddl_file:
    query = ddl_file.read()
  query = query.format(data_dict["owner_id"],data_dict['name'],data_dict['surname'],data_dict['phone'],data_dict['email'],data_dict['owner_id'])
  cursor.execute(query)
  myDb.commit()
  cursor.close()

  cursor = myDb.cursor()
  with open("ddl/car/update.ddl") as ddl_file:
    query = ddl_file.read()
  query = query.format(id,data_dict['type'],data_dict['brand'],data_dict['model'],data_dict['problem'],data_dict['owner_id'],id)
  cursor.execute(query)
  myDb.commit()
  cursor.close()
  
  myDb.close()
  return jsonify("Updated"),200





@app.route("/deleteOrder/<id>", methods=["DELETE"])
def delete(id):
  myDb = MYSQL.connect(host="147.232.40.14", user="mk257st", passwd="Zeayohk7", database="mk257st")
  cursor = myDb.cursor()
  with open("ddl/car/deleteId.ddl") as ddl_file:
    query = ddl_file.read()
  query = query.format(id)
  cursor.execute(query)
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("delete"),204


app.run()
