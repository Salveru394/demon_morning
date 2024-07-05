import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

my_list = [1, 2, 3, 4, 5]
i = len(my_list) -1
while i >= 0:
    print(my_list[i])
    i -= 1