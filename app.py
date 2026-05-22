medical_data = {
    "fever": {
        "disease": "Viral Fever",
        "explanation": "A viral infection that increases body temperature.",
        "precautions": [
            "Drink plenty of water",
            "Take rest",
            "Use paracetamol",
            "Consult doctor if it lasts more than 2 days"
        ]
    },
    "headache": {
        "disease": "Migraine",
        "explanation": "A condition causing severe headaches.",
        "precautions": [
            "Take proper sleep",
            "Avoid stress",
            "Avoid loud noise",
            "Consult doctor if severe"
        ]
    }
}
def get_response(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        data = medical_data["fever"]
    elif "headache" in user_input:
        data = medical_data["headache"]
    else:
        return "Please tell more symptoms."

    precautions = "\n- ".join(data["precautions"])

    return f"""
Disease: {data['disease']}

Explanation:
{data['explanation']}

Precautions:
- {precautions}

Note: This is not a medical diagnosis. Consult a doctor.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    reply = get_response(user_input)
    return jsonify({"reply": reply})

app.run(debug=True)
@app.route('/')
def home():
    return "Doctor Bot is Running 🚀"
