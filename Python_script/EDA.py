import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import logging

# -----------------------------
# SETTINGS
# -----------------------------
warnings.filterwarnings("ignore")

logging.basicConfig(
    filename="log.logging",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")

# -----------------------------
# LOAD DATA
# -----------------------------
try:
    df = pd.read_csv(r'd:\Data_set\Data_set_25\Data\employees.csv')
    logging.info("Dataset loaded successfully")
except Exception as e:
    logging.error(f"Error loading dataset: {e}")

# -----------------------------
# BASIC INFO
# -----------------------------
print(df.head())
print(df.tail())
print(df.describe().T)
print(df.info())
print(df.columns)
print(df.isnull().sum())

logging.info("Basic data inspection completed")

# -----------------------------
# CREATE WORKING COLUMN
# -----------------------------
df['working'] = df['Exit_Date'].apply(lambda x: 'yes' if pd.isna(x) else 'no')
print(df['working'].value_counts())

logging.info("Working column created")

# -----------------------------
# VISUALIZATION SECTION
# -----------------------------

# 1. Performance Rating vs Working
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Performance_Rating', hue='working', palette='coolwarm')
plt.title("Performance Rating vs Working Status")
plt.xlabel("Performance Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 2. Distribution of Performance Rating (Better as violin)
plt.figure(figsize=(8,5))
sns.violinplot(data=df, x='working', y='Performance_Rating', palette='Set2')
plt.title("Performance Rating Distribution by Working Status")
plt.tight_layout()
plt.show()

# 3. Attrition Reason (Better as horizontal for readability)
plt.figure(figsize=(10,5))
sns.countplot(data=df, y='Attrition_Reason', palette='viridis')
plt.title("Attrition Reasons Count")
plt.xlabel("Count")
plt.ylabel("Reason")
plt.tight_layout()
plt.show()

# 4. Gender vs Working
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Gender', hue='working', palette='pastel')
plt.title("Gender vs Working Status")
plt.tight_layout()
plt.show()

# -----------------------------
# AGE GROUPING
# -----------------------------
bins = [20, 30, 40, 50, 60]  
labels = ['22-30', '31-40', '41-50', '51-55']

df['Age_group'] = pd.cut(df['Age'], bins=bins, labels=labels)

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Age_group', hue='working', palette='magma')
plt.title("Age Group vs Working Status")
plt.tight_layout()
plt.show()

# -----------------------------
# JOB ROLE
# -----------------------------
plt.figure(figsize=(12,5))
sns.countplot(data=df, y='Job_Role', hue='working', palette='cool')
plt.title("Job Role vs Working Status")
plt.tight_layout()
plt.show()

# -----------------------------
# EXPERIENCE GROUPING
# -----------------------------
bins = [0, 5, 10, 15]
labels = ['1-5', '6-10', '11-15']

df['Experience_group'] = pd.cut(
    df['Experience_Years'],
    bins=bins,
    labels=labels,
    include_lowest=True
)

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Experience_group', hue='working', palette='cubehelix')
plt.title("Experience Group vs Working Status")
plt.tight_layout()
plt.show()

# -----------------------------
# EXIT REASON (ONLY LEFT EMPLOYEES)
# -----------------------------
df['Exit_Reason'] = df['Attrition_Reason'].where(df['working'] == 'no')

plt.figure(figsize=(10,5))
sns.countplot(data=df, y='Exit_Reason', palette='rocket')
plt.title("Exit Reasons (Only Employees Who Left)")
plt.tight_layout()
plt.show()

# -----------------------------
# END LOG
# -----------------------------
logging.info("Script executed successfully")


print(df.info())