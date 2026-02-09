import matplotlib
matplotlib.use("Agg")   # ⭐ VERY IMPORTANT (no GUI backend)

import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_charts():
    df = pd.read_csv("data/hr_data.csv")

    os.makedirs("static", exist_ok=True)

    # Attrition chart
    df["attrition"].value_counts().plot(kind="bar")
    plt.title("Attrition Count")
    plt.savefig("static/attrition.png")
    plt.close()

    # Department chart
    df["department"].value_counts().plot(kind="bar")
    plt.title("Department Distribution")
    plt.savefig("static/dept.png")
    plt.close()
