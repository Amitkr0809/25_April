"""write a program that reads n number and print the cube of N number from 1
input;
4
output:
1
8
27
64"""

n = int(input("enter number : "))
cube= 0
for i in range(1,n+1):
    cube = i*i*i
    print(cube)