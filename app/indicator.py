try:
    import RPi.GPIO as GPIO
    import time
except Exception:
    pass


class LedIndicator:
    def __init__(self, port):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.port = port
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(self.port, GPIO.LOW)

    def blink(self, timeOn=1, timeOff=0.5, n=1):
        for i in range(n):
            GPIO.output(self.port, GPIO.HIGH)
            time.sleep(timeOn)
            GPIO.output(self.port, GPIO.LOW)
            if i != n-1:
                time.sleep(timeOff)

    def on(self):
        GPIO.output(self.port, GPIO.HIGH)

    def off(self):
        GPIO.output(self.port, GPIO.LOW)
