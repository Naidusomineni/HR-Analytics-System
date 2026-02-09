from flask import Flask, render_template, request
from dashboard.charts import generate_charts
import joblib, pandas as pd
import numpy as np

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route("/", methods=["GET","POST"])
def home():

    generate_charts()   

    df = pd.read_csv("data/hr_data.csv")

    total = len(df)
    avg_salary = int(df["salary"].mean())
    attrition_rate = round(df["attrition"].mean()*100,2)


    prediction = None

    if request.method == "POST":
        data = np.array([[int(request.form["age"]),
                          int(request.form["salary"]),
                          int(request.form["years"]),
                          int(request.form["dept"]),
                          int(request.form["perf"])]])

        pred = model.predict(data)[0]
        prediction = "Will Leave" if pred==1 else "Will Stay"

    return render_template("index.html",
                           total=total,
                           salary=avg_salary,
                           rate=attrition_rate,
                           prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
