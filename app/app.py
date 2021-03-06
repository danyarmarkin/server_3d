'''
	Raspberry Pi GPIO Status and Control
'''
try:
	import RPi.GPIO as GPIO
	from flask import Flask, render_template, request
except Exception:
	pass
from indicator import *

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define sensors GPIOs
button = 20
senPIR = 16

#define actuators GPIOs
ledRed = 13
ledYlw = 19
ledGrn = 26

#initialize GPIO status variables
buttonSts = 0
senPIRSts = 0
ledRedSts = 0
ledYlwSts = 0
ledGrnSts = 0

red = LedIndicator(18)
	
@app.route("/")
def index():
	templateData = {
      'progress'  : 25,
      'nowProgram'  : "none",
      'workStatus'  : "in work",
      'steps'  : "64000",
      }
	return render_template('index.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'turn_left':
		print("turned left for " + action + " steps")
		red.blink(0.5, 0.3, 2)
	if deviceName == 'turn_right':
		print("turned right for " + action + " steps")
		red.blink(0.5, 0.3, 1)
	if deviceName == 'ledGrn':
		actuator = ledGrn

   
	templateData = {
	  'progress'  : 25,
      'nowProgram'  : deviceName,
      'workStatus'  : "in work",
      'steps'  : "64000",
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
