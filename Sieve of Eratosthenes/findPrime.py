import sys
from datetime import datetime
"""
Basically find prime numbers in a select interval
Use of lambda might be better
"""
def findPrime(first, second):
	if  (first < 2 or first >= second):
		print("Second value is greater than the first ")
		raise ArithmeticError()
		exit(1)

	primeNums = list(range(first, second))
	divisors = range(2,8)

	# now use the lambda to save on the if else
	# and generate the prime numbers

	"""
	its not working with large values such as second=1000
	I don't like this second though, although it might optimize it 
	"""
	for i in range(2, second):
		primeNums = list(filter(lambda x: x==i or x % i, primeNums))
		# took a while, in python 3 filter no longer returns a list, its an iterable object,
		# just convert it and it should work out
	[print(pNum, end = " ") for pNum in primeNums]
	print("\n")
	

def testTime(one, two):
	now = datetime.now()
	findPrime(one, two)
	print(datetime.now() - now)



def main():
	# first argument is filename so want 3
	if(len(sys.argv) != 3):
		print("Expected 2 arguments to be passe, this wasn't the case exiting...")
		exit(1)
	try:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
	except ValueError:
		print("Could not convert one of the values to an integer")
		exit(1)

	#findPrime(start, end)
	testTime(start, end	)


if __name__ == '__main__':
	main()