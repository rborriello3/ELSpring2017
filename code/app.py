from flask import Flask, render_template, request, redirect
import Adafruit_PCA9685
import time
import os, shutil
from picamera import PiCamera

app = Flask(__name__, static_url_path='/static')
app.config['PROPAGATE_EXCEPTIONS'] = True
pwm1 = Adafruit_PCA9685.PCA9685(0X40)
pwm2 = Adafruit_PCA9685.PCA9685(0x40)
pwm1.set_pwm_freq(50)
pwm2.set_pwm_freq(50)
camera = PiCamera()
count = 0

@app.route('/')
def controls():
        templateData = {
                'title': 'PiCamera'
        }
        return render_template('PiCam.html', **templateData)

@app.route('/up', methods=['GET'])
def moveUp():
        global servoPosition
        global pwm1
        pwm1.set_pwm(0, 0, 12)
        time.sleep(0.02)
        pwm1.set_pwm(0, 0, 0)
        return render_template('PiCam.html')

@app.route('/down', methods=['GET'])
def moveDown():
        global servoPosition
        global pwm1
        pwm1.set_pwm(0, 0, 475)
        time.sleep(0.1)
        pwm1.set_pwm(0, 0, 0)
        return render_template('PiCam.html')

@app.route('/right', methods=['GET'])
def moveRight():
        global pwm2
        pwm2.set_pwm(1, 0, 12)
        time.sleep(0.02)
        pwm2.set_pwm(1, 0, 0)
        return render_template('PiCam.html')

@app.route('/left', methods=['GET'])
def moveLeft():
        global pwm2
        pwm2.set_pwm(1, 0, 475)
        time.sleep(0.1)
        pwm2.set_pwm(1, 0, 0)
        return render_template('PiCam.html')

@app.route('/takePicture', methods=['GET'])
def takePicture():
        if os.path.exists('static'):
                shutil.rmtree('static')
        os.makedirs('static')
        time.sleep(2)
        camera.capture('static/image.jpg')
        templateData = {

                'title': 'PiCamera'
        }
        return render_template('PiCam.html', **templateData)

if __name__ == "__main__":
        app.jinja_env.auto_reload = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.run('137.140.183.121', port=3000)
