from flask import Flask, render_template, url_for, request, Response
from flask import render_template
from LOBOROBOT import LOBOROBOT  # 载入机器人库
import  RPi.GPIO as GPIO
from camera import VideoCamera

car = LOBOROBOT()
global a12
global a13
a12 = 50
a13 = 120
car.set_servo_angle(13,a13)
car.set_servo_angle(12,a12)
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/control', methods=["POST"])
def control():
    global a12
    global a13
    if request.method == "POST":
        model = request.form['model']
        print(model)
        print("%d,,%d" % (a12, a13))
        if model == "stop":
            car.t_stop(1)
            return "stop"
        elif model == "up":
            car.t_up(40,0)
        elif model == "down":
            car.t_down(40,0)
        elif model == "left":
            car.moveLeft(40,0)
        elif model == "right":
            car.moveRight(40,0)
        elif model == "upleft":
            car.forward_Left(40,0)
        elif model == "upright":
            car.forward_Right(40,0)
        elif model == "downleft":
            car.backward_Left(40,0)
        elif model == "downright":
            car.backward_Right(40,0)
        elif model == "cleft":
            car.turnLeft(40,0)
        elif model == "cright":
            car.turnRight(40,0)
        elif model == "ydown":
            if a12 + 10 >10 and a12 + 10<120:
                a12 = a12 + 10
            car.set_servo_angle(12,a12)
        elif model == "yup":
            if a12 - 10 >10 and a12 - 10<120:
                a12 = a12 - 10
            car.set_servo_angle(12,a12)
        elif model == "yleft":
            if a13 + 10 >10 and a13 + 10<200:
                a13 = a13 + 10
            car.set_servo_angle(13,a13)
        elif model == "yright":
            if a13 - 10 >10 and a13 - 10<200:
                a13 = a13 - 10
            car.set_servo_angle(13,a13)
    return "ok"
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
 
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)