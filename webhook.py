from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    return jsonify({"status": 200})

@app.route("/pix", methods=["POST"])
def pix():
    print(request.json)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
