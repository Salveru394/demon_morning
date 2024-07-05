import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

x = 1
while x <= 15:
    if x % 2 != 0:
       print(x)
    x =x + 1