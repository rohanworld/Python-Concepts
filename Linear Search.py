#Linear Search
#To find an element from a list without using inbuilt functions
arr = [2,3,4,6,8,7,92,54,78,9,26,34,10]
num = 2


#The below is While Loop
# pos = -1
# def search(list, n):
#     i = 0
#     while i < len(list):
#         globals() ['pos'] = i
#         if list[i] == n:
#             return True
#         i = i+1        

# if search(arr, num):
#     print("Found.. at ", pos+1)
# else:
#     print("Not Found..")


#The below is For Loop
pos = -1
def search(list, n):
    i = 0
    for i in range(len(list)):
        globals() ['pos'] = i
        if list[i] == n:
            return True

if search(arr, num):
    print("Found.. at ", pos+1)
else:
    print("Not Found..")