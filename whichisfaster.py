import time

def pan(n):
	   total = []
	   for x in range(n):
		# print('%d +' % x, end=' ')
		   total.append(x)
	#    print('The total is %d' % sum(total))


def jianxia(n):
	   sum = 0
	   for x in range(n):
		   sum = sum + x
	   return sum

start = time.time()
pan(50000000)
end = time.time()
print("Pan's code takes %f" % (end - start))


start = time.time()
jianxia(50000000)
end = time.time()
print("Jianxia's code takes %f" % (end - start))