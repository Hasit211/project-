f=open('hasit.txt')
filelines = f.readlines()
for line in filelines:
    print(line)
 #introSring='my,name is hasit ,and i am 15 years, old'
#words=introSring.split(',')
#print(words)
#def greet(name):
 #   print('hello '+name+ '. how are you?')
#greet('hasit')

def countWordsFromFile():
    fileName = input('hasit.txt')
    numberOfWords = 0
    file = open(fileName,'r')
    for line in file:
        word = line.split()
        numberOfWords = numberOfWords+len(word)
    print(numberOfWords)
countWordsFromFile()