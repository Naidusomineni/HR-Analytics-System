from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import sqlite3

app = Flask(__name__)

# Load trained model
model = joblib.load("model/model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    # Read data from SQL database
    conn = sqlite3.connect("hr.db")
    df = pd.read_sql("SELECT * FROM employees", conn)
    conn.close()

    total = len(df)
    avg_salary = int(df["salary"].mean())
    attrition_rate = round(df["attrition"].mean() * 100, 2)

    prediction = None

    if request.method == "POST":
        age = int(request.form["age"])
        salary = int(request.form["salary"])
        years = int(request.form["years"])
        dept = int(request.form["dept"])
        perf = int(request.form["perf"])

        data = np.array([[age, salary, years, dept, perf]])
        pred = model.predict(data)[0]

        prediction = "Will Leave" if pred == 1 else "Will Stay"

    return render_template(
        "index.html",
        total=total,
        salary=avg_salary,
        rate=attrition_rate,
        prediction=prediction
    )


if __name__ == "__main__":
    app.run()
