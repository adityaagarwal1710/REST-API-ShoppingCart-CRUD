# REST-API-ShoppingCart-CRUD
A repository containing example of REST API in python with  flask  and  mongoDB, for CRUD operations on a cart.

In this repository, I will  explain my work on creating REST API in python with the help of flask, MongoDB to perform CRUD operations on shopping cart.<br>



## Tools/Modules/Packages  Required
- MongoDB : To create and maintain database
- Postman App : To make requests to API from client side
- Python(3.9.6) : To create the  API
- MongoDB Atlas
- Postman 
- Python (3.9.6)
- flask : To work with flask framework in python
- pymongo : To work with MongoDB database from python


## Operations that can be performed with API
- Create and/or Add items to  cart
- Get items in cart
- Update name, price,quantity of an item
- Remove specific item from cart


## Explaination about  different operations
- Create and/or  Add items to  cart :
  - Methods : POST
  - EndPoint : localhost:5000/add
  - form_data : "name", "price",  "quantity"
  
- Get items in cart :
  - This operation allow  you to  get all the items present in the cart
  - EndPoint : localhost:5000/allitems
  - Methods : GET
- Update name, quantity, price of item in cart
  - This  operation allow you to  update name of item present in the cart by providing item id.
  - EndPoint : localhost:5000/update/<id>
  - Methods : PUT
  
- Remove specific item from cart
  - This operation  allows you to  remove specific item from cart by providing its item id.
  - EndPoint : localhost:5000/delete/<id>
  - Methods : DELETE


## Code with explaination
- Importing requied packages
```python
from flask import Flask, Response, request
import json
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import pymongo
from flask import jsonify,request
```
- Starting the server
```python
app = Flask(__name__)
if (__name__ == "__main__"):
    app.run(debug=True)
```
- Connecting with MongoDB
app.config['MONGO_URI'] = "mongodb+srv://Aditya:1234@cluster0.9dqsb.mongodb.net/test?retryWrites=true&w=majority"
mongo=PyMongo(app)
```
- Adding to  the cart
```python
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
```
- Viewing the cart
```python
@app.route('/allitems')
def allitems():
    items=mongo.db.carts.find()
    resp=dumps(items)
    return resp
```
- Updating item from cart
```python

```
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

- Deleting item from cart
```python
@app.route('/delete/<id>',methods=['DELETE'])
def delete_item(id):
    mongo.db.carts.delete_one({'_id':ObjectId(id)})
    resp=jsonify("Item dleted")
    resp.status_code=200
    return resp
```

