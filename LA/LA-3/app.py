from flask import Flask, render_template, request
app = Flask(__name__)

# CSV Handling
with open('data.csv', 'r') as file:
    header = file.readline().split(',')
    data = file.read().split('\n')
    data = [i.split(',') for i in data]
print(data)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        ID = request.form['ID']
        id_value = request.form['id_value']
        if ID == 'student_id':
            student_data = []
            for item in data:
                if item[0] == id_value:
                    student_data.append(item)
            if student_data:
                template = '''
!'''
                return render_template("student", student_data = student_data)
            else:
                return render_template("error")
                    
            return render_template("student", student_id = id_value)
        elif ID == 'course_id':
            return render_template("course", course_id = id_value)
        else:
            return render_template("error")
        
    return render_template("index")
