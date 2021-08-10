#Selection Sort: taking minimum value and keepin aside and moving to next to continue
nums = [2,15674,2564326874,546783654,135643674,4,8,9,7,6,1,3,5]

def linsort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        print("After every iteration it looks like: ",list)

print("Before sorting : ", nums)
print()
linsort(nums)
print()
print("After sorting correctly : ",nums)