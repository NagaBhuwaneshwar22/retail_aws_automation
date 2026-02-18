from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType
from core.spark_session import get_spark
from core.db import execute_query
from core.loader import load_to_postgres
import os
from dotenv import load_dotenv

load_dotenv()

def run_orders_pipeline():

    spark = get_spark()

    schema = StructType([
        StructField('order_id', IntegerType(), True),
        StructField('order_date', TimestampType(), True),
        StructField('order_customer_id', IntegerType(), True),
        StructField('order_status', StringType(), True),
    ])

    df = spark.read.format("csv") \
        .schema(schema) \
        .option("header", "false") \
        .load(os.getenv("ORDERS_FILE_PATH"))

    df_clean = df.na.drop()

    create_orders_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        order_date TIMESTAMP,
        order_customer_id INT,
        order_status VARCHAR(50)
    )
    """

    execute_query(create_orders_table_query)

    load_to_postgres(df_clean, "orders")

    print("Orders pipeline completed.")
