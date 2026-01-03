Expense Tracker with Anomaly Detection

A full-stack Flask web application that allows users to record expenses and view them date sorted, analyze spending patterns, detect anonamlies in purchases using machine learning, and export results to CSV.

This project demonstrates backend development, data processing, and practical use of unsupervised machine learning in a real application.

🚀 Features

Add and store expenses (date, category, amount)

Persist data using SQLite

Display expenses in a clean web interface

Detect anomalous spending using Isolation Forest

Highlight anomalies visually in the UI

Export all expenses (including anomaly labels) to CSV

🧠 Machine Learning

This project uses Isolation Forest, an unsupervised anomaly detection algorithm from scikit-learn, to identify unusual expense amounts based on historical data.

No hardcoded thresholds or averages

The model learns what “normal” spending looks like

Expenses that are statistically isolated are flagged as anomalies

Requires at least 5 data points to produce meaningful results

🛠️ Tech Stack

Python

Flask – web framework

SQLite – lightweight database

Pandas – data processing

scikit-learn – anomaly detection (Isolation Forest)

HTML / CSS – frontend


▶️ How to Run Locally

Clone the repository

Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open your browser and visit:

http://localhost:5000

📤 CSV Export

The application includes a CSV export feature that allows users to download all expenses, including anomaly labels, for further analysis in tools like Excel or Google Sheets.

⚠️ Deployment Notes

The deployed demo version uses a shared SQLite database

Data may be shared across users and reset on service restarts

This setup is intentional for demonstration purposes

In a production environment, this would be replaced with:

User authentication

A production database (e.g., PostgreSQL)

User-scoped data isolation

Of course you can view this on your own machine using the instructions listed before