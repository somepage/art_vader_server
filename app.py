from flask import Flask, Response, request
import json
from recommend import change_weights

app = Flask(__name__)


@app.route("/set_default", methods=['GET', 'POST'])
def set_defaults():
    with open('weights.json', 'r') as f:
        json_data = json.load(f)
    json_data = {key: 1 / len(json_data) for key in json_data.keys()}
    with open('weights.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    return "Success request"


@app.route("/opinion", methods=['GET', 'POST'])
def like():
    like = bool(request.values.get("like"))
    label = request.values.get("label").lower()
    print(label)

    return change_weights(label, like)


@app.route("/museums", methods=['GET'])
def get_museums():
    with open('weights.json', 'r') as f:
        json_data = json.load(f)

    if len(set(json_data.values())) != 1:
        fav_label = [key for (key, value) in json_data.items() if value == max(list(json_data.values()))][0]
        museums = open("museums.json", "r")
        json_museum = json.load(museums)
        fav_museum = {"genre": fav_label,
                      "museums": json_museum[fav_label]}
        fav_museum_arr = [fav_museum]
        resp = Response(response=json.dumps(fav_museum_arr, ensure_ascii=False).encode('utf-8'), status=200,
                        mimetype="application/json")
        return resp
    else:
        resp = Response(response=[], status=200, mimetype="application/json")
        return resp


app.run(host='0.0.0.0', debug=True)
