import pandas as pd
import matplotlib.pyplot as plt
import os


file_path = "data/employee_data.csv"

df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


print("\n--- Dataset Information ---")
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Shape ---")
print(df.shape)


print("\n--- Missing Values ---")
print(df.isnull().sum())


print("\n--- Duplicate Records ---")
print("Duplicates:", df.duplicated().sum())


print("\n--- Statistical Summary ---")
print(df.describe())


print("\n--- Attrition Count ---")
print(df["Attrition"].value_counts())


os.makedirs("charts", exist_ok=True)


plt.figure(figsize=(7, 5))

df["Attrition"].value_counts().plot(kind="bar")

plt.title("Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("charts/attrition.png", dpi=300)
plt.close()


plt.figure(figsize=(8, 5))

plt.hist(df["Age"], bins=10)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("charts/age_distribution.png", dpi=300)
plt.close()


department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

department_attrition.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "charts/attrition_by_department.png",
    dpi=300
)

plt.close()


gender_attrition = pd.crosstab(
    df["Gender"],
    df["Attrition"]
)

gender_attrition.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Attrition by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    "charts/attrition_by_gender.png",
    dpi=300
)

plt.close()

plt.figure(figsize=(8, 5))

plt.hist(df["MonthlyIncome"], bins=20)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    "charts/monthly_income.png",
    dpi=300
)

plt.close()


job_satisfaction = df["JobSatisfaction"].value_counts().sort_index()

plt.figure(figsize=(7, 5))

job_satisfaction.plot(kind="bar")

plt.title("Job Satisfaction Distribution")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    "charts/job_satisfaction.png",
    dpi=300
)

plt.close()


overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

overtime_attrition.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Overtime vs Employee Attrition")
plt.xlabel("OverTime")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    "charts/overtime_vs_attrition.png",
    dpi=300
)

plt.close()


print("\nEDA completed successfully!")
print("Charts saved inside the charts folder.")