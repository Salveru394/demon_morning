import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

factorial_number=1
n=8

for num in range(1,n+1):
    factorial_number*=num

    print(factorial_number)