# import pyhtml as h
# import sys
# import matplotlib.pyplot as plt

# def generate_student_details(student_id):
#     with open("data.csv", 'r') as f:
#         headers = f.readline().strip().split(',')
#         student_data = None
#         for line in f:
#             data = line.strip().split(',')
#             if int(data[0]) == student_id:
#                 if student_data is None:
#                     student_data = [data]
#                 else:
#                     student_data.append(data)
        
#         if student_data:
#             total_marks = sum(int(data[2]) for data in student_data)
#             result = h.html(
#                 h.head(
#                     h.title("Student Data"),
#                     h.style("table, th, td { border: 1px solid black; }")
#                 ),
#                 h.body(
#                     h.h1("Student Details"),
#                     h.table(
#                         h.tr(
#                             [h.th(x) for x in headers]
#                         ),
#                         *[h.tr(
#                             [h.td(data[0]), h.td(data[1]), h.td(data[2])]
#                         ) for data in student_data],
#                         h.tr(
#                             h.td("Total Marks"),
#                             h.td(""),  # Empty cell for Course ID column
#                             h.td(total_marks)  # Total marks in the Marks column
#                         )
#                     )
#                 )
#             )
#             with open("output.html", "w") as output_file:
#                 output_file.write(str(result))
#         else:
#             with open("output.html", "w") as output_file:
#                 output_file.write(str(h.html(
#                     h.head(h.title("Error")),
#                     h.body(h.h1("Student ID not found."))
#                 )))

# def generate_course_details(course_id):
#     with open("data.csv", 'r') as f:
#         headers = f.readline().strip().split(',')
#         marks = []
#         for line in f:
#             data = line.strip().split(',')
#             if int(data[1]) == course_id:
#                 marks.append(int(data[2]))
        
#         if marks:
#             avg_marks = sum(marks) / len(marks)
#             max_marks = max(marks)
            
#             # Generate histogram
#             plt.hist(marks, bins=10, edgecolor='black')
#             plt.xlabel('Marks')
#             plt.ylabel('Frequency')
#             plt.title(f'Histogram of Marks for Course {course_id}')
#             plt.savefig('histogram.png')
#             plt.close()
            
#             result = h.html(
#                 h.head(
#                     h.title("Course Details")
#                 ),
#                 h.body(
#                     h.h1("Course Details"),
#                     h.table(
#                         h.tr(
#                             h.th("Average Marks"),
#                             h.th("Maximum Marks")
#                         ),
#                         h.tr(
#                             h.td(f"{avg_marks:.2f}"),
#                             h.td(max_marks)
#                         )
#                     ),
#                     h.img(src="histogram.png")
#                 )
#             )
#             with open("output.html", "w") as output_file:
#                 output_file.write(str(result))
#         else:
#             with open("output.html", "w") as output_file:
#                 output_file.write(str(h.html(
#                     h.head(h.title("Error")),
#                     h.body(h.h1("Course ID not found."))
#                 )))

# def main():
#     if len(sys.argv) != 3:
#         with open("output.html", "w") as output_file:
#             output_file.write(str(h.html(
#                 h.head(h.title("Error")),
#                 h.body(h.h1("Invalid number of arguments."))
#             )))
#         return

#     param = sys.argv[1]
#     param_val = int(sys.argv[2])

#     if param == '-s':
#         generate_student_details(param_val)
#     elif param == '-c':
#         generate_course_details(param_val)
#     else:
#         with open("output.html", "w") as output_file:
#             output_file.write(str(h.html(
#                 h.head(h.title("Error")),
#                 h.body(h.h1("Invalid parameter."))
#             )))

# if __name__ == "__main__":
#     main()







"""

import sys
import csv
from jinja2 import Template
import matplotlib.pyplot as plt

students = {}
courses = {}

def dict_update(dictionary_name, student_id, course_id, marks):
    if student_id in dictionary_name.keys():
        dictionary_name[student_id][course_id] = marks
    else:
        dictionary_name[student_id] = {}
        dictionary_name[student_id][course_id] = marks


with open('data.csv', 'r') as data_file:
    f = csv.DictReader(data_file)
    line_count = 0
    for row in f:
        if line_count>=0:
            dict_update(courses, int(row[' Course id']),
                        int(row['Student id']), int(row[' Marks']))
            dict_update(students, int(row['Student id']),
                        int(row[' Course id']), int(row[' Marks']))
        line_count+=1

#Generating Student Template
students_template = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>IIT Madras</title>
  </head>
  <body>
    <h1 class="mainTitle">Student Details</h1>
    <table frame= "box" rules = "all">
      <tr>
        <th>Student id</th>
        <th>Course id</th>
        <th>Marks</th>
      </tr>
      {% for sub_id, marks in students_details %}
      <tr>
          <td>{{ student_id }}</td>
          <td>{{ sub_id }}</td>
          <td>{{ marks }}</td>
      </tr>
      {% endfor %}
      <tr>
        <td colspan="2" style="text-align: center">Total Marks</td>
        <td>{{ total_marks }}</td>
      </tr>
    </table>
  </body>
</html>
'''

#Generating Course Template
course_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IIT Madras</title>
</head>
<body>
    <h1>Course Details</h1>
    <table frame = "box" rules = "all">
        <tr>
            <th>Average Marks</th>
            <th>Maximum Marks</t>
        </tr>
        <tr>
            <td>{{Average_marks}}</td>
            <td>{{Maxium_marks}}</td>
        </tr>
    </table>
    <img src="course_histogram.png" alt="course_histogram" />
</body>
</html>
'''

#Generating Error Template
error_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IIT Madras</title>
</head>
<body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
        
    </table>
</body>
</html>
'''

arg_option = sys.argv[1]
arg_id = int(sys.argv[2])

try:

  if arg_option == '-c':

    # ----Generate Histogram----
    plt.hist(courses[arg_id].values(), bins=10)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig('course_histogram.png')

    # ----Generate Course details template
    template = Template(course_template)
    html_out = template.render(Average_marks=((sum(courses[arg_id].values())) /
                                          len(courses[arg_id].values())),
                               Maxium_marks=max(courses[arg_id].values()))
    html_outfile = open('output.html', 'w')
    html_outfile.write(html_out)
    html_outfile.close()

  elif arg_option == '-s':

    # ----Generate Student details template----
    template = Template(students_template)
    html_out = template.render(students_details=students[arg_id].items(),
                               student_id=arg_id,
                               total_marks=sum(students[arg_id].values()))
    html_outfile = open('output.html', 'w')
    html_outfile.write(html_out)
    html_outfile.close()

except:

  # ----Generating Error template----
  html_outfile = open('output.html', 'w')
  html_outfile.write(error_template)
  html_outfile.close()


"""
