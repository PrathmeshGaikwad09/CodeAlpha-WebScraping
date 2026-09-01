import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/employee_data.csv")

# Create charts folder
os.makedirs("charts", exist_ok=True)

# 1. Attrition Distribution
attrition_counts = df["Attrition"].value_counts()

plt.figure(figsize=(7, 5))
attrition_counts.plot(kind="bar")
plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/attrition_distribution.png")
plt.close()


# 2. Department vs Attrition
department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

department_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/department_attrition.png")
plt.close()


# 3. Gender vs Attrition
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
plt.savefig("charts/gender_attrition.png")
plt.close()


# 4. Age Distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=15,
    edgecolor="black"
)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/age_distribution.png")
plt.close()


# 5. Monthly Income Distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["MonthlyIncome"],
    bins=20,
    edgecolor="black"
)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/income_distribution.png")
plt.close()


# 6. Job Satisfaction Distribution
job_satisfaction = df["JobSatisfaction"].value_counts().sort_index()

plt.figure(figsize=(7, 5))
job_satisfaction.plot(kind="bar")

plt.title("Job Satisfaction Distribution")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/job_satisfaction.png")
plt.close()


# 7. Overtime vs Attrition
overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

overtime_attrition.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Overtime vs Attrition")
plt.xlabel("Overtime")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/overtime_attrition.png")
plt.close()


# 8. Job Level vs Attrition
joblevel_attrition = pd.crosstab(
    df["JobLevel"],
    df["Attrition"]
)

joblevel_attrition.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Job Level vs Attrition")
plt.xlabel("Job Level")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/joblevel_attrition.png")
plt.close()


print("All visualizations generated successfully!")
