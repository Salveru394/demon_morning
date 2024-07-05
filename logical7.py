import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable

#for i in range(60):
#   print("Seekho Bigdata")

i = 0
while i < 60:
    i = i + 1
    print("seekho bigdata")
    