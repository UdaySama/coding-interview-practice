import json
import os

def read_users(filename="data.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []