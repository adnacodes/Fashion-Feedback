from flask import Flask
import os
from pytrends.request import TrendReq
import pandas as pd

path = os.getcwd()
parent = os.path.dirname(path)

app = Flask(__name__, template_folder=parent + '/frontend')
pytrends = TrendReq(hl='en-US', tz=360)

@app.route('/')
def home():
    return {}

# Gather interest over time for a given search term
@app.route('/api/search/<param>')
def interest_over_time(param):
    pytrends.build_payload([param], timeframe='today 5-y')
    interest_over_time = pytrends.interest_over_time()
    return interest_over_time.to_json()

# Gathers related queries for a given search term
@app.route('/api/related/<param>')
def related(param):
    pytrends.build_payload([param], timeframe='today 5-y')
    related_queries = pytrends.related_queries()
    return related_queries[param]['top'].to_json()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3002)
