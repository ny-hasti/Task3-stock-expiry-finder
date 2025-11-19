# Task3-stock-expiry-finder
This API calculates the upcoming expiry date for NIFTY, BANK-NIFTY, or FIN-NIFTY based on any input date. The user passes an index and date in YYYY-MM-DD format, and the API returns the next valid expiry day by moving forward to Tuesday, Wednesday, or Thursday accordingly.

<img width="405" height="144" alt="image" src="https://github.com/user-attachments/assets/80fc8120-9f47-499c-80f5-aee9f887cbc8" />


**Features**
Get expiry date for any given input date
Supports:
NIFTY → Thursday expiry
BANK-NIFTY → Wednesday expiry
FIN-NIFTY → Tuesday expiry
Easy GET API
Clean and beginner-friendly implementation

**Project Structure**
Expiry-API/
│
├── expiry.py          # Main Flask application
└── README.md       # Project documentation

****How to Run the API****
Clone or download the project
Navigate to the project folder

Run:
python app.py

Open your browser and test:
http://127.0.0.1:5000/

You should see:
Simple Expiry API Running!
📌 API Endpoint Details
1️⃣ Get Expiry Date

Endpoint:
GET /expiry

****How It Works (Logic)****
**Convert user date string to Python date
**Identify expiry weekday:**
NIFTY → Thursday (3)
BANK-NIFTY → Wednesday (2)
FIN-NIFTY → Tuesday (1)
Move forward day-by-day until date matches expiry weekday
Return the final expiry date
