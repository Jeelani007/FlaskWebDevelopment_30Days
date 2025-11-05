from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def student():
    student_data = {"name": "Jeelani", "age": 19, "course": "B.Tech - IT"}
    return render_template('student.html', student=student_data)
if __name__ == '__main__':
    app.run()
