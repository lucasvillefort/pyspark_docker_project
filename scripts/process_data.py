# docker exec -it spark-master spark-submit /scripts/process_data.py


from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("DataProcessing").getOrCreate()

# Load data
input_path = "/data/cards_data.csv"
output_path = "/processed_data/processed_output.csv"
model_path = "/processed_data/model"

# Read raw data
df = spark.read.csv(input_path, header=True, inferSchema=True)

# id,client_id,card_brand,card_type,card_number,expires,cvv,has_chip,num_cards_issued,credit_limit,acct_open_date,year_pin_last_changed,card_on_dark_web

# Assemble features
"""
assembler = VectorAssembler(
    inputCols=[
        "has_chip",
        "num_cards_issued",
        "credit_limit",
        "year_pin_last_changed",
        "card_on_dark_web",
    ],
    outputCol="features",
)
df = assembler.transform(df)

# Train model
lr = LinearRegression(featuresCol="features", labelCol="credit_limit")
lr_model = lr.fit(df)
lr_model.save(model_path)"""

# Save processed data
df.write.csv(output_path)

spark.stop()
