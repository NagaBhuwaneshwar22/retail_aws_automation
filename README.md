# 🛒 Retail Data Engineering Project

An end-to-end modular data pipeline built using **PySpark + PostgreSQL**.

This project demonstrates:
- CSV ingestion using PySpark
- Data cleansing
- Automated table creation in PostgreSQL
- JDBC-based data loading
- Modular project architecture
- Environment-based configuration
- Git-ready professional structure

---

## 🏗 Project Architecture

```
CSV Files → PySpark → Data Cleaning → PostgreSQL (via JDBC)
```

---

## 📂 Project Structure

```
retail_data_project/
│
├── data/                   # Raw CSV files
├── spark_jars/             # PostgreSQL JDBC driver
│
├── core/
│   ├── spark_session.py    # Spark session creator
│   ├── db.py               # PostgreSQL connection & query execution
│   ├── loader.py           # Generic JDBC loader
│
├── tables/
│   ├── orders.py           # Orders pipeline logic
│   ├── customers.py        # (Future)
│   ├── products.py         # (Future)
│
├── config/
│   ├── settings.py         # Environment config handler
│
├── utils/
│   ├── spark_utils.py      # Utility functions
│
├── run_pipeline.py         # Main pipeline runner
├── .env                    # Environment variables
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- Python
- PySpark (Local Mode)
- PostgreSQL
- JDBC
- psycopg2
- VS Code
- Git

---

## 🗄 Database Schema (Orders Table)

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date TIMESTAMP,
    order_customer_id INT,
    order_status VARCHAR(50)
);
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file in root:

```
ORDERS_FILE_PATH=your_csv_path_here

DB_HOST=localhost
DB_USER=postgres
DB_PASS=your_password
DB_NAME=retail_db
DB_PORT=5432
```

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd retail_data_project
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv py-venv
py-venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Download PostgreSQL JDBC Driver

Download from:
https://jdbc.postgresql.org/download/

Place the `.jar` file inside:

```
spark_jars/
```

---

## 🚀 Running the Pipeline

Run using:

```bash
spark-submit --jars spark_jars/postgresql-42.x.x.jar run_pipeline.py
```

---

## ✅ What This Project Demonstrates

- Modular pipeline design
- Separation of concerns
- Reusable Spark session management
- Automated DDL execution
- Secure config using environment variables
- Clean JDBC integration
- Scalable design for multiple tables

---

## 📈 Future Enhancements

- Incremental data loading
- SCD Type-2 implementation
- Batchsize optimization for JDBC
- Airflow orchestration
- AWS S3 integration
- Terraform-based infrastructure
- Logging & monitoring
- Unit testing with pytest

---

## 👨‍💻 Author

Retail Data Engineering Practice Project  
Built for hands-on learning and cloud-ready development.

---

## 🧠 Learning Goal

This project is designed to simulate real-world Data Engineering workflows and enforce production-level best practices.
