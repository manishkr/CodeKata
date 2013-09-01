#!/usr/bin/python3
"""
Problem : http://codekata.pragprog.com/2007/01/kata_four_data_.html
"""
import sys
"""from enum import Enum"""

class DataOption:
	 Weather = "weather" 
	 FootBall = "football"

def isInt(str):
	try:
		val = int(str)
		return True
	except ValueError:
		return False

def getFloatVal(str):
	try:
		val = float(str)
		return val
	except ValueError:
		return 0.0
	
class Data:
	def __init__(self, type, name, maxVal, minVal):
		self.Type = type
		self.Name = name
		self.MaxVal = getFloatVal(maxVal)
		self.MinVal = getFloatVal(minVal)

	def diff(self):
		return self.MaxVal - self.MinVal
	
class FileHandler:
	def __init__(self, fileName, option):
		self.FileName = fileName
		self.Option = option
		if(self.Option == DataOption.Weather):
			self.NameCol= 0
			self.MaxCol = 1
			self.MinCol = 2
		elif(self.Option == DataOption.FootBall):
			self.NameCol = 1
			self.MaxCol = 6
			self.MinCol = 8
		else:
			assert(False)
			self.NameCol = 0
			self.MaxCol = 0
			self.MinCol = 0
	
	def perform(self):
		dataList = []
		
		with open(self.FileName) as oFile:
			for line in oFile:
				words = line.split()
				if(len(words) > self.MinCol):
					if(True == isInt(words[0].strip("."))):
						data = Data(self.Option, words[self.NameCol], words[self.MaxCol].strip("*"), words[self.MinCol].strip("*"))
						dataList.append(data)
		
		if(len(dataList) > 0):
			maxObj = min(dataList, key = lambda x : x.diff())
			
			if(self.Option == DataOption.Weather):
				print("Day on which temperature had minimum spread : ", maxObj.Name)
			elif(self.Option == DataOption.FootBall):
				print("Team which goal difference was minimum :", maxObj.Name)
		
if __name__ == '__main__':
	if(len(sys.argv) == 3):
		if(sys.argv[2].lower() == DataOption.Weather or sys.argv[2].lower() == DataOption.FootBall):
			fileHandler = FileHandler(sys.argv[1], sys.argv[2])
			fileHandler.perform()
		else:
			print("wrong option, please enter weather or football")
	else:
		print("Please give file name and option(weather/football) about file type")
