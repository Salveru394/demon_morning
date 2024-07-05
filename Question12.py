import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

sum_even = 0
i = 2
while i <= 20:
    if i % 2 == 0:
     sum_even = sum_even + i
    i = i + 2
    print(sum_even)