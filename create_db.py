import sqlite3
import pandas as pd

df = pd.read_csv("data/hr_data.csv")

conn = sqlite3.connect("hr.db")
df.to_sql("employees", conn, if_exists="replace", index=False)

conn.close()
print("HR database created successfully!")
