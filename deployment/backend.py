
from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open('pipe_best.pkl', 'rb') as f:
    pipemodel = pickle.load(f)

columns = ['bedrooms',
'bathrooms',
'sqft_living',
'sqft_lot',
'floors',
'waterfront',
'view',
'condition',
'grade',
'sqft_above',
'sqft_basement',
'yr_built',
'yr_renovated',
'lat',
'long',
'sqft_living15',
'sqft_lot15',
]
data = {
    'bedrooms' :           4.0,
    'bathrooms' :          2.5,
    'sqft_living' :     2710.0,
    'sqft_lot' :        8127.0,
    'floors' :             2.0,
    'waterfront' :         0.0,
    'view' :               0.0,
    'condition' :          3.0,
    'grade' :              8.0,
    'sqft_above' :      2710.0,
    'sqft_basement' :      0.0,
    'yr_built' :        1994.0,
    'yr_renovated' :       0.0,
    'lat' :               47.4,
    'long' :            -122.0,
    'sqft_living15' :   2520.0,
    'sqft_lot15' :      8436.0
}

@app.route("/")
def hello_world():
    return jsonify(data)

@app.route("/housing", methods=['GET', 'POST'])
def data_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [
            data['bedrooms'], 
            data['bathrooms'], 
            data['sqft_living'], 
            data['sqft_lot'],
            data['floors'], 
            data['waterfront'], 
            data['view'], 
            data['condition'],
            data['grade'], 
            data['sqft_above'], 
            data['sqft_basement'], 
            data['yr_built'],
            data['yr_renovated'],
            data['lat'],
            data['long'],
            data['sqft_living15'],
            data['sqft_lot15']
        ]

        new_data = pd.DataFrame([new_data], columns=columns)
        result = pipemodel.predict(new_data)

        response = {
            'code':200, 
            'status':'OK',
            'prediction': result[0]
        }

        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model"

# app.run(debug=True)