import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

sc = SparkContext("local[*]", "spark-program")

data = ["apple", "banana", "orange", "pear", "grape"]
rdd=sc.parallelize(data)
searchelement="an"
rdd1=rdd.filter(lambda x:searchelement in x).collect()

for i in rdd1:
    print(i)
