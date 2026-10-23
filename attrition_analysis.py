import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "IBM-HR-Analytics-Employee-Attrition-and-Performance.csv"
)

counts = df["Attrition"].value_counts()

counts.plot(
    kind="bar",
    title="Employee Attrition Distribution"
)
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
