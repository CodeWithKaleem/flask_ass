from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/home')
def Hello_world():
    return f'Hello World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5002')