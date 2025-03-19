from flask import Flask, render_template, request, jsonify
import json
import webcolors

app = Flask(__name__)


JSON_FILE = "color_hex_values.json"

def load_color_data():
    
    with open(JSON_FILE, "r") as file:
        return json.load(file)
    
def save_color_hex(color_name, hex_value):
    data = load_color_data()
    data[color_name] = hex_value
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/", methods=["GET", "POST"])
def color():

    
    if request.method == "POST":
        color_name = request.form.get("color_name")
        data = load_color_data()
        
        if color_name in data:
            return jsonify({"message": "Color already stored!","hex": data[color_name]})
        
        hex_value = webcolors.name_to_hex(color_name)
        save_color_hex(color_name, hex_value)
        return jsonify({"message": "New color stored!", "hex": hex_value})
    
    return render_template("color.html")
if __name__ == "__main__":
    app.run(debug=True)