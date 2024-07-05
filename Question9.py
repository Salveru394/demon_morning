import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

ele=str(input("Enter the input string:"))
rev=""
for i in ele[::-1]:
    rev+=i
    print(rev)

