# 👥 Employee Attrition Analysis

> **What are the key factors influencing employee attrition?**

A complete end-to-end Data Analytics project that analyzes employee attrition using **Python**, **PostgreSQL**, and **Power BI**. The project explores employee behavior, identifies attrition patterns, and provides actionable business insights through data visualization and SQL analysis.

---

## 📌 Project Overview

Employee attrition is one of the biggest challenges organizations face. High attrition rates can increase recruitment costs, reduce productivity, and impact overall business performance.

This project analyzes a dataset containing **50,000 employee records** to identify the primary factors influencing employee turnover.

### Objectives

* Analyze employee attrition trends
* Identify high-risk employee groups
* Discover the impact of salary, experience, and performance on attrition
* Answer business questions using SQL
* Build an interactive Power BI dashboard
* Generate actionable HR insights

---

## 🛠️ Tech Stack

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| Python     | Data Cleaning & EDA     |
| Pandas     | Data Manipulation       |
| Matplotlib | Visualization           |
| Seaborn    | Statistical Charts      |
| PostgreSQL | Database & SQL Analysis |
| psycopg2   | PostgreSQL Connection   |
| Power BI   | Dashboard Creation      |

---

## 📁 Project Structure

```text
Employee_Attrition_Analysis/
│
├── Data/
│   ├── Employees.csv
│   └── Employees_cleaned.csv
│
├── Python_script/
│   ├── EDA.py
│   └── Injection_in_database_script.py
│
├── Sql_query/
│   ├── query.sql
│   └── query_and_output.docx
│
├── Power_bi_dashboard/
│   ├── Dashboard.pbix
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   └── 4.png
│
└── README.md
```

---

## 📊 Dataset Information

### Dataset Summary

| Metric   | Value           |
| -------- | --------------- |
| Records  | 50,000          |
| Features | 13              |
| Format   | CSV             |
| Domain   | Human Resources |

### Features

| Column             | Description          |
| ------------------ | -------------------- |
| Employee_ID        | Unique Employee ID   |
| Name               | Employee Name        |
| Age                | Employee Age         |
| Gender             | Male/Female          |
| Department         | Employee Department  |
| Job_Role           | Job Position         |
| Join_Date          | Joining Date         |
| Salary             | Employee Salary      |
| Performance_Rating | Performance Score    |
| Experience_Years   | Years of Experience  |
| Attrition          | Employee Left or Not |
| Exit_Date          | Exit Date            |
| Attrition_Reason   | Reason for Leaving   |

---

## 🔄 Data Pipeline

```text
Raw Dataset (CSV)
        │
        ▼
Python Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Cleaned Dataset
        │
        ▼
PostgreSQL Database
        │
        ▼
SQL Business Analysis
        │
        ▼
Power BI Dashboard
```

---

## 🧹 Data Cleaning

The dataset was cleaned using Python.

### Cleaning Steps

* Checked missing values
* Handled null records
* Converted data types
* Removed inconsistencies
* Created derived features
* Validated dataset quality

### Feature Engineering

New columns created:

* Working Status
* Age Group
* Experience Group
* Exit Reason

---

## 📈 Exploratory Data Analysis (EDA)

EDA was performed using Python libraries such as Pandas, Matplotlib, and Seaborn.

### Analysis Performed

* Attrition Distribution
* Department-wise Attrition
* Salary Analysis
* Experience Analysis
* Age Group Analysis
* Gender Analysis
* Job Role Analysis
* Performance Rating Analysis
* Attrition Reason Analysis

### Visualizations

* Count Plots
* Bar Charts
* Violin Plots
* Distribution Plots
* Heatmaps

---

## 💼 SQL Business Questions

The following business questions were answered using PostgreSQL:

### 1. What is the overall attrition rate?

### 2. Which departments have the highest attrition?

### 3. Which job roles are most likely to leave?

### 4. Are employees leaving early or after long tenure?

### 5. Do lower salaries contribute to attrition?

### 6. Which age group has the highest attrition?

### 7. Does gender influence attrition?

### 8. Which employee profile has the highest risk of leaving?

### 9. Which combination of salary and performance results in maximum attrition?

---

## 📊 Power BI Dashboard

The Power BI dashboard contains multiple pages for stakeholder analysis.

### Dashboard Pages

#### Page 1 – Attrition Overview

* Total Employees
* Attrition Rate
* Active Employees
* Attrition KPIs

#### Page 2 – Department Analysis

* Department-wise Attrition
* Job Role Breakdown

#### Page 3 – Demographic Analysis

* Age Group Analysis
* Gender Analysis
* Experience Analysis

#### Page 4 – Salary & Performance

* Salary Distribution
* Performance Impact
* Attrition Risk Analysis

---

## 📸 Dashboard Preview

### Attrition Overview

![Overview](Power_bi_dashboard/1.png)

### Department Analysis

![Department](Power_bi_dashboard/2.png)

### Demographic Analysis

![Demographics](Power_bi_dashboard/3.png)

### Salary & Performance Analysis

![Salary](Power_bi_dashboard/4.png)

---

## 💡 Key Findings

* Employees with lower salaries are more likely to leave.
* High-performing employees may leave when compensation is not competitive.
* Early-career employees show higher attrition rates.
* Certain departments experience significantly higher turnover.
* Better job opportunities are the most common reason for attrition.
* Salary and performance together are strong indicators of attrition risk.

---

## 📈 Business Recommendations

* Improve compensation strategies for high performers.
* Focus retention programs on early-career employees.
* Monitor departments with high turnover.
* Develop employee engagement initiatives.
* Implement predictive attrition monitoring.

---

## ▶️ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn psycopg2
```

### Run EDA

```bash
python Python_script/EDA.py
```

### Load Data into PostgreSQL

```bash
python Python_script/Injection_in_database_script.py
```

### Run SQL Queries

Execute:

```sql
Sql_query/query.sql
```

inside PostgreSQL.

### Open Dashboard

Open:

```text
Power_bi_dashboard/Dashboard.pbix
```

using Power BI Desktop.

---

## 🚀 Future Improvements

* Machine Learning Attrition Prediction
* Employee Churn Forecasting
* Real-Time Dashboard
* HR KPI Monitoring System
* Automated Reporting

---

## 👤 Author

**Vivek Mali**

Aspiring Data Analyst

### Skills

* Python
* SQL
* PostgreSQL
* Power BI
* Data Visualization
* Exploratory Data Analysis
* Business Intelligence

GitHub: https://github.com/Vivek7ok
