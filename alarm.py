#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import RPi.GPIO as GPIO
from time import sleep
import smtplib

ALARMn = 4
ENABLEDn = 17
TOGGLEn = 27

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering 

""" Connection of Access Manager to Raspberry Pi:
Access Manager 			Raspberry Pi
IN1: alarm contact  		-
IN2: alarm monitor enable	Pin13, GPIO27 (TOGGLEn)
OUT1: alarm out			Pin7, GPIO4 (ALARMn)
OUT2: alarm monitor enabled	Pin11, GPIO17 (ENABLEDn)
OUT3: alarm controller alive	- 

Only ALARMn has to be monitored, others are not important!
"""
GPIO.setup(ALARMn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ENABLEDn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOGGLEn, GPIO.OUT)
GPIO.output(TOGGLEn, GPIO.HIGH)

sender = 'wyss@superspider.net'
receivers = ['wyss@superspider.net','MOBILE@mail.963.ch']
message = """From: Stefan Wyss <wyss@superspider.net>
To: Stefan Wyss <wyss@superspider.net>
Subject: Einbruchalarm

Einbruchalarm! Polizei Faellanden: 0041 44 806 40 60
"""

def sendEmail():
	server = smtplib.SMTP('asmtp.mail.hostpoint.ch', 587)
	server.starttls()
	server.login("wyss@superspider.net", PASSWORD)
	server.sendmail(sender, receivers, message)
	server.quit()

print "Home Alarm Script started..."
while True:
	if not GPIO.input(ALARMn):
		print "Alarm detected. Sending alarm SMS..."
		sendEmail()
		while not GPIO.input(ALARMn):
			sleep(0.1)
		print "Alarm reset..."
	sleep(0.1)
