# ============================================
# where you are going to implement everything via api
# a) expiry finding for given index for any date
# ============================================

from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)#stsrt flask API

@app.route("/")#open URL in Browser
def home():
    return "Simple Expiry API Running!"

@app.route("/expiry", methods=["GET"])#user pas value
def get_expiry():

    index = request.args.get("index")#pas index
    date_str = request.args.get("date")#pas date

    # it do try if date is current formed
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()#strptime convert string into time
    except:#if not in formed so crete  error
        return jsonify({"error": "Date format must be YYYY-MM-DD"})

    # expiry weekday: NIFTY = 3 (Thu), BANK-NIFTY = 2 (Wed)
    if index.upper() == "NIFTY":
        expiry_day = 3 #Thursday = 3
    elif index.upper() == "BANK-NIFTY":
        expiry_day = 2 #Wednesday = 2
    elif index.upper() == "FIN-NIFTY":
        expiry_day = 1 # Tuesday
    else:
        return jsonify({"error": "Only NIFTY or BANK-NIFTY allowed"})

    # move forward day-by-day until expiry day matches
    while d.weekday() != expiry_day:
        d += timedelta(days=1)# Add 1 day to date d

    return jsonify({
        "index": index,
        "expiry": str(d)
    })

if __name__ == "__main__":
    app.run(debug=True)#Code બદલશો → server auto restart

