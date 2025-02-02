from jinja2 import Template
import sys
import csv
import pandas as pd

arguments = sys.argv

filename = 'data.csv'
students = []

with open(filename, 'r') as file:
    data  = pd.read_csv(file)
    # for row in data.iterrows():
    #     students.append(row[1])
    #     print(row[1][2])
    data = data.to_dict('records')
    for student in data:
        students.append(student)