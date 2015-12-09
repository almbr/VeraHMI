#!/usr/bin/env python

from src.GUI import GUI
import sys, threading, time, thread, os


def initClasses():
	if sys.platform == "linux2":
		# SpeedHandler
		from src.SpeedHandler import SpeedHandler
		speedHandler = SpeedHandler(environment)
		speedHandler.start()

		# ButtonHandler
		from src.ButtonHandler import ButtonHandler
		buttonHandler = ButtonHandler(environment)
		buttonHandler.start()

		# GPSHandler
		from src.GPSHandler import GPSHandler
		gpsHandler = GPSHandler(environment)
		gpsHandler.start()

	# ECUHandler
	from src.ECUHandler import ECUHandler
	ecuHandler = ECUHandler(environment)
	ecuHandler.start()


try:
	# Environment
	if sys.platform == "linux2":
		from src.Environment import Environment
		environment = Environment()
		environment.start()
	else:
		from src.EmptyEnvironment import Environment
		environment = Environment()

	gui = GUI(environment)

	thread.start_new_thread(initClasses, ())

	#Start gui and enter its mainloop
	gui.start()
	
except (KeyboardInterrupt, SystemExit):
	print("Exiting...")
	sys.exit()



