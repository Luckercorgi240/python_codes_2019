wasd = input('Enter the path of your file')
file = open(wasd)
string = file.read()
d = {}
for c in string:
    d[c] = string.count(c)
for k in d:
    print(k, end = ' ')
    print(d.get(k))