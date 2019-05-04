your_file = input('Please enter the path of your file    ')
with open(your_file) as infile:
    lines=0
    words=0
    characters=0
    for line in infile:
        wordslist=line.split()
        lines=lines+1
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)
print('There are %d lines in your file' % lines)
print('There are %d words in your file' % words)
print('There are %d characters in your file' % characters)