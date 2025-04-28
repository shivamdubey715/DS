from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    num3 = num1 + num2
    return jsonify({"result":num3})

@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    num3 = num1 * num2
    return jsonify({"result":num3})

if __name__ == '__main__':
    app.run(debug=True)