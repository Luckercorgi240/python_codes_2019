import sys
def loop(n):
    number = 0
    for x in range(n):
        number = number + x
        print(number)

loop(int(sys.argv[1]))