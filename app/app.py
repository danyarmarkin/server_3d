'''
	Raspberry Pi GPIO Status and Control
'''
try:
	import RPi.GPIO as GPIO
	from flask import Flask, render_template, request
except Exception:
	pass
from indicator import *

steps = 64000
work_status = "not in work"
progress = 0

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = LedIndicator(18)
	
@app.route("/")
def index():
	templateData = {
      'progress'  : 25,
      'nowProgram'  : "none",
      'workStatus'  : work_status,
      'steps'  : steps,
      }
	return render_template('index.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	s = ""
	if deviceName == 'turn_left':
		s = "left"
		red.blink(0.5, 0.3, 2)
	if deviceName == 'turn_right':
		s = 'right'
		red.blink(0.5, 0.3, 1)

	for i in range(1, int(action)+1):
		work_status = "in_work"
		templateData = {
			'progress': round(i/int(action)),
			'nowProgram': s,
			'workStatus': work_status,
			'steps': steps,
		}
		print(s, i)
		red.blink(0.5, 0.3, 1)
		render_template('index.html', **templateData)

	work_status = "not in work"
	templateData = {
	  'progress'  : 100,
      'nowProgram'  : "none",
      'workStatus'  : work_status,
      'steps'  : steps,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
