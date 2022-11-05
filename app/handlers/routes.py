import this
from flask import Flask, jsonify, request, make_response
import joblib
import pandas as pd
import numpy as np
import os, json
from sklearn.ensemble import RandomForestClassifier as rf

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        missing_param_response = make_response(jsonify({ 'message': 'Missing one or more parameters required.' }), 400)
        invalid_param_response = make_response(jsonify({ 'message': 'One or more invalid parameters.' }), 400)
        # parse through parameters
        failures = request.args.get('failures')
        if (failures == None):
            return missing_param_response
        if (int(failures) < 0 or int(failures) > 4):
            return invalid_param_response
        activities = request.args.get('activities')
        if (activities == None):
            return missing_param_response
        if (not(activities == "true" or activities == "false" or int(activities) == 1 or int(activities) == 0)):
            return invalid_param_response
        higher_edu = request.args.get('higher_edu')
        if (higher_edu == None):
            return missing_param_response
        if (not(higher_edu == "true" or higher_edu == "false" or int(higher_edu) == 1 or int(higher_edu) == 0)):
            return invalid_param_response
        studytime = request.args.get('studytime')
        if (studytime == None):
            return missing_param_response
        if (int(studytime) < 1 or int(studytime) > 4):
            return invalid_param_response
        G1 = request.args.get('G1')
        if (G1 == None):
            return missing_param_response
        if (int(G1) < 0 or int(G1) > 20):
            return invalid_param_response
        G2 = request.args.get('G2')
        if (G2 == None):
            return missing_param_response
        if (int(G2) < 0 or int(G2) > 20):
            return invalid_param_response
        # create the df for query
        data = [[failures], [activities], [higher_edu], [studytime], [G1], [G2]]
        query_df = pd.DataFrame({
            'G1': pd.Series(G1),
            'G2': pd.Series(G2),
            'activities': pd.Series(activities),
            'failures': pd.Series(failures),
            'higher': pd.Series(higher_edu),
            'studytime': pd.Series(studytime)
        })
        query = pd.get_dummies(query_df)
        # get the prediction
        prediction = clf.predict(query)
        if (np.ndarray.item(prediction)):
            return make_response(jsonify({ 'message': 'Applicant is likely to succeed.' }), 200)
        return make_response(jsonify({ 'message': 'Applicant is not likely to succeed.' }), 200)
        ##return jsonify(np.ndarray.item(prediction))
