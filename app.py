from flask import Flask, Response, request
import json
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import pymongo
from flask import jsonify,request

app=Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI'] = "mongodb+srv://Aditya:1234@cluster0.9dqsb.mongodb.net/test?retryWrites=true&w=majority"
mongo=PyMongo(app)



@app.route('/add',methods=['POST'])
def add_item():
    _json=request.json
    _name=_json['name']
    _price=_json['price']
    _quantity=_json['quantity']
    if _name and _price and _quantity and request.method=='POST':
        
        id=mongo.db.carts.insert_one({'name':_name,'price':_price,'quantity':_quantity})
        resp=jsonify("Item Added Successfully")
        resp.status_code=200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'Not Found'+request.url

    }
    resp=jsonify(message)
    resp.status_code=404
    return resp

@app.route('/allitems')
def allitems():
    items=mongo.db.carts.find()
    resp=dumps(items)
    return resp

@app.route('/allitems/<id>')
def item(id):
    item=mongo.db.carts.find_one({'_id':ObjectId(id)})
    resp=dumps(item)
    return resp

@app.route('/delete/<id>',methods=['DELETE'])
def delete_item(id):
    mongo.db.carts.delete_one({'_id':ObjectId(id)})
    resp=jsonify("Item dleted")
    resp.status_code=200
    return resp


@app.route('/update/<id>',methods=['PUT'])
def update_item(id):
    _id=id
    _json=request.json
    _name=_json['name']
    _price=_json['price']
    _quantity=_json['quantity']
    if _name and _price and _quantity and request.method=='PUT':
        mongo.db.carts.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else objectId(_id)},{'$set':{'name':_name,"price":_price,"quantity":_quantity}})
        resp=jsonify("Item Updates")
        resp.status_code=200
        return resp
    else:

        return not_found() 




if __name__ == "__main__":
    app.run(debug=True)
