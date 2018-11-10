from flask import Flask, Response, request
import json
from recommend import change_weights

app = Flask(__name__)


@app.route("/set_default", methods=['POST'])
def set_defaults():
    with open('weights.json', 'r') as f:
        json_data = json.load(f)
    json_data = {key: 1 / len(json_data) for key in json_data.keys()}
    with open('weights.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    return "Success request"


@app.route("/opinion", methods=['GET', 'POST'])
def like():
    like = bool(request.args.get("like"))
    label = request.args.get("label")
    return change_weights(label, like)


@app.route("/museums", methods=['GET'])
def get_museums():
    museums = open("museums.json", "r")
    resp = Response(response=museums, status=200, mimetype="application/json")
    return resp


app.run(host='0.0.0.0', debug=True)
