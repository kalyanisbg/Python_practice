from flask import Flask, jsonify, request
# from flask_cors import CORS
from SessionProject import flights, utils


app = Flask(__name__)


# getting information

@app.route('/')
def hello():
    return {'hello': 'Universe'}


@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights.flights)


@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = utils.search_flights(id, flights.flights)
    return jsonify(flight)


# Adding new flights
@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flights.flights.append(flight)
    return flight


@app.route('/flights/<int:fid>', methods=['PUT'])
def update_flight(fid):
    pass

if __name__ == '__main__':
    app.run(debug=True)