#Performing Bubble sort --- arrange by swapping
#Easiset sorting method available
nums = [2,4,8,9,7,6,1,3,5]

nums.sort()
print("Using built-in function: ", nums)

def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        print("After every iteration : ",list) 

sort(nums)
print("After sorting manually : ", nums)