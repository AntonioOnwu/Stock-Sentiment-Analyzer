# type: ignore
from flask import Flask, json, jsonify, request

from Nasdaq import tickers
from Search import export_result
from WebScraping import export_json, mentions
from Blacklist import blacklist


app = Flask(__name__)

# displays top ten mentioned stocks and their rating
@app.route('/api/topMentions', methods=['POST'])
def topten():
    return export_json()

# gets all metioned stocks mentions and rating 
@app.route('/api/AllMentions', methods=['POST'])
def allMentions():
    return mentions()

# Getting user's input
@app.route('/api/query', methods=['POST'])
def create():
    request_data = json.loads(request.data)
    query = {"stock": request_data}
    with open('/Users/antonioonwu/stonkstop/src/Backend/Query.json', 'w') as outfile:
        json.dump(query, outfile, indent = 4)
    return query

# Gets query results
@app.route('/api/results', methods=['POST'])
def query():
        return export_result()



if __name__ == '__main__':
    app.run(debug=True)
    