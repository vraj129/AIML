import csv
import pandas as pd
 
f =  open("C:\\Users\\Vraj.Patel\\Desktop\\Vraj Patel\\AIML\\week12\\pandasEx\\movies.csv")
data = list(csv.reader(f))
print(data[0])