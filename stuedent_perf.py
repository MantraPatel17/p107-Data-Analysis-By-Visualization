import pandas as pd
import csv
import plotly.express as px


reader = pd.read_csv("data.csv")

mean = reader.groupby(["student_id", "level"], as_index=False)[
    "attempt"].mean()


print(reader.groupby("level")["attempt"].mean())

g = px.scatter(
    mean,
    x="student_id",
    y="level",
    color="attempt",
    size="attempt"
)

g.show()
