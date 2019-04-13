def fib(n):
    first = 0
    second = 1
    third = first + second
    step = 0
    print(first, second, end = ' ')
    while third < n:
        print(third, end = ' ')
        first = second
        second = third
        third = first + second

x = int(input('What number do you want to stop at?\n'))
fib(x)