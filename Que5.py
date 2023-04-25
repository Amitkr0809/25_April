"""
given two integers M and N write a program to print a solid rectangle pattern of rows and N column using the asterisk character(*)
Input:
2
3
output
* * *
* * *     """

m = int(input("enter Number of row "))
n = int(input("enter Number of column "))

for i in range(1, n):
    for j in range(1, m):
        print(n * "*", end="")
    print()
