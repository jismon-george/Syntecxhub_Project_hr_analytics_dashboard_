# 👨‍💼 HR Analytics Dashboard
### Employee Attrition Analysis and Workforce Insights

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![Plotly](https://img.shields.io/badge/Plotly-5.x-orange)
![HTML](https://img.shields.io/badge/HTML-5-red)
![License](https://img.shields.io/badge/License-MIT-purple)

---

# 📌 Project Overview

The **HR Analytics Dashboard** is an interactive workforce analysis solution developed to help Human Resource departments understand employee behavior, monitor attrition trends, and support strategic decision-making.

The dashboard provides meaningful insights into:

- Employee Attrition
- Department Distribution
- Gender Diversity
- Salary Analysis
- Education Background
- Job Satisfaction
- Performance Ratings
- Workforce Demographics

This project demonstrates practical applications of **Data Analytics**, **Business Intelligence**, and **Data Visualization** techniques using Python.

---

# 🎯 Objectives

The primary objectives of this project are:

✔ Analyze employee attrition patterns

✔ Identify departments with high turnover

✔ Study salary distributions

✔ Understand employee demographics

✔ Improve retention strategies

✔ Provide data-driven HR recommendations


---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Data Analysis |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Plotly | Interactive Visualizations |
| Matplotlib | Charts |
| Seaborn | Statistical Graphs |
| HTML | Dashboard Export |
| Jupyter Notebook | Development |
| VS Code | IDE |
| Git & GitHub | Version Control |

---

# 📂 Repository Structure

```text
Syntecxhub_Project_hr_analytics_dashboard_

│
├── README.md
├── hr_analysis.py
├── hr_employee_data.csv
├── hr_analytics_dashboard.html
├── HR_Analytics_Report.docx
│
└── images/
```

---

# 📊 Dataset Description

The dataset contains employee-related information including:

| Column Name | Description |
|------------|-------------|
| Employee_ID | Unique employee identifier |
| Age | Employee age |
| Gender | Male/Female |
| Department | Department name |
| Education | Qualification |
| MonthlyIncome | Salary |
| Attrition | Yes / No |
| JobRole | Position |
| JobSatisfaction | Satisfaction Score |
| PerformanceRating | Rating |
| YearsAtCompany | Experience |

---

# ⚙️ Project Workflow

## Step 1 : Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

---

## Step 2 : Load Dataset

```python
df = pd.read_csv("hr_employee_data.csv")
```

---

## Step 3 : Data Cleaning

```python
df.info()

df.isnull().sum()

df.drop_duplicates(inplace=True)
```

---

## Step 4 : Exploratory Data Analysis


### Employee Attrition

```python
df['Attrition'].value_counts()
```

---

### Department Distribution

```python
df['Department'].value_counts()
```

---

### Gender Analysis

```python
df['Gender'].value_counts()
```


---

### Salary Analysis

```python
df['MonthlyIncome'].describe()
```


---

## Step 5 : Visualization


### Attrition Chart

```python
fig = px.pie(
df,
names='Attrition',
title='Employee Attrition'
)

fig.show()
```


---

### Department Analysis

```python
fig = px.bar(

df,
x='Department',
title='Department Distribution'

)

fig.show()

```


---

### Age Distribution

```python
fig = px.histogram(

df,
x='Age',
nbins=20

)

fig.show()

```


---

## Step 6 : Dashboard Generation


```python
fig.write_html(

"hr_analytics_dashboard.html"

)
```


---

# 📈 Dashboard Features


### Employee Attrition Rate

Tracks employee turnover.


### Gender Diversity Analysis

Shows male and female employee ratios.



### Salary Insights

Displays salary distribution patterns.



### Department Performance

Identifies workforce allocation.



### Education Statistics

Educational qualification analysis.



### Experience Analysis

Years spent in company.



### Interactive Visualizations

Zoom

Hover

Filter

Export


---

# 📑 Report Summary


The project report contains:

• Executive Summary

• Business Problem Statement

• Methodology

• Dataset Description

• Data Cleaning Steps

• Exploratory Data Analysis

• Dashboard Screenshots

• Findings

• Recommendations

• Conclusion


---

# 🔍 Key Findings


### High Attrition Departments

Departments with comparatively higher employee turnover were identified.


### Salary Influence

Employees with lower salaries showed higher attrition probability.


### Job Satisfaction

Employees having low satisfaction scores were more likely to leave.


### Experience Trend

Most employees leaving had fewer years in the organization.


---

# 💡 Recommendations


Increase employee engagement programs


Improve compensation structure


Conduct regular satisfaction surveys


Provide career growth opportunities


Implement employee retention strategies


---

# 🚀 How To Run


### Clone Repository


```bash
git clone https://github.com/jismon-george/Syntecxhub_Project_hr_analytics_dashboard_.git
```


### Install Dependencies


```bash
pip install pandas

pip install numpy

pip install matplotlib

pip install seaborn

pip install plotly
```


### Execute Project


```bash
python hr_analysis.py
```


Dashboard Output


```bash
hr_analytics_dashboard.html
```


Open the generated HTML file in any browser.



---

# 📸 Project Preview


Dashboard Includes


✔ KPI Cards

✔ Pie Charts

✔ Bar Charts

✔ Histograms

✔ Interactive Filters

✔ HR Summary Report



---

# 🎓 Learning Outcomes


Data Cleaning


Data Visualization


Business Intelligence


Exploratory Data Analysis


Dashboard Development


Human Resource Analytics


Python Programming


GitHub Project Management



---

# 👨‍💻 Author

### JISMON GEORGE

MCA Student  
St. Joseph's College of Engineering and Technology, Palai

Data Analyst | AI & Machine Learning Enthusiast

GitHub: https://github.com/jismon-george

LinkedIn: www.linkedin.com/in/jismon-george-3194a7294


---



