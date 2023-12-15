# -*- coding: utf-8 -*-
from app import app
from flask import request
from app import model

@app.route("/api/data",methods=['GET'])
def get_predict():
    airlines = ["IndiGo","Air India", "SpiceJet","Vistara"]
    departure = str(request.args.get("dep"))
    destination = str(request.args.get("dest"))
    date = str(request.args.get("date"))
    total_stops = 'non-stop'
    info = 'no-info'
    route = 1.0
    predict = {
        "departure city": departure,
        "destination city": destination,
        "date": date,
        "prices":[]
    }
    
    for airline in airlines:
        price = float(model.predict(airline, date, departure, destination, route, total_stops, info))
        airline_price = {
            "airline": airline,
            "price": price
        }
        
        predict["prices"].append(airline_price)

    return predict


