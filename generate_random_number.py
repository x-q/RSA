import random

def generate(a):
	
	output = 0

	for i in range(a):
		
		c = 10 ** i
		output += c * random.randint(0, 9)

	return output
