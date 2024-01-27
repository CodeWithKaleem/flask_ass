from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def show_form():
    return render_template('index.html')

@app.route('/details', methods = ['POST'])
def display_details():
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    dob = request.form.get('dob')
    return f'First name = {first_name} Last name = {last_name} email = {email} Date of birth = {dob}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')