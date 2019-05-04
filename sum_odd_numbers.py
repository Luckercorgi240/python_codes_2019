def pan1(n):
	sum = 0
	for x in range(1, n, 2):
		sum = sum + x
	print(sum)

def pan2(n):
	sum = 0
	for x in range(n):
		if x % 2 == 1:
			sum = sum + x
		else:
			pass
	print(sum)


def pan3(n):
	sum = 0
	step = 1
	while step < n:
		sum = sum + step
		step = step + 2
	print(sum)

def pan4(n):
	print(sum(range(1, n, 2)))


function = input('Which function do you want to use? (pan1, pan2, or pan3, pan4)   ')
number = input('What number do you want the function to do to?   ')
number = int(number)
if function == 'pan1':
    pan1(number)
elif function == 'pan2':
    pan2(number)
elif function == 'pan3':
    pan3(number)
elif function == 'pan4':
    pan4(number)