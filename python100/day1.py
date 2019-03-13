"""Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""


def printNum():
    ans = []
    for i in range(2000, 3200):
        if i%7 == 0 and i%5 != 0:
            ans.append(str(i))
    print(",".join(ans))

"""Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""



def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)

"""Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

def powerhash(num):
    powerdict = {}
    for i in range(num):
        powerdict[i+1] = (i+1)*(i+1)
    print(powerdict)

"""Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

def strparser(s):
    numlist = s.split(",")
    numtuple = tuple(numlist)
    print(numlist)
    print(numtuple)


"""Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""


class stringhandler(object):
    def __int__(self, s = ""):
        self._s = s


    def getstr(self):
        self._s = input("Enter the string: ")

    def printstr(self):
        print(self._s.upper())


"""Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math

def getQ(numlist):
    ans = []
    for i in numlist:
        D = int(i)
        ans.append(str(int(round(math.sqrt((2*50*D)/30)))))
    print(",".join(ans))


"""uestion 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] """

def array_2d(x, y):
    ans = []
    for i in range(x):
        element = []
        for j in range(y):
            element.append(i*j)
        ans.append(element)
    print(ans)

"""Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

def sort_words(inputstr):
    strlist = inputstr.split(",")
    strlist.sort()
    print(",".join(strlist))

"""Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""

def printpara():
    ans = []
    while 1:
        s = input()
        if s:
            ans.append(s.upper())
        else:
            break
    print("\n".join(ans))


"""Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""

def removeandsort(strlist):
    ans = list(set(strlist))
    ans.sort()
    print(" ".join(ans))
