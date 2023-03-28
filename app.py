from datetime import datetime

import pandas as pd
from flask import Flask, jsonify
import os
os.environ['TZ'] = 'UTC'
app = Flask(__name__)
wsgi_app = app.wsgi_app


df = pd.DataFrame({"name":["iss"], "id":[25544], "latitude":[-37.154849142298], "longitude":[28.986038357665],"altitude":[433.50271238095],"velocity":[27537.123944258],"visibility":["daylight"],"footprint":[4575.5309717821],"timestamp":[1680003604],"daynum":[2460031.8280093],"solar_lat":[2.9303189144016],"solar_lon":[63.217224261698],"units":["kilometers"]})

df["latitude"] = df["latitude"].astype("float64")
df["longitude"] = df["longitude"].astype("float64")
df["altitude"] = df["altitude"].astype("float64")
df["velocity"] = df["velocity"].astype("float64")
df["footprint"] = df["footprint"].astype("float64")
df["daynum"] = df["daynum"].astype("float64")
df["solar_lat"] = df["solar_lat"].astype("float64")
df["solar_lon"] = df["solar_lon"].astype("float64")

df_p = df.T.to_dict('dict')


# A route to return all of the available entries in our catalog.
@app.route('/', methods=['GET'])
def api_all():
    with app.app_context():
        current_date_time = datetime.now()
        df_p[0].update({'timestamp': current_date_time})
        return jsonify(df_p[0])


# Add caching headers
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

app.config['JSON_AS_ASCII'] = False
# app.run()