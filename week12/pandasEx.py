import csv
import pandas as pd
 
f =  open("path to file")
data = list(csv.reader(f))
print(data[0])