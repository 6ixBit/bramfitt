from src import app

from src.model import get_all_records
from src.controller import fetch_bus_times

# TODO: Make request to API and display live results
# TODO: Setup MongoDB to run with Docker 
# TODO: Store each result returned from API in DB and append a timestamp to each record when inserting
@app.route('/api')
def api():
    return fetch_bus_times()
    
# TODO: Fetch API calls stored in DB and return to client
# TODO: Make the database data available to be queried
@app.route('/db')
def database():
    result = get_all_records()
    return result