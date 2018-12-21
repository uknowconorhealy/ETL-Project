import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///resources/state_violence.sqlite")

# Save reference to the table
type_and_rate = pd.read_sql('select * from type_and_rate', con=engine)
gun_incidents = pd.read_sql('select * from gun_incidents', con=engine)
#Put second table here

session = Session(engine)

#Set up Flask
app = Flask(__name__)


#Create routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f'Welcome to the state violence API. This API contains data by state for violent incidents across 2015. Please see the routes below<br/>'
        f"Available Routes:<br/>"
        f'</br>'
        f"/api/v1.0/type_and_rates<br/>"
        f"Columns: State, Total Murders, Total, Handguns, Rifles, Shotguns, Unknown Firearms, Knives, Other Weapons, Hands/Feet/etc, Total Population, Murders and Nonnegligent Manslaughter, Gun Ownership (%), Murders and Nonnegligent Manslaughter Rate (%), Murder Rate (%), Gun Murder Rate (%)<br/>"
        f'</br>'
        f"/api/v1.0/gun_incidents<br/>"
        f'Columns: State, Incident ID, Date, City or County, Killed, Injured'
    )

@app.route("/api/v1.0/type_and_rates")
def type_and_rates():
    """Return a list of types of weapons and murder rates per state"""
    # Query all passengers
    #results = session.query('type_and_rate').all()

    return pd.DataFrame.to_json(type_and_rate, orient='records')

@app.route("/api/v1.0/gun_incidents")
def incidents():
    """Return a list of types of weapons and murder rates per state"""
    # Query all passengers
    #results = session.query('type_and_rate').all()

    return pd.DataFrame.to_json(gun_incidents, orient='records')

if __name__ == '__main__':
    app.run(debug=True)