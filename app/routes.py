# -*- coding: utf-8 -*-
from app import app
from flask import request
from app import model

@app.route("/v1/api/data",methods=['GET'])
def get_predict():
    airlines = ["Air India","Vistara","IndiGo", "SpiceJet"]
    departure_city = str(request.args.get("departure"))
    destination_city = str(request.args.get("destination"))
    date = str(request.args.get("depdate"))
    total_stops = 'non-stop'
    info = 'no-info'
    route = 1.0
    data = {
        "departure_city": departure_city,
        "destination_city": destination_city,
        "date": date,
        "prices":[]
    }
    
    for airline in airlines:
        cost = float(model.predict(airline, date, departure_city, destination_city, route, total_stops, info))
        airline_cost = {
            "airline": airline,
            "cost": cost
        }
        
        data["prices"].append(airline_cost)

    return data


