from src import app

from src.model import test_db
from src.controller import fetch_bus_times

# TODO: Make request to API and display live results
# TODO: Setup MongoDB to run with Docker 
# TODO: Store each result returned from API in DB and append a timestamp to each record when inserting
@app.route('/api')
def api():
    fetch_bus_times()
    return "Live api calls from TFL API"

# TODO: Fetch API calls stored in DB and return to client
# TODO: Make the database data available to be queried
@app.route('/db')
def database():
    test_db()
    return "Live from DB instance"