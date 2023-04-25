"""   write a program that reads two numbers M and N and prints the sum of N numbers from M
input
7
3
output:
24   """

m = int(input("enter number "))
n = int(input("enter number "))
sum = 0
for i in range(m,m+n):
    sum = sum+i
print(sum)

