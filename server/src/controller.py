import requests
from datetime import datetime

API_URL="https://api.tfl.gov.uk/StopPoint/490009333W/arrivals"

def fetch_bus_times(url=API_URL):
    list_of_bus_times = []

    try: 
        req = requests.get(url)

        for value in req.json(): 
            list_of_bus_times.append(prepare_response(value))

        return list_of_bus_times
    except:
        return {"error": "Failed to reach TFL API"}

def prepare_response(api_request: dict) -> dict: 
    result = {}

    try: #TODO: Parse ISO8601 timestamps received to human readable format
        result["timestamp"] = api_request["timestamp"]
        result["vehicle_num_plate"] = api_request["vehicleId"]
        result["station_name"] = api_request["stationName"]
        result["line_name"] = api_request["lineName"]
        result["bus_direction"] = api_request["direction"]
        result["mode_name"] = api_request["modeName"]
        result["destination_name"] = api_request["destinationName"]
        result["towards"] = api_request["towards"]
        result["expected_arrival"] = api_request["expectedArrival"]
    except:
        result["error"] = "Failed to parse API response"

    return result

