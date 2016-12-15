#Lets try a quick sort

# Selection Sort

import random

l = list(range(1,101))
random.shuffle(l)

def selection(randList):
	for i in range(len(randList)):
		minimum = i
		for k in range(i+1, len(randList)):
			if randList[k] < randList[minimum]:
				minimum = k
		swap(randList, minimum, i)


def 


def swap(A, x, y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp

[print(val, end= ' ') for val in l]
selection(l)

print("\n\nRunning Selection Sort\n")
[print(val, end= ' ') for val in l]