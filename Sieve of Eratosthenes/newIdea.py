import sys
from datetime import datetime
from datetime import timedelta
"""
Basically find prime numbers in a select interval
Use of lambda might be better
"""
def findPrime(first, second):
	if  (first < 2 or first >= second):
		print("Second value is greater than the first ")
		print("Or initial value is to low (as in ) < 2 ")
		raise ArithmeticError()
		exit(1)

	primeNums = list(range(first, second))
	divisors = range(2,8)
	#not needed

	"""
	used to use for loop between 2 and the second
	(look at divisor) but changing to the while loop
	changes the time of find prime numbers in a list of 10k
	from ~= 3.5 seconds to ~= 0.5 of a second improving time 
	greatly for even larger values


	Example of the efficiency between the difference
	=======================================
	=   N	=	while	=     for	  	  =
	=======================================
	=  90k	=  23.89 sec= 4 mins 25.66 sec=
	=======================================
	"""
	incr = 0
	while (len(primeNums) > incr+1):
		#print("Current length:{} and current incr:{}".format(len(primeNums), incr))
		i = primeNums[incr]
		primeNums = list(filter(lambda x: x==i or x % i, primeNums))
		incr+=1
		# took a while, in python 3 'filter' no longer returns a list, its an iterable object,
		# just convert it and it should work out

	#[print(pNum, end = " ") for pNum in primeNums]
	#print("\n")


def testTime(one, two):
	now = datetime.now()
	#for _ in range(50):
	findPrime(one, two)
	return(datetime.now() - now)


timelist = []
def average(one, two, looptimes):
	for i in range(looptimes):
		timelist.append(testTime(one, two))

	returnVal = sum(timelist, timedelta())/len(timelist)
	print("Average time with {} loops: {}".format(looptimes, returnVal))

def main():
	# first argument is filename so want 3
	no_arguments = False

	if(len(sys.argv) != 3 and not no_arguments):
		print("Expected 2 arguments to be passe, this wasn't the case exiting...")
		exit(1)
	try:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
	except IndexError:		
		print("IndexError: ")
		if(no_arguments == False):
			print("Could not convert one of the values to an integer")
			exit(1)

	
	#findPrime(start, end)
	#testTime(start, end	)
	
	average(start, end, 1)
	#average(start, end, 10)
	#average(start, end, 50)
	#average(start, end, 100)

if __name__ == '__main__':
	main()