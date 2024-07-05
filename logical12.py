import os
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "C:/Users/91957/Documents/rahulfiles/Python/Python37/python.exe"  # or "python" depending on your Python executable
def count_even_numbers(start, end):
 count = 0
 for i in range(start, end):
     if i % 2 == 0:
         count = count + 1
    return count
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

even_count = count_even_numbers(start_range, end_range)
print(f"The count of even numbers between {start_range} and {end_range} is: {even_count}")