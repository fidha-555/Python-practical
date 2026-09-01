from functools import reduce
nums =[1,3,5,7,9]
total = reduce(lambda x,y : x+y , nums)
print(total)