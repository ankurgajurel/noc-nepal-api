from flask import Flask, jsonify

from data import petrol_data, diesel_data, lpg_data

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "this is an api for noc nepal prices. chk http://github.com/ankurgajurel/noc-nepal-api for docs",})

@app.route('/petrol')
def petrol():
    return petrol_data.petrol_data

@app.route('/diesel')
def diesel():
    return diesel_data.diesel_data

@app.route('/lpg')
def lpg():
    return lpg_data.lpg_data

if __name__ == "__main__":
    app.run(debug=True, port=3000)