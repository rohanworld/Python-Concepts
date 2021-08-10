#Binary Search
#the list has to be sorted

pos = -1
def search(list, n):
    l=0
    u=len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False


arr = [2, 3, 4, 6, 8, 7, 92, 36, 98, 7, 25, 89]
num = 36

print("Program Running..")
if search(arr, num):
    print("Found.. at ", pos+1)
else:
    print("Not Found..")