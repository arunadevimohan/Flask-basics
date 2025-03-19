from flask import Flask, render_template, request, jsonify

import webcolors
import json

app = Flask(__name__)

JSON_FILE = "hex_values.json"

def save_hex_value(hex_value):
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append({"hex": hex_value})
    
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hex_value = request.form.get("hex_value")
        if hex_value:
            save_hex_value(hex_value)
        return jsonify({"message": "Hex value saved!", "hex": hex_value})
    return render_template("color.html")

if __name__ == "__main__":
    app.run(debug=True)
