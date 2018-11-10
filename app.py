from flask import Flask, Response

app = Flask(__name__)


@app.route("/set_default", methods=['GET'])
def set_defaults():
    return "Success"


@app.route("/like", methods=['POST'])
def like():
    return 0


@app.route("/museums", methods=['GET'])
def get_museums():
    museums = open("musuems.json", "r")
    resp = Response(response=museums, status=200, mimetype="application/json")
    return resp


app.run(host='0.0.0.0', debug=True)
