# 👥 Employee Attrition Analysis

> **What are the main factors influencing employees to leave the company?**

A complete end-to-end data analytics project that analyses employee attrition using Python (EDA), PostgreSQL (SQL analysis), and Power BI (interactive dashboard) on a dataset of 50,000 employee records.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Data Pipeline](#-data-pipeline)
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis)
- [SQL Business Questions](#-sql-business-questions)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key Findings](#-key-findings)
- [How to Run](#️-how-to-run)

---

## 📖 Project Overview

Employee attrition — the rate at which employees leave a company — is one of the most costly challenges for HR departments. This project digs into a dataset of **50,000 employees** to uncover the key drivers behind attrition using a full analytics pipeline:

1. **Python** — Data cleaning, feature engineering, and visual EDA
2. **PostgreSQL** — Business question analysis using advanced SQL
3. **Power BI** — Interactive dashboard for stakeholders

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python (pandas, seaborn, matplotlib) | EDA & data visualisation |
| PostgreSQL + psycopg2 | Database storage & SQL analysis |
| Power BI | Interactive dashboard |
| CSV | Raw data format |

---

## 📁 Project Structure

```
Employees/
│
├── Data/
│   ├── employees.csv            # Raw dataset (50,000 rows)
│   └── employees_fixed.csv      # Cleaned dataset (loaded into PostgreSQL)
│
├── Python_script/
│   ├── EDA.py                   # Exploratory Data Analysis script
│   └── Injection script.py      # PostgreSQL data injection script
│
├── Sql_query/
│   ├── qeury.sql                # All business SQL queries
│   └── qeury_and_output.docx   # SQL queries with result outputs
│
├── Power bi dashbored/
│   ├── Employees.pbix           # Power BI project file
│   ├── 1.png                    # Dashboard screenshot - Overview
│   ├── 2.png                    # Dashboard screenshot - Department view
│   ├── 3.png                    # Dashboard screenshot - Demographics
│   └── 4.png                    # Dashboard screenshot - Salary & Performance
│
└── README.md
```

---

## 📊 Dataset

**File:** `Data/employees.csv`  
**Rows:** 50,000 employees  
**Columns:** 13

| Column | Description |
|---|---|
| `Employee_ID` | Unique identifier for each employee |
| `Name` | Employee full name |
| `Age` | Employee age |
| `Gender` | Male / Female |
| `Department` | Department (Finance, Sales, HR, etc.) |
| `Job_Role` | Role title (Manager, Analyst, etc.) |
| `Join_Date` | Date employee joined the company |
| `Salary` | Annual salary (numeric) |
| `Performance_Rating` | Rating from 1–5 |
| `Experience_Years` | Total years of experience |
| `Attrition` | Yes / No — did the employee leave? |
| `Exit_Date` | Date of exit (blank if still employed) |
| `Attrition_Reason` | Reason for leaving (Better Offer, etc.) |

**Derived Columns** (added in Python):

| Column | Description |
|---|---|
| `working` | `'yes'` if still employed, `'no'` if left |
| `Age_group` | Binned age: 22–30, 31–40, 41–50, 51–55 |
| `Experience_group` | Binned experience: 1–5, 6–10, 11–15 |
| `Exit_Reason` | Attrition reason only for employees who left |

---

## 🔄 Data Pipeline

```
employees.csv
      │
      ▼
  EDA.py  ──────────────────────────────────────────────
  • Load CSV                                            │
  • Inspect shape, nulls, dtypes                       │ Visualisations
  • Engineer: working, Age_group, Experience_group     │ (seaborn / matplotlib)
  • Save cleaned → employees_fixed.csv                 │
      │                                                 │
      ▼
  Injection script.py
  • Connect to PostgreSQL (psycopg2)
  • COPY employees_fixed.csv → employees table
      │
      ▼
  PostgreSQL — qeury.sql
  • Run 8 business questions
      │
      ▼
  Power BI — Employees.pbix
  • Connect to PostgreSQL
  • Build interactive dashboard
```

---

## 🔍 Exploratory Data Analysis

**Script:** `Python_script/EDA.py`

The EDA script performs the following steps:

**1. Data Loading & Inspection**
- Loads `employees.csv` using pandas
- Prints head/tail, `.describe()`, `.info()`, null counts

**2. Feature Engineering**
- Creates `working` column: `'yes'` if `Exit_Date` is null, else `'no'`
- Creates `Age_group` bins: 22–30 | 31–40 | 41–50 | 51–55
- Creates `Experience_group` bins: 1–5 | 6–10 | 11–15 years

**3. Visualisations**

| Chart | Insight |
|---|---|
| Performance Rating vs Working Status (countplot) | Do high performers leave more? |
| Performance Rating Distribution (violinplot) | Rating spread for active vs left employees |
| Attrition Reasons Count (horizontal bar) | What reasons are most common? |
| Gender vs Working Status | Does gender affect attrition? |
| Age Group vs Working Status | Which age group leaves most? |
| Job Role vs Working Status | Which roles have highest attrition? |
| Experience Group vs Working Status | Early-career vs late-career attrition |
| Exit Reasons (left employees only) | Why did leavers specifically exit? |

**Logging:** All steps are logged to `log.logging` with timestamps.

---

## 💼 SQL Business Questions

**File:** `Sql_query/qeury.sql`  
**Database:** PostgreSQL (`employees` table)

Eight business questions are answered:

### Q1 — What is the overall attrition rate?
```sql
SELECT COUNT(*) * 100 / (SELECT COUNT(*) FROM employees) AS attrition_rate
FROM employees
WHERE WORKING = 'no';
```

### Q2 — Which departments have the highest attrition?
Calculates department-wise attrition percentage using a correlated subquery.

### Q3 — Which job roles are most likely to leave?
Calculates role-wise attrition percentage.

### Q4 — Are employees leaving early (0–2 years) or after a long time?
Uses a CTE to bucket employees into `'2 year'` and `'more than 2 year'` experience groups and compares attrition percentage.

### Q5 — Are low-salary employees more likely to leave?
Segments employees as `'low'` (≤ ₹45,000) or `'high'` salary and compares attrition rates.

### Q6 — Which age group has the highest attrition?
Groups by `AGE_GROUP` column and calculates attrition per group.

### Q7 — Does gender affect attrition rate?
Calculates gender-wise contribution to overall attrition.

### Q8 — Can we predict attrition based on salary, performance & experience?
Uses a CTE with multi-condition `CASE` logic to classify employees as:
- `high_chances` — salary ≤ 35K, rating ≥ 4, experience ≥ 10 yrs
- `medium_chances` — salary ≤ 45K, rating ≥ 4, experience ≥ 7 yrs
- `low_chances` — salary ≤ 55K, rating ≥ 4, experience ≥ 5 yrs

### Bonus — Which combination leads to highest attrition: Low salary + high performance?
Segments salary × performance combinations and ranks by attrition %. Returns the top combination using `LIMIT 1`.

> 📄 Full query outputs are documented in `Sql_query/qeury_and_output.docx`

---

## 📊 Power BI Dashboard

**File:** `Power bi dashbored/Employees.pbix`

The dashboard consists of 4 pages:

| Page | Screenshot | Focus |
|---|---|---|
| Page 1 | `1.png` | Overall attrition overview & KPIs |
| Page 2 | `2.png` | Department & job role breakdown |
| Page 3 | `3.png` | Demographics (age, gender, experience) |
| Page 4 | `4.png` | Salary & performance analysis |

**To open the dashboard:**
1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/)
2. Open `Employees.pbix`
3. Update the PostgreSQL data source connection if needed (host/credentials)
4. Refresh data

---

## 💡 Key Findings

Based on the SQL queries and EDA:

- **Early-career employees (0–2 years)** show significantly higher attrition than long-tenured staff
- **Low salary + high performance** is the riskiest combination — high performers who feel underpaid are most likely to leave
- **Certain job roles and departments** carry disproportionately high attrition rates
- **Age group 22–30** tends to have the highest attrition (early career mobility)
- **Better Offer** is the most common attrition reason, pointing to compensation as the key lever

---

## ▶️ How to Run

### 1. Python EDA
```bash
pip install pandas numpy matplotlib seaborn
python Python_script/EDA.py
```

### 2. Load Data into PostgreSQL
```bash
pip install psycopg2
# Update credentials in the script first
python "Python_script/Injection scrpit.py"
```
> Update `host`, `database`, `user`, `password`, and `file_path` in the script to match your local PostgreSQL setup.

### 3. Run SQL Queries
Open `Sql_query/qeury.sql` in pgAdmin, DBeaver, or any PostgreSQL client and execute the queries against the `employees` table.

### 4. Power BI Dashboard
Open `Power bi dashbored/Employees.pbix` in Power BI Desktop.

---

## 👤 Author

**Vivek** — [GitHub](https://github.com/Vivek7ok)

---

*Built as a full end-to-end HR analytics project using Python · PostgreSQL · Power BI*
