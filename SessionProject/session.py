from flask import Flask, jsonify
from SessionProject import flights


app = Flask(__name__)


# getting information

@app.route('/')
def hello():
    return {'hello': 'Universe'}

@app.route('/flights')
def get_flights():
    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True)