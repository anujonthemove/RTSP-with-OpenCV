'''
Python class to demonstrate Exception handling with RTSP feeds.
'''
import numpy as np
import os
import sched, datetime
import errno
import socket
from socket import error as socket_error
import cv2
import time
import re
from urlparse import urlparse
import sys
from datetime import datetime


allowed_file_extensions = ['.mpg', '.webm', '.mp4', '.mkv', '.avi']

class RTSPExceptionHandling(object):

	def __init__(self, video_path=''):

		# video_path = video_path.strip()
		self.__is_rtsp = False
		self.__is_video = False
		self.__is_camera = False

		if video_path == ''  or video_path == ' ':
			print("Please provide some value")
			sys.exit(0)

		elif type(video_path) == int:
			print("== Using locally connected camera ==")
			self.__video_name = "camera_location"
			self.__is_camera = True

		elif type(video_path) == str:

			self.__video_name, self.__file_extension = os.path.splitext(os.path.basename(video_path))
			
			# print(self.__video_name, self.__file_extension)
			if not self.__file_extension in allowed_file_extensions:
				print("== Invalid video file format, please check! ==")
				sys.exit(0)

			# Regex for checking if the path to video is rtsp
			pattern = re.compile(r'(rtsp://(.*))(\?.*)?')
			match = pattern.match(video_path)

			
			
			if match:
				self.__rtsp_url = urlparse(video_path)
				self.__is_video = False
				self.__is_rtsp = True
				print("== Using RTSP feed ==")

			else:
				if not os.path.exists(video_path):
					print("\nVideo file does not exist. Please make sure path and video filename is proper.\n\n***ABORTING***\n")
					sys.exit(0)
				
				self.__video_path = video_path
				self.__is_video = True
				self.__is_rtsp = False
				print("== Using locally stored video file ==")
				

		

	def demo_rtsp_exception_handling(self):

		if self.__is_rtsp:

			urlInfo = self.__rtsp_url
			url = urlInfo.geturl()
			protocol = urlInfo.scheme
			host = urlInfo.hostname
			port = urlInfo.port
			location = urlInfo.netloc
			print(url)
			
			req = "DESCRIBE "+ url +" RTSP/1.0\r\nCSeq: 2\r\n\r\n"

			while True:
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((host, port))
					s.sendall(req)
					data = s.recv(100)
					# print(data)

					cap = cv2.VideoCapture(url)

					if not cap.isOpened():
						raise SystemError('Camera connected but video feed not available.')

					ret, frame = cap.read()
					if not ret:
						raise Exception('Camera connected but incoming images are invalid.')
					
					
				except socket_error as serr:
					print("\nError-1: " + str(serr.args[1]) + ' at time: ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
					time.sleep(2)
					

				except SystemError as error:
					print("\nError-2: " + str(error) + ' at time: ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
					time.sleep(2)
					
				except Exception as e:

					print("\nError-3: " + str(e) + ' at time: ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
					time.sleep(2)
					
		elif self.__is_video:
			print("Running from a video file")
			
			
		elif self.__is_camera:
			name = raw_input('Choose camera channel (0/1/2) ') or 0
			print('Using camera number: ' + str(name))
			