import pandas as pd
import os


df = pd.read_csv("data/employee_data.csv")

os.makedirs("reports", exist_ok=True)

print("\n========== EDA BUSINESS INSIGHTS ==========\n")


total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()

attrition_rate = (employees_left / total_employees) * 100

print("1. OVERALL ATTRITION")
print("--------------------")
print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print("Attrition Rate:", round(attrition_rate, 2), "%")



print("\n2. DEPARTMENT-WISE ATTRITION")
print("-----------------------------")

department_analysis = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

department_analysis["Attrition_Rate_%"] = (
    department_analysis["Yes"]
    / department_analysis.sum(axis=1)
) * 100

department_analysis["Attrition_Rate_%"] = (
    department_analysis["Attrition_Rate_%"].round(2)
)

print(department_analysis)



print("\n3. OVERTIME VS ATTRITION")
print("------------------------")

overtime_analysis = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

overtime_analysis["Attrition_Rate_%"] = (
    overtime_analysis["Yes"]
    / overtime_analysis.sum(axis=1)
) * 100

overtime_analysis["Attrition_Rate_%"] = (
    overtime_analysis["Attrition_Rate_%"].round(2)
)

print(overtime_analysis)



print("\n4. JOB SATISFACTION VS ATTRITION")
print("---------------------------------")

satisfaction_analysis = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"]
)

satisfaction_analysis["Attrition_Rate_%"] = (
    satisfaction_analysis["Yes"]
    / satisfaction_analysis.sum(axis=1)
) * 100

satisfaction_analysis["Attrition_Rate_%"] = (
    satisfaction_analysis["Attrition_Rate_%"].round(2)
)

print(satisfaction_analysis)



print("\n5. GENDER-WISE ATTRITION")
print("------------------------")

gender_analysis = pd.crosstab(
    df["Gender"],
    df["Attrition"]
)

gender_analysis["Attrition_Rate_%"] = (
    gender_analysis["Yes"]
    / gender_analysis.sum(axis=1)
) * 100

gender_analysis["Attrition_Rate_%"] = (
    gender_analysis["Attrition_Rate_%"].round(2)
)

print(gender_analysis)



print("\n6. AGE GROUP VS ATTRITION")
print("-------------------------")

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56+"
    ]
)

age_analysis = pd.crosstab(
    df["AgeGroup"],
    df["Attrition"]
)

age_analysis["Attrition_Rate_%"] = (
    age_analysis["Yes"]
    / age_analysis.sum(axis=1)
) * 100

age_analysis["Attrition_Rate_%"] = (
    age_analysis["Attrition_Rate_%"].round(2)
)

print(age_analysis)



print("\n7. MONTHLY INCOME VS ATTRITION")
print("------------------------------")

income_analysis = df.groupby("Attrition")["MonthlyIncome"].agg(
    ["mean", "median", "min", "max"]
)

income_analysis = income_analysis.round(2)

print(income_analysis)



print("\n8. YEARS AT COMPANY VS ATTRITION")
print("---------------------------------")

experience_analysis = df.groupby("Attrition")["YearsAtCompany"].agg(
    ["mean", "median", "min", "max"]
)

experience_analysis = experience_analysis.round(2)

print(experience_analysis)



print("\n9. JOB LEVEL VS ATTRITION")
print("------------------------")

joblevel_analysis = pd.crosstab(
    df["JobLevel"],
    df["Attrition"]
)

joblevel_analysis["Attrition_Rate_%"] = (
    joblevel_analysis["Yes"]
    / joblevel_analysis.sum(axis=1)
) * 100

joblevel_analysis["Attrition_Rate_%"] = (
    joblevel_analysis["Attrition_Rate_%"].round(2)
)

print(joblevel_analysis)



department_analysis.to_csv(
    "reports/department_attrition.csv"
)

overtime_analysis.to_csv(
    "reports/overtime_attrition.csv"
)

satisfaction_analysis.to_csv(
    "reports/job_satisfaction_attrition.csv"
)

gender_analysis.to_csv(
    "reports/gender_attrition.csv"
)

age_analysis.to_csv(
    "reports/age_group_attrition.csv"
)

income_analysis.to_csv(
    "reports/income_attrition.csv"
)

experience_analysis.to_csv(
    "reports/experience_attrition.csv"
)

joblevel_analysis.to_csv(
    "reports/joblevel_attrition.csv"
)



print("\n==========================================")
print("EDA INSIGHTS ANALYSIS COMPLETED!")
print("Analysis reports saved in reports folder.")
print("==========================================")
