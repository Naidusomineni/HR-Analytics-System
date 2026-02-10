import matplotlib
matplotlib.use("Agg")   # very important

import pandas as pd
import matplotlib.pyplot as plt
import os

# load data
df = pd.read_csv("data/hr_data.csv")

# ensure static folder exists
os.makedirs("static", exist_ok=True)

# attrition chart
df["attrition"].value_counts().plot(kind="bar")
plt.title("Attrition Count")
plt.savefig("static/attrition.png")
plt.close()

# department chart
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.savefig("static/dept.png")
plt.close()

print("Charts generated successfully!")
