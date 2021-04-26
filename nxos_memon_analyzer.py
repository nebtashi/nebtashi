
import re
import sys

file_path = sys.argv[1]
used_mem = []
free_mem = []

def get_used_mem (memon):

	file = open(memon, mode='r')
	memon_data = file.readlines()


	for i in range(len(memon_data)): 
		x1 = re.search("total.*used", memon_data[i])
		if x1 != None: 
			x2= x1.group()
			x3= re.search("\d+", x2)
			used_mem.append(x3.group())

