"""
HR Analytics Dashboard - Core Analysis
========================================
Covers all requirements from the project brief:
1. Analyze employee dataset (salary, department, experience)
2. Identify patterns in employee attrition
3. Perform correlation analysis to find key factors
4. Compare attrition across departments and roles
5. Build KPIs (attrition rate, retention rate, etc.)
6. Feed into HR dashboard for decision-making
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#444444"
plt.rcParams["axes.labelcolor"] = "#222222"
plt.rcParams["text.color"] = "#222222"
plt.rcParams["xtick.color"] = "#333333"
plt.rcParams["ytick.color"] = "#333333"

df = pd.read_csv("hr_employee_data.csv")
df["attrition_flag"] = (df["attrition"] == "Yes").astype(int)

# -------------------------------------------------------------------
# 1. DATASET OVERVIEW
# -------------------------------------------------------------------
print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)
print(f"Total employees: {len(df):,}")
print(f"Departments: {df['department'].nunique()}  |  Job roles: {df['job_role'].nunique()}")
print(f"Average age: {df['age'].mean():.1f}  |  Average tenure: {df['years_at_company'].mean():.1f} yrs")
print(f"Average monthly salary: {df['monthly_salary'].mean():,.0f}")

# -------------------------------------------------------------------
# 2. CORE KPIs
# -------------------------------------------------------------------
total_employees = len(df)
total_attrition = df["attrition_flag"].sum()
attrition_rate = total_attrition / total_employees * 100
retention_rate = 100 - attrition_rate
avg_tenure_left = df[df["attrition"] == "Yes"]["years_at_company"].mean()
avg_tenure_stayed = df[df["attrition"] == "No"]["years_at_company"].mean()
avg_salary_left = df[df["attrition"] == "Yes"]["monthly_salary"].mean()
avg_salary_stayed = df[df["attrition"] == "No"]["monthly_salary"].mean()
pct_overtime_left = (df[df["attrition"] == "Yes"]["overtime"] == "Yes").mean() * 100
pct_overtime_stayed = (df[df["attrition"] == "No"]["overtime"] == "Yes").mean() * 100
avg_satisfaction_left = df[df["attrition"] == "Yes"]["job_satisfaction"].mean()
avg_satisfaction_stayed = df[df["attrition"] == "No"]["job_satisfaction"].mean()

kpis = {
    "Total Employees": total_employees,
    "Total Attrition (count)": int(total_attrition),
    "Attrition Rate (%)": round(attrition_rate, 2),
    "Retention Rate (%)": round(retention_rate, 2),
    "Avg Tenure - Left (yrs)": round(avg_tenure_left, 2),
    "Avg Tenure - Stayed (yrs)": round(avg_tenure_stayed, 2),
    "Avg Monthly Salary - Left": round(avg_salary_left, 0),
    "Avg Monthly Salary - Stayed": round(avg_salary_stayed, 0),
    "% Overtime - Left": round(pct_overtime_left, 1),
    "% Overtime - Stayed": round(pct_overtime_stayed, 1),
    "Avg Job Satisfaction - Left": round(avg_satisfaction_left, 2),
    "Avg Job Satisfaction - Stayed": round(avg_satisfaction_stayed, 2),
}

print("\n" + "=" * 60)
print("KEY HR KPIs")
print("=" * 60)
for k, v in kpis.items():
    print(f"  {k:<32}: {v}")

kpi_df = pd.DataFrame(list(kpis.items()), columns=["KPI", "Value"])
kpi_df.to_csv("hr_kpis.csv", index=False)

# -------------------------------------------------------------------
# 3. ATTRITION PATTERNS (by satisfaction, overtime, tenure band, WLB)
# -------------------------------------------------------------------
print("\n" + "=" * 60)
print("ATTRITION PATTERNS")
print("=" * 60)

print("\n--- By Job Satisfaction (1=Low, 4=Very High) ---")
sat_pattern = df.groupby("job_satisfaction")["attrition_flag"].mean().mul(100).round(2)
print(sat_pattern.to_string())

print("\n--- By Overtime ---")
ot_pattern = df.groupby("overtime")["attrition_flag"].mean().mul(100).round(2)
print(ot_pattern.to_string())

print("\n--- By Tenure Band ---")
df["tenure_band"] = pd.cut(df["years_at_company"], bins=[-1, 1, 2, 5, 8, 100],
                            labels=["0-1 yrs", "2 yrs", "3-5 yrs", "6-8 yrs", "9+ yrs"])
tenure_pattern = df.groupby("tenure_band")["attrition_flag"].mean().mul(100).round(2)
print(tenure_pattern.to_string())

print("\n--- By Work-Life Balance (1=Low, 4=Best) ---")
wlb_pattern = df.groupby("work_life_balance")["attrition_flag"].mean().mul(100).round(2)
print(wlb_pattern.to_string())

# -------------------------------------------------------------------
# 4. CORRELATION ANALYSIS
# -------------------------------------------------------------------
print("\n" + "=" * 60)
print("CORRELATION ANALYSIS (vs. Attrition)")
print("=" * 60)

numeric_cols = ["age", "years_experience", "years_at_company", "years_since_last_promotion",
                "monthly_salary", "job_satisfaction", "work_life_balance",
                "performance_rating", "commute_distance_km", "attrition_flag"]

corr_matrix = df[numeric_cols].corr()
attrition_corr = corr_matrix["attrition_flag"].drop("attrition_flag").sort_values(key=abs, ascending=False)
print(attrition_corr.round(3).to_string())
attrition_corr.to_csv("attrition_correlations.csv", header=["correlation_with_attrition"])

# -------------------------------------------------------------------
# 5. DEPARTMENT & ROLE COMPARISON
# -------------------------------------------------------------------
print("\n" + "=" * 60)
print("ATTRITION BY DEPARTMENT")
print("=" * 60)
dept_summary = df.groupby("department").agg(
    headcount=("employee_id", "count"),
    attrition_count=("attrition_flag", "sum"),
    attrition_rate_pct=("attrition_flag", lambda x: round(x.mean() * 100, 2)),
    avg_salary=("monthly_salary", "mean"),
    avg_satisfaction=("job_satisfaction", "mean")
).sort_values("attrition_rate_pct", ascending=False)
print(dept_summary.to_string())
dept_summary.to_csv("department_summary.csv")

print("\n" + "=" * 60)
print("ATTRITION BY JOB ROLE (Top 10 by attrition rate, min 20 employees)")
print("=" * 60)
role_summary = df.groupby("job_role").agg(
    headcount=("employee_id", "count"),
    attrition_rate_pct=("attrition_flag", lambda x: round(x.mean() * 100, 2))
)
role_summary = role_summary[role_summary["headcount"] >= 20].sort_values("attrition_rate_pct", ascending=False)
print(role_summary.to_string())
role_summary.to_csv("role_summary.csv")

# -------------------------------------------------------------------
# 6. VISUALIZATIONS
# -------------------------------------------------------------------
PURPLE = "#5B4FE5"
PINK = "#D1499E"
BLUE = "#5B6EE8"
GREY = "#999999"

# --- Chart 1: Attrition rate by department ---
fig, ax = plt.subplots(figsize=(9, 5.5))
dept_sorted = dept_summary.sort_values("attrition_rate_pct")
colors = [PINK if v == dept_sorted["attrition_rate_pct"].max() else PURPLE for v in dept_sorted["attrition_rate_pct"]]
bars = ax.barh(dept_sorted.index, dept_sorted["attrition_rate_pct"], color=colors, height=0.6)
for bar, val in zip(bars, dept_sorted["attrition_rate_pct"]):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, f"{val:.1f}%", va="center", fontsize=11, fontweight="bold")
ax.set_xlabel("Attrition Rate (%)")
ax.set_title("Attrition Rate by Department", fontsize=15, fontweight="bold", pad=15)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("chart1_attrition_by_dept.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nSaved chart1_attrition_by_dept.png")

# --- Chart 2: Attrition by job satisfaction ---
fig, ax = plt.subplots(figsize=(8, 5.5))
labels = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}
sat_labels = [labels[i] for i in sat_pattern.index]
colors = [PINK if v == sat_pattern.max() else BLUE for v in sat_pattern]
bars = ax.bar(sat_labels, sat_pattern.values, color=colors, width=0.55)
for bar, val in zip(bars, sat_pattern.values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 1, f"{val:.1f}%", ha="center", fontsize=11, fontweight="bold")
ax.set_ylabel("Attrition Rate (%)")
ax.set_xlabel("Job Satisfaction Level")
ax.set_title("Attrition Rate by Job Satisfaction", fontsize=15, fontweight="bold", pad=15)
ax.set_ylim(0, max(sat_pattern.values) + 12)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("chart2_attrition_by_satisfaction.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart2_attrition_by_satisfaction.png")

# --- Chart 3: Attrition by overtime ---
fig, ax = plt.subplots(figsize=(6.5, 5.5))
colors = [PINK if v == ot_pattern.max() else BLUE for v in ot_pattern]
bars = ax.bar(ot_pattern.index, ot_pattern.values, color=colors, width=0.45)
for bar, val in zip(bars, ot_pattern.values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 1, f"{val:.1f}%", ha="center", fontsize=11, fontweight="bold")
ax.set_ylabel("Attrition Rate (%)")
ax.set_xlabel("Works Overtime")
ax.set_title("Attrition Rate: Overtime vs. No Overtime", fontsize=14, fontweight="bold", pad=15)
ax.set_ylim(0, max(ot_pattern.values) + 12)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("chart3_attrition_by_overtime.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart3_attrition_by_overtime.png")

# --- Chart 4: Attrition by tenure band ---
fig, ax = plt.subplots(figsize=(9, 5.5))
colors = [PINK if v == tenure_pattern.max() else PURPLE for v in tenure_pattern]
bars = ax.bar(tenure_pattern.index.astype(str), tenure_pattern.values, color=colors, width=0.55)
for bar, val in zip(bars, tenure_pattern.values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 1, f"{val:.1f}%", ha="center", fontsize=11, fontweight="bold")
ax.set_ylabel("Attrition Rate (%)")
ax.set_xlabel("Tenure at Company")
ax.set_title("Attrition Rate by Tenure Band", fontsize=15, fontweight="bold", pad=15)
ax.set_ylim(0, max(tenure_pattern.values) + 12)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("chart4_attrition_by_tenure.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart4_attrition_by_tenure.png")

# --- Chart 5: Correlation bar chart (key factors) ---
fig, ax = plt.subplots(figsize=(9.5, 6))
corr_sorted = attrition_corr.sort_values()
colors = [PINK if v > 0 else BLUE for v in corr_sorted]
bars = ax.barh(corr_sorted.index, corr_sorted.values, color=colors, height=0.55)
xmin, xmax = corr_sorted.min(), corr_sorted.max()
span = xmax - xmin
for bar, val in zip(bars, corr_sorted.values):
    offset = span * 0.03
    if val >= 0:
        ax.text(val + offset, bar.get_y() + bar.get_height()/2, f"{val:+.2f}", va="center", ha="left", fontsize=10, fontweight="bold")
    else:
        ax.text(val - offset, bar.get_y() + bar.get_height()/2, f"{val:+.2f}", va="center", ha="right", fontsize=10, fontweight="bold")
ax.axvline(0, color="#444444", linewidth=0.8)
ax.set_xlim(xmin - span * 0.22, xmax + span * 0.18)
ax.set_xlabel("Correlation with Attrition")
ax.set_title("Key Factors Correlated with Attrition", fontsize=15, fontweight="bold", pad=15)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("chart5_correlation_factors.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart5_correlation_factors.png")

# --- Chart 6: Salary comparison left vs stayed by department ---
fig, ax = plt.subplots(figsize=(9, 5.5))
salary_compare = df.groupby(["department", "attrition"])["monthly_salary"].mean().unstack()
x = np.arange(len(salary_compare.index))
width = 0.35
ax.bar(x - width/2, salary_compare["No"], width, label="Stayed", color=PURPLE)
ax.bar(x + width/2, salary_compare["Yes"], width, label="Left", color=PINK)
ax.set_xticks(x)
ax.set_xticklabels(salary_compare.index, rotation=20, ha="right")
ax.set_ylabel("Avg Monthly Salary")
ax.set_title("Average Salary: Stayed vs. Left, by Department", fontsize=14, fontweight="bold", pad=15)
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
plt.tight_layout()
plt.savefig("chart6_salary_comparison.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart6_salary_comparison.png")

print("\nAnalysis complete. All KPIs, summary tables, and charts generated.")
