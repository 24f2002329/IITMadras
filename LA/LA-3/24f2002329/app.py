import matplotlib
from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        df = pd.read_csv('./data.csv')
        id_type = request.form.get('ID')
        id_value = request.form.get('id_value')

        if id_type == 'student_id' and id_value:
            return student_data(df, int(id_value))
        elif id_type == 'course_id' and id_value:
            return course_data(df, int(id_value))
        else:
            return render_template('error.html')
    else:
        return render_template('error.html')

def student_data(df, sid):
    courses = df.loc[df['Student id'] == sid]

    if len(courses) == 0:
        return render_template('error.html')

    total = courses[' Marks'].sum()
    return render_template('student_data.html', courses=courses.to_dict(orient='records'), total=total)

def course_data(df, cid):
    marks = df.loc[df[' Course id'] == cid]

    if len(marks) == 0:
        return render_template('error.html')

    avg = marks[' Marks'].mean()
    max_marks = marks[' Marks'].max()
    export_plot(marks)
    return render_template('course_data.html', avg=avg, max_marks=max_marks)

def export_plot(data):
    freq = data[' Marks'].value_counts().sort_index()
    x = np.array(freq.index)
    lower_limit = (x.min() // 10) * 10

    plt.figure(figsize=(10, 6))
    plt.bar(x, freq.values, width=1, align='center')
    plt.xlim(lower_limit, 100)
    plt.xticks(range(lower_limit, 101, 10))
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('./static/bar-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    app.run(debug=False, port=5000) 
