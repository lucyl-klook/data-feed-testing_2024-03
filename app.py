import json

with open('hk-d-testing.json', 'r') as file:
    datafeed = json.load(file)


from flask import Flask, request, jsonify

app = Flask(__name__)

# Your JSON datafeed
datafeed = {
    "data": [
        # Your data objects here
    ]
}

@app.route('/datafeed', methods=['GET'])
def get_datafeed():
    # Retrieve headers
    locale = request.args.get('locale', default='en-US')
    vertical = request.args.get('verticals')
    date = request.args.get('date')
    country = request.args.get('country', default='HK')

    # Filter data based on headers
    filtered_data = [
        item for item in datafeed['data']
        if (locale is None or item['locale'] == locale) and
           (country is None or item['country'] == country) and
           (date is None or item['date'] == date)
    ]

    # If vertical is specified, further filter by vertical
    if vertical:
        for i in range(len(filtered_data)):
            filtered_data[i]['verticals'] = {key: val for key, val in filtered_data[i]['verticals'].items() if key == vertical}

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
