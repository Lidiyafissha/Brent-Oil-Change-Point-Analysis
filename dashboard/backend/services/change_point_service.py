import json

# Example: saved from Task 2 output
CHANGE_POINT_FILE = "../data/results/change_points.json"

def get_change_points():
    try:
        with open(CHANGE_POINT_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {"message": "Change point results not found"}
