"""Program to find the exponentiation of an element"""

lis = list(map(int, input('enter the number followed by power to calculate exponentiation \n>> ').split()))
ans = lambda a,b: a**b
print(ans(lis[0], lis[1]))

