from flask import Flask 
app = Flask(__name__)

@app.route('/')
def show_text():
    return f'Work is not done.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')