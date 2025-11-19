# ============================================
# Expiry Finder API (GET + POST Support)
# ============================================

from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)   # start flask API

@app.route("/")         # open URL in Browser
def home():
    return "Simple Expiry API Running!"

# -----------------------------
# Function to calculate expiry
# -----------------------------
def calculate_expiry(index, date_str):

    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
    except:
        return {"error": "Date format must be YYYY-MM-DD"}

    # expiry weekday: NIFTY = Thu, BANK-NIFTY = Wed, FIN-NIFTY = Tue
    if index.upper() == "NIFTY":
        expiry_day = 3  # Thu
    elif index.upper() == "BANK-NIFTY":
        expiry_day = 2  # Wed
    elif index.upper() == "FIN-NIFTY":
        expiry_day = 1  # Tue
    else:
        return {"error": "Only NIFTY, BANK-NIFTY, FIN-NIFTY allowed"}

    # move to upcoming expiry
    while d.weekday() != expiry_day:
        d += timedelta(days=1)

    return {
        "index": index,
        "expiry": str(d)
    }

# -----------------------------------
# GET Method  → /expiry?index=...&date=...
# -----------------------------------
@app.route("/expiry", methods=["GET"])
def get_expiry():
    index = request.args.get("index")
    date_str = request.args.get("date")

    result = calculate_expiry(index, date_str)
    return jsonify(result)

# -----------------------------------
# POST Method → JSON Input
# {
#   "index": "NIFTY",
#   "date": "2024-01-10"
# }
# -----------------------------------
@app.route("/expiry", methods=["POST"])
def post_expiry():

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    index = data.get("index")
    date_str = data.get("date")

    result = calculate_expiry(index, date_str)
    return jsonify(result)

# Run the server
if __name__ == "__main__":
    app.run(debug=True,port=5007)
