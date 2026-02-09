from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

from dashboard.charts import generate_charts

app = Flask(__name__)

# load model
model = joblib.load("model/model.pkl")

# ⭐ generate charts ONLY ONCE at startup (NOT inside route)
generate_charts()


@app.route("/", methods=["GET", "POST"])
def home():

    df = pd.read_csv("data/hr_data.csv")

    total = len(df)
    avg_salary = int(df["salary"].mean())
    attrition_rate = round(df["attrition"].mean()*100, 2)

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
