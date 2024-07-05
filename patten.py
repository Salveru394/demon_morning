import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

rows = 4

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for each column
    for j in range(1, i + 1):
        print('*', end=' ')
    print()