import time
x= int(input("Enter a Number for a box:\n"))
for i in range(x):
    for j in range(x):
        print("# ", end='')
    print()
print("*******")
y= int(input("Enter a Number for Right Triangle:\n"))
for i in range(y):
    for j in range(i+1):
        print("# ", end='')
    print()
print("*******")
z= int(input("Enter a Number for reverse Right Triangle:\n"))
for i in range(z):
    for j in range(x-i):
        print("# ", end='')
    print()
print("*******")
n = int(input("Enter a number for Triangle: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    print("\n", end="")
print("*******")
num = int(input("Enter the number for tables:\n"))
for i in range(10):
    print(f"{num}X{i+1}={num*(i+1)}")
time.sleep(5)




        
