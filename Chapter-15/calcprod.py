#! python3
# calcprod.py - measures how long it takes for your computer to count up to 100,000

import time

def calcProd(): #creates a function
	#calculate the product of the first 100,000 numbers
	product = 1
	for i in range(1, 100000):
		product = product + 1
	return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('How long does it take for your computer to count up to 100,000?')
print('It took %s seconds to calculate!' % (endTime - startTime))
