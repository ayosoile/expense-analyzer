from flask import Flask, render_template, request, redirect, Response
from sklearn.ensemble import IsolationForest
import sqlite3
import pandas as pd 

app = Flask(__name__)

#get connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

#pandas dataframe
def load_expenses_df():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM expenses", conn)
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"])
    df = df.sort_values("date")
    conn.close()
    return df

#Anomaly detector
def detect_anomalies(df):
    if len(df) < 5:
        df["is_anomaly"] = False
        return df
    
    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    #-1 for an anomaly and 1 if there isnt
    df["anomaly_score"] = model.fit_predict(df[["amount"]])
    df["is_anomaly"] = df["anomaly_score"] == -1

    return df



#initialize database
def init_db():
    conn = get_db_connection()
    conn.execute("""CREATE TABLE IF NOT EXISTS expenses (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date TEXT,
                 category TEXT,
                 amount REAL)""")
    conn.close()

#for debugging data types
@app.route("/debug")
def debug():
    df = load_expenses_df()
    return df.dtypes.to_string()

#home page
@app.route("/")
def index():
    df = load_expenses_df()
    df = detect_anomalies(df)

    expenses = df.to_dict(orient="records")
    return render_template("index.html", expenses=expenses)

#add db value
@app.route("/add", methods=["POST"])
def add_expense():
    date = request.form["date"]
    category = request.form["category"]
    amount = float(request.form["amount"])


    conn = get_db_connection()
    conn.execute(
        "INSERT INTO expenses (date, category, amount) VALUES (?,?,?)", (date,category, amount)
    )
    conn.commit()
    conn.close()

    return redirect("/")

#export to csv
@app.route("/export")
def export_csv():
    df = load_expenses_df()
    df = detect_anomalies(df)
    df = df.drop(columns=["id"])


    csv_data = df.to_csv(index=False)

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=expenses.csv"
        }
    )

#run app
if __name__ == "__main__":
    init_db()
    app.run(debug=True)