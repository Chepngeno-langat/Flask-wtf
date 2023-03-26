from flask import Flask, render_template, request, redirect, url_for
from forms import CourseForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ab8aec9165e8ba37f041564c'


@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    #name = request.form['name']
    # enrolment_num = request.form['enrolment_num']
    # email = request.form['email']
    # course_rating = request.form['course_review']
    # course_review = request.form['course_rating']
    # if request.method == 'POST':
    #     with open('course_output', 'w') as text:
    #         text.write(str(name))
    #         text.write(str(enrolment_num))
    #         text.write(str(email))
    #         text.write(str(course_rating))
    #         text.write(str(course_review))
    return render_template('index.html', form=form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
