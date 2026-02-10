import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib, os

df = pd.read_csv("data/hr_data.csv")

le = LabelEncoder()
df["department"] = le.fit_transform(df["department"])

X = df[["age","salary","years","department","performance"]]
y = df["attrition"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

preds = model.predict(X)

acc = accuracy_score(y, preds)
cm = confusion_matrix(y, preds)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("Model trained successfully!")
print("Accuracy:", round(acc*100, 2), "%")
print("Confusion Matrix:")
print(cm)
