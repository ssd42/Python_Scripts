import pandas as pd
import matplotlib.pyplot as pyplot
import numpy as  np

#Series
s = pd.Series([1,3,5,np.nan,6,8])
print(s , end=2*'\n')

#Data frame
dates = pd.date_range('20161205', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates,columns=list('ABCD'))
#print(df)
df.tail(3)


#You can make a data frame passing it a dictionary
adic = {'A': 1.,
		'B': pd.Timestamp('20161205'),
		'C': np.array([3] * 4, dtype='int32'),
		'D': pd.Categorical(["test", "train", "test", "train"]), 
		'E': 'foo'
		}

df2 = pd.DataFrame(adic)
print(df2)

"""
def main():
	print("Libraries imported")


if __name__ == '__main__':
	main()
"""
