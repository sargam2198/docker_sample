#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:06:35 2018

@author: Sargam
"""

import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger
import numpy as np
import pandas as pd

with open('rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: IRIS_Prediction
        schema:
          id: iris
          properties:
            prediction:
              type: array
              description: Class_of_iris
              items:
                type: int  
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return jsonify((str(prediction))) 

@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: IRIS_Prediction
        schema:
          id: iris1
          properties:
            prediction:
              type: array
              description: Class_of_iris1
              items:
                type:int
    """
        
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return jsonify(list(prediction))

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    