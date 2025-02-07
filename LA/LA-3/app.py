from flask import Flask, render_template, request, render_template_string
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# CSV Handling
with open('data.csv', 'r') as file:
    header = file.readline().split(',')
    data = file.read().split('\n')
    data = [i.split(',') for i in data]
    for i in data:
        i[0],i[1],i[2] = i[0].strip(),i[1].strip(),i[2].strip()
print(data)


# Templates:
error_template = '''
            <!DOCTYPE HTML>
            <html>
            <head>
                <title>Something Went Wrong</title>
            </head>
            <body>
                <h1>Wrong Inputs</h1>
                <p>Something Went Wrong</p>
                <a href="/">Go Back</a>
            </body>
            </html>
            '''

student_template = '''<!DOCTYPE HTML>
                <html>
                <head>
                    <title>Student Data</title>
                </head>
                <body>
                    <h1>Student Details</h1><br>
                    <table border = "2" id = "student-details-table">
                        <tr>
                            <th>Student Id</th>
                            <th>Course Id</th>
                            <th>Marks</th>
                        </tr>
                        {% for data in student_data %}
                        <tr>
                            <td>{{ data[0] }}</td>
                            <td>{{ data[1] }}</td>
                            <td>{{ data[2] }}</td>
                        </tr>
                        {% endfor %}
                        <tr>
                            <td colspan = "2" style="text-align:center"> Total Marks </td>
                            <td>{{ total_marks }}</td>
                        </tr>
                    </table><br>
                    <a href="/">Go Back</a>
                </body>
                </html>
                '''

course_template = '''<!DOCTYPE HTML>
                <html>
                <head>
                    <title>Course Data</title>
                </head>
                <body>
                    <h1>Course Details</h1><br>
                    <table border = "2" id = "course-details-table">
                        <tr>
                            <th>Average Marks</th>
                            <th>Maximum Marks</th>
                        </tr>
                        <tr>
                            <td>{{ avg_marks }}</td>
                            <td>{{ max_marks }}</td>
                        </tr>
                    </table><br>
                    <img src="static/histogram.png" height=250px width=300px alt="Histogram"><br>
                    <a href="/">Go Back</a>
                </body>
                </html>
                '''

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            ID = request.form['ID']
            id_value = request.form['id_value']
            if ID == 'student_id':
                student_data = []
                for item in data:
                    if item[0] == id_value:
                        student_data.append(item)
                if student_data:
                    total_marks = sum(int(item[2]) for item in student_data)
                    return render_template_string(student_template, student_data=student_data, total_marks=total_marks)
                else:
                    return render_template_string(error_template)

            elif ID == 'course_id':
                course_data = []
                for item in data:
                    if item[1] == id_value:
                        course_data.append(item)
                if course_data:
                    avg_marks = sum(int(item[2]) for item in course_data) / len(course_data)
                    max_marks = max(int(item[2]) for item in course_data)
                    plt.hist([int(item[2]) for item in course_data], bins = 10)
                    plt.xlabel('Marks')
                    plt.ylabel('Frequency')
                    histogram_path = 'static/histogram.png'
                    if os.path.exists(histogram_path):
                        os.remove(histogram_path)
                    plt.savefig(histogram_path)
                    plt.close()

                    # Add a query parameter to force reload
                    histogram_url = f"/static/histogram.png?{int(os.path.getmtime(histogram_path))}"
                    
                    return render_template_string(course_template, avg_marks=avg_marks, max_marks=max_marks)
                else:
                    return render_template_string(error_template)
            else:
                return render_template_string(error_template)
        except Exception as e:
            print(f"Error: {e}")
            return render_template_string(error_template)

        
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
