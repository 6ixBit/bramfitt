# Run application

- run docker-compose build 
- run docker-compose up -d
- visit client application on localhost:8080
  
# Server endpoints [localhost:5000]

- /api - Returns response from TFL API
- /db - Returns past API calls from DB

# Server Tests

- run python3 -m unittest

# Imporvements

- Could store API URL and DB URI in config file so it can be read from environment
- Write more tests for lower level functions
- Fix table alignment on history page on certain mid sized devices
