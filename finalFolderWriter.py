
import os, sys
firstNumber = input("What are the last three digits of the first 18- folder you're trying to make? ")
lastNumber = input("What are the last three digits of the last 18- folder you're trying to make? " )
subfolderNames = ["Final Versions", "Original Submissions", "Working Files"]
for x in range (int(firstNumber), int(lastNumber) + 1):
	path = ("18-%d" % (x))
	def makemydir(whatever):
		for subfolder_name in subfolderNames:
			os.makedirs(os.path.join(path, subfolder_name))

	makemydir(path)


