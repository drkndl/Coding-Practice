#Heads up, this program is painfully slow

import numpy as np 
arr = np.arange(20,1000000,1)
print(arr)
#Took the array from 20 cuz there's no way the first 20 numbers have the longest Collatz sequence

def collatz(elem):
	count=0
	while elem>=16: #Took it till 16 cuz after that it's just 8,4,2,1 for all numbers
		if elem%2==0:
			elem=elem/2
			count+=1
		else:
			elem=3*elem+1
			count+=1
		if elem==1:
			break
	return count

num_dict={}

for elem in arr:
	count = collatz(elem)
	num_dict[elem]=count

Keymax = max(num_dict, key=num_dict.get) 
print(Keymax) 
	