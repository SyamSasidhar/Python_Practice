
def Say_Hello_World_With_Python():
    if __name__ == '__main__':
        print("Hello, World!")

def Python_If_Else():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    if __name__ == '__main__':
        n = int(input().strip())
        if n%2==1:
            print("Weird")
        else:
            if n>=2 and n<=5:
                print("Not Weird")
            elif n>=6 and n<=20:
                print("Weird")
            elif n>20:
                print("Not Weird")

def Arithmetic_Operators():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        c = a+b
        d = a-b
        e = a*b
        print(c)
        print(d)
        print(e)

def Python_Divison():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        c = a//b
        d = a/b
        print(c)
        print(d)

def Loops():
    if __name__ == '__main__':
        n = int(input())
        for i in range(0, n):
            print(i * i)

def Write_Function_for_Leap_year():
    def is_leap(year):
        leap = False
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True

        return leap


    year = int(input())
    print(is_leap(year))

def Print_Function():
    if __name__ == '__main__':
        n = int(input())
        for i in range(1, n + 1):
            print(i, end="")

def Find_the_Runner_Up_Score():
    if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
        arr = list(arr)
        arr.sort()
        n-=1
        while n>0:
            if arr[n]!=arr[n-1]:
                print(arr[n-1])
                break
            else:
                n-=1

def Collections_OrderedDict():
    n = int(input())
    d1 = {}
    for i in range(n):
        s = input()
        v = int(s.split()[-1])
        k = s.rsplit(' ', 1)[0]
        d1[k] = v + d1.get(k, 0)
    for k, v in d1.items():
        print(k, v)

def Reduce_Function():
    from fractions import Fraction
    from functools import reduce

    def product(fracs):
        t = reduce(lambda x, y: x * y, fracs)  # complete this line with a reduce statement
        return t.numerator, t.denominator

    if __name__ == '__main__':
        fracs = []
        for _ in range(int(input())):
            fracs.append(Fraction(*map(int, input().split())))
        result = product(fracs)
        print(*result)






# Say_Hello_World_With_Python()
# Python_If_Else()
# Arithmetic_Operators()
# Python_Divison()
# Loops()
# Write_Function_for_Leap_year()
# Print_Function()
# Find_the_Runner_Up_Score()
# Collections_OrderedDict()
# Reduce_Function()