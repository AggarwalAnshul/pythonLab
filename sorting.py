#bubble sort
'''
def bubble(arr,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:#if left value is greater than right
                arr[j],arr[j+1]=arr[j+1],arr[j]#swap

    print("sorted array : ")
    for a in arr:
        print( a,end=" ")

def sort():
    arr=[int(x) for x in input("enter value : ").split(",")]#user input
    n=len(arr)
    bubble(arr,n)
'''
#selection
'''
def indexofmin(arr, start, n):
    Min = arr[start]
    index = start
    for x in range(start+1, n):
        if(arr[x]<Min):
            Min=arr[x]
            index = x 
    return index
def selection(arr,n):
    for i in range(n): #n-1
        index=indexofmin(arr, i, n) #array, current , size
        arr[i],arr[index]=arr[index],arr[i]#swap
def sort():
    arr=[int(x) for x in input("enter value : ").split(",")]#user input
    n=len(arr)
    selection(arr,n)
    print("sorted array : ",arr)
'''

#insertion
'''
def insert(arr,n):
    for i in range(1,n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    print(" sorted array : ",arr)
def sort():
    arr=[int(x) for x in input("enter value : ").split(",")]#user input
    n=len(arr)
    insert(arr,n)
'''
#merge
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j] 
                j+=1
            k+=1
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1
            
            
def sort():
    arr=[int(x) for x in input("enter value : ").split(",")]#user input
    n=len(arr)
    mergeSort(arr)
    print("sorted array : ",arr)
sort()














    
    
