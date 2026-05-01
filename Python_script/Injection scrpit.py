import psycopg2
import time
import logging
import warnings

# 🚫 Ignore warnings (as per requirement)
warnings.filterwarnings("ignore")

# 📝 Configure Logging
logging.basicConfig(
    level=logging.INFO,  # Set log level
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_load.log"),  # Save logs to file
        logging.StreamHandler()  # Print logs to console
    ]
)

try:
    logging.info("🔗 Connecting to PostgreSQL database...")

    # 🔗 Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="empolyees",
        user="postgres",
        password="Vivek@123"
    )

    cur = conn.cursor()
    logging.info("✅ Database connection established")

    # 📂 File path
    file_path = r"D:\Data_set\Data_set_25\Data\employees_fixed.csv"

    # ⏱️ Start timer
    start = time.time()

    logging.info("📥 Starting data insertion using COPY command...")

    # 📥 Open file and insert data
    with open(file_path, 'r', encoding='utf-8') as file:

        copy_query = """
        COPY employees(
            employee_id, name, age, gender, department, job_role,
            join_date, salary, performance_rating, experience_years,
            attrition, exit_date, attrition_reason, working,
            age_group, experience_group, exit_reason
        )
        FROM STDIN WITH CSV HEADER
        """

        cur.copy_expert(copy_query, file)

    # 💾 Commit changes
    conn.commit()
    logging.info("💾 Data committed successfully")

    # ⏱️ End timer
    end = time.time()
    total_time = end - start

    logging.info(f"🔥 Data inserted successfully in {total_time:.2f} seconds")

except Exception as e:
    logging.error("❌ Error occurred during data insertion")
    logging.error(str(e))

    # 🔄 Rollback if error happens
    if 'conn' in locals():
        conn.rollback()
        logging.info("↩️ Transaction rolled back")

finally:
    # 🔒 Close connections safely
    if 'cur' in locals():
        cur.close()
        logging.info("🔒 Cursor closed")

    if 'conn' in locals():
        conn.close()
        logging.info("🔌 Database connection closed")