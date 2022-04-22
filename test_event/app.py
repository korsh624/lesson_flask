
from flask import Flask, render_template, Response, request, redirect, url_for
servo=90
app = Flask(__name__)
@app.route('/')
def json():
    return render_template('json.html',servo=servo)
#background process happening without any refreshing
@app.route('/forvard')
def forvard():
    global servo
    servo=servo+1
    print(servo)
    return ("nothing")

@app.route('/resvard')
def resvard():
    global servo
    servo=servo-1
    print(servo)
    return ("nothing")
if __name__ == '__main__':
    app.run()