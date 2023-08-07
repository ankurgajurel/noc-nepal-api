from flask import Flask, jsonify, request

import data

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "this is an api for noc nepal prices. chk http://github.com/ankurgajurel/noc-nepal-api for docs",})

@app.route('/<product_name>')
def product(product_name, place = "all"):

    product_data = data.data_for_product(product_name)
    place = request.args.get('place', default = 'all', type = str)

    default_return = product_data

    if place != "all":
        send_data = []
        for each in default_return:
            if place.lower() in each["place"].lower():
                send_data.append(each)
                print(each)

        return jsonify(send_data)
    
    return (default_return)

if __name__ == "__main__":
    app.run(debug=False)