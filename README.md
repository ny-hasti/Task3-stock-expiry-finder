# Task3-stock-expiry-finder
This API calculates the upcoming expiry date for NIFTY, BANK-NIFTY, or FIN-NIFTY based on any input date. The user passes an index and date in YYYY-MM-DD format, and the API returns the next valid expiry day by moving forward to Tuesday, Wednesday, or Thursday accordingly.

# Steps 
These are the steps your API follows when the user calls:
  /expiry?index=NIFTY&date=2025-11-20

**1. User sends two inputs**
index → NIFTY / BANK-NIFTY / FIN-NIFTY
date → YYYY-MM-DD

**2. API checks if index is valid**
If index is not one of:
NIFTY
BANK-NIFTY
FIN-NIFTY
→ API returns an error.

**3. API checks if date is valid**
If the date is not in YYYY-MM-DD format → API returns error.

**4. Convert that string date into a Python date object**
Example:
"2025-11-20" → becomes → 2025-11-20 (datetime.date object)

**5. Find expiry weekday**

Each index has a fixed expiry weekday:

Index	Expiry Day	Python weekday number
FIN-NIFTY	Tuesday	1
BANK-NIFTY	Wednesday	2
NIFTY	Thursday	3

**6. Compare**
Check:
Does the user’s date fall on the expiry weekday?
 If yes → return the same day

If no → move forward 1 day again and again until weekday matches

7. Return the expiry date as JSON

Example:
{
  "index": "NIFTY",
  "input_date": "2025-11-20",
  "expiry_date": "2025-11-20"
}


#  Working Steps of the Code 

Explained simply so anyone can understand the code flow.

**1. Import required modules**
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
Flask → to create API
datetime → to handle date
timedelta → for adding days

**2. Create Flask app**
app = Flask(__name__)

**3. Create mapping of index → weekday**
INDEX_WEEKDAY = {
    "FIN-NIFTY": 1,
    "BANK-NIFTY": 2,
    "NIFTY": 3
}

Python weekday numbering:
Mon=0, Tue=1, Wed=2, Thu=3, Fri=4, Sat=5, Sun=6

**4. Home route**
@app.route("/")
def home():
    return "Simple Expiry API Running!"

Just shows a welcome text.

**5. Main Expiry API**
@app.route("/expiry", methods=["GET"])
def get_expiry():

This creates the main endpoint: /expiry

***STEP A: Take user inputs***
index = request.args.get("index", "").strip().upper()
date_str = request.args.get("date", "").strip()


.upper() → makes input case-insensitive

.strip() → removes extra spaces

***STEP B: Validate index***
if index not in INDEX_WEEKDAY:
    return jsonify({"error": "Invalid index"}), 400


Checks if index is correct.

STEP C: Validate and convert date
input_date = datetime.strptime(date_str, "%Y-%m-%d").date()


Converts "2025-11-20" → date object.

***STEP D: Find target weekday***
target_weekday = INDEX_WEEKDAY[index]

***STEP E: Calculate expiry***
days_ahead = (target_weekday - input_date.weekday()) % 7
expiry_date = input_date + timedelta(days=days_ahead)


This finds how many days ahead the expiry day is.

Example
If input date is Wednesday (weekday = 2)
For NIFTY expiry = Thursday (weekday = 3)

days_ahead = (3 - 2) % 7 = 1
expiry_date = input_date + 1 day

***STEP F: Send the output***
return jsonify({
    "index": index,
    "input_date": input_date.isoformat(),
    "expiry_date": expiry_date.isoformat()
})
