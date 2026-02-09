import pandas as pd
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
import joblib, os

df = pd.read_csv("data/hr_data.csv")

le = LabelEncoder()
df["department"] = le.fit_transform(df["department"])

X = df[["age","salary","years","department","performance"]]
y = df["attrition"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("Model trained successfully!")
