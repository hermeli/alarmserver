#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import RPi.GPIO as GPIO
from time import sleep
import smtplib

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering 
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.HIGH)

print "Input states before switching..."
print "Alarm* input: %d" % GPIO.input(4)
print "Enable* input: %d" % GPIO.input(17)
sleep(5)

GPIO.output(27,GPIO.LOW)
sleep(1)
GPIO.output(27,GPIO.HIGH)
sleep(5)

print "Input states after switching..."
print "Alarm* input: %d" % GPIO.input(4)
print "Enable* input: %d" % GPIO.input(17)
