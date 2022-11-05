import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        failures = request.args.get('failures')
        activities = request.args.get('activities')
        higher_edu = request.args.get('higher_edu')
        studytime = request.args.get('studytime')
        G1 = request.args.get('G1')
        G2 = request.args.get('G2')
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
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))
