from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def calculate_risk(url):

    score = 0

    if len(url) > 50:
        score += 20

    if url.count('.') > 4:
        score += 20

    suspicious_words = [
        "login",
        "verify",
        "bank",
        "secure",
        "update"
    ]

    for word in suspicious_words:

        if word in url:
            score += 10

    return score

@app.route('/scan', methods=['POST'])
def scan():

    data = request.json

    url = data['url']

    score = calculate_risk(url)

    if score > 50:

        message = "🚨 Dangerous Website"

    elif score > 20:

        message = "⚠️ Suspicious Website"

    else:

        message = "✅ Safe Website"

    return jsonify({
        "message": message,
        "risk_score": score
    })

app.run(debug=True)
