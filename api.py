import json
from flask import Flask, request, jsonify
import requests

from ScraperModule.CostParser import Parser

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def getPrices():
    answer = Parser.Parse(request.json[0]["Address"], 1, 50)
    json_string = json.dumps(answer, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)

    url = "http://localhost:8080/answers"
    response = requests.post(url, data=str(json_string), stream=True)

    return "OK from Python"


if __name__ == '__main__':

    app.run()