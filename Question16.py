import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=0
while x < len(my_list):
    print(my_list[x])
    x = x + 1