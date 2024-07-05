import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

ele=str(input("Enter the element string: "))
vowels="aeiouAEIOU"
count=0
for i in ele:
    if i in vowels:
        count=count+1
        print(count)