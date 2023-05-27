def leap_year():

    def is_leap(year):
        leap = False
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year%400 == 0:
                    leap = True

        return leap


    year = int(input("Enter a year:"))
    print(is_leap(year))

def print_consecutive_numbers():
    if __name__ == '__main__':
        n = int(input())
        for i in range(1, n+1):
            print(i, end="")

def reduce_function():
    from fractions import Fraction
    from functools import reduce

    def product(fracs):
        t =  reduce(lambda x,y:x/y, fracs)
        return t.numerator, t.denominator

    if __name__ == '__main__':
        fracs = []
        for _ in range(int(input())):
            fracs.append(Fraction(*map(int, input().split())))
        print(fracs)
        result = product(fracs)
        print(*result)


def collections_OrderedDict():

    n = int(input("No of Items: "))
    d1 = {}
    for i in range(n):
        s = input()               # "Banana Fries 12"
        v = int(s.split()[-1])    # 12
        k = s.rsplit(' ', 1)[0]   # 'Banana Fries'
        d1[k] = v + d1.get(k, 0)

    # print(d1)
    for k,v in d1.items():
        print(k,v)

# collections_OrderedDict()

















# leap_year()
# print_consecutive_numbers()
# reduce_function()