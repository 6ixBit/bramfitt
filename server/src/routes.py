from src import app

from src.model import get_all_records
from src.controller import fetch_bus_times

@app.route('/api')
def api():
    return fetch_bus_times()
    
@app.route('/db')
def database():
    result = get_all_records()
    return result