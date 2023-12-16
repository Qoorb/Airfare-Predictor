from pycaret.regression import *

import numpy as np
import pandas as pd


model = load_model('XGBoost_deployment_15122023')

cols = ['Airline', 'Date_of_Journey', 'Source', 'Destination',
        'Route', 'Total_Stops', 'Additional_Info']

def predict(*args) -> float:
    int_features = [x for x in args]
    final = np.array(int_features)
    
    data_unseen = pd.DataFrame([final], columns = cols)
    data_unseen['Date_of_Journey'] = data_unseen.Date_of_Journey.astype("datetime64")

    prediction = model.predict(data_unseen)
    prediction = prediction[0]
    
    return prediction