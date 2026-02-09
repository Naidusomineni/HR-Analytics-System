import pandas as pd
import matplotlib.pyplot as plt

def generate_charts():
    df = pd.read_csv("data/hr_data.csv")

    # attrition chart
    df["attrition"].value_counts().plot(kind="bar")
    plt.title("Attrition Count")
    plt.savefig("static/attrition.png")
    plt.clf()

    # department chart
    df["department"].value_counts().plot(kind="bar")
    plt.title("Department Distribution")
    plt.savefig("static/dept.png")
    plt.clf()
