"""N Primary number"""
import math
def isPrime(num):
    limit = int( math.sqrt(num) )
    for x in range(2, limit):
        if num%x == 0:
            return 0
    return 1


limit = int(input('enter how many prime numbers to generate'))
count = 0
nextNum = 2
while(count < limit):
    if ( isPrime(nextNum) == 1):
        count+=1
        print(nextNum)
    nextNum+=1

