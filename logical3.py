import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

a = 10
b = 30
c = 20

if (a >=b and a >= c):
    print("a is greater than b and c")
if (b >=a and b >= c):
    print("b is greater than a and c")
if (c >=a and c >=b):
    print("c is greater than a and b")
print()