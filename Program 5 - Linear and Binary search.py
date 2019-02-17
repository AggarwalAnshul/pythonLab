"""Program for linear search"""

def linear(lis, value):
    if find in lis:
        print('element found at position: ',lis.index(find)+1)
    else:
        print('element not found!')

def binary(lis, value):
    lis.sort()
    ans = binarySearch(0,len(lis)-1,lis,value)
    print(lis)
    if(ans == -1):
        print('element not found')
    else:
        print('element found at position: ',ans)

def binarySearch(left, right, lis, value):
    if left <= right:
        middle = int((left + right)/2)
        if lis[middle] == value:
            return middle+1
        elif lis[middle] > value:
            return binarySearch(left, middle-1, lis, value)
        else:
            return binarySearch(middle+1, right, lis, value)
    else:
        return -1


lis = list(map(int, input("Enter the elements of list \n>> ").split()))
find = int(input('Enter the element to find the element in list \n>> '))
choice = int( input('perfrom\n1.Linear Search \n2.Binary search\n>> '))
if choice==1:
    linear(lis, find)
else:
    binary(lis, find)



