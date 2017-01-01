import RPi.GPIO as GPIO
from time import sleep
from flask import Flask, render_template, request
app = Flask(__name__)

ALARMn = 4
ENABLEDn = 17
TOGGLEn = 27
GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   4 : {'name' : 'GPIO 4', 'state' : GPIO.HIGH, 'display' : 'ALARM*'},
   17 : {'name' : 'GPIO 17', 'state' : GPIO.HIGH, 'display' : 'ENABLED*'},
   27 : {'name' : 'GPIO 27', 'state' : GPIO.HIGH, 'display' : 'TOGGLE*'} 
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(TOGGLEn, GPIO.OUT)
GPIO.output(TOGGLEn, GPIO.HIGH)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "toggle" execute the code indented below:
   if action == "toggle":
     GPIO.output(changePin,GPIO.LOW)
     sleep(1)
     GPIO.output(changePin,GPIO.HIGH)
     message = "Toggled " + deviceName

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
