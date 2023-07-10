

# import dependenices
import numpy as np
from flask import Flask, jsonify
from pymongo import MongoClient
import json

#################################################
# Database Setup
#################################################
# Create an instance of MongoClient
mongo = MongoClient(port=27017)

# assign the superstore database to a variable name
db = mongo['superstore']

# assign the collection to a variable
orders = db['orders']


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/customers<br/>"
        f"/api/v1.0/products"
    )

@app.route("/api/v1.0/customers")
def customers():
    # # Query for category
    # query = {'Category': 'Office Supplies'}
    # fields = {'Customer Name': 1, 'Sales': 1, '_id': 0}
    

    # Cast the results as a list and save them to a variable
    # results = list(orders.find(query, fields))
    results = db.orders.distinct('Customer Name')


    # Convert list of tuples into normal list
    customers = list(np.ravel(results))

    return jsonify(customers)

@app.route("/api/v1.0/products")
def products():
    #     # Query for category
    # query = {'Category': "Office Supplies"}
    # fields = {'Product Name': 1, 'Quantity': 1, '_id': 0}

    # Cast the results as a list and save them to a variable
    # results = list(orders.find(query, fields))
    results = db.orders.distinct('Product Name')


    # Convert list of tuples into normal list
    products = list(np.ravel(results))

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)