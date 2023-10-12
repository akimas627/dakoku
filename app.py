from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

# 一番最初のログインページ（index.html）を表示させる
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return render_template('home.html',time = current_time)


if __name__ == '__main__':
    app.run()