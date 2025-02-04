from jinja2 import Template
import sys
import pandas as pd

arguments = sys.argv 

students = [] # list of dictionaries containing student details

with open('data.csv', 'r') as file:
    data  = pd.read_csv(file)
    data = data.to_dict('records')
    for student in data:
        students.append(student)

def generate_student_details():
    