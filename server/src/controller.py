import requests
from datetime import datetime
from flask import jsonify
import dateutil.parser
import json

from src.model import insert_records

API_URL="https://api.tfl.gov.uk/StopPoint/490009333W/arrivals"

def fetch_bus_times(url=API_URL):
    list_of_bus_times = []

    try: 
        req = requests.get(url)

        for value in req.json(): 
            list_of_bus_times.append(prepare_response(value))

        insert_records(list_of_bus_times)
        return jsonify(list_of_bus_times)
    except:
        return jsonify({"error": "Failed to reach TFL API"})

def prepare_response(api_request: dict) -> dict: 
    result = {}

    try: 
        result["timestamp"] = parse_time(api_request["timestamp"])
        result["vehicle_num_plate"] = api_request["vehicleId"]
        result["station_name"] = api_request["stationName"]
        result["line_name"] = api_request["lineName"]
        result["bus_direction"] = api_request["direction"]
        result["destination_name"] = api_request["destinationName"]
        result["towards"] = api_request["towards"]
        result["expected_arrival"] = parse_time(api_request["expectedArrival"])
    except:
        result["error"] = "Failed to parse API response"

    return result

def parse_time(time: str):
    parsed = dateutil.parser.parse(time)
    return parsed.strftime("%H:%M:%S")

