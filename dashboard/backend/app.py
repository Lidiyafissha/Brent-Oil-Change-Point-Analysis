from flask import Flask, jsonify, request
from flask_cors import CORS

from services.price_service import get_prices
from services.change_point_service import get_change_points
from services.event_service import get_events

app = Flask(__name__)
CORS(app)

@app.route("/api/prices")
def prices():
    start = request.args.get("start")
    end = request.args.get("end")
    return jsonify(get_prices(start, end))


@app.route("/api/change-points")
def change_points():
    return jsonify(get_change_points())


@app.route("/api/events")
def events():
    return jsonify(get_events())


if __name__ == "__main__":
    app.run(debug=True)
