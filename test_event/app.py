
from flask import Flask, render_template, Response, request, redirect, url_for
servo=90
app = Flask(__name__)
@app.route('/json')
def json():
    return render_template('json.html',servo=servo)
#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    global servo
    servo=servo+1
    print(servo)
    return ("nothing")
if __name__ == '__main__':
    app.run()