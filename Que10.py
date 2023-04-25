"""  given a number n,write a program that reads n numbers as input and prints the product of the given n numbers.
input:
	n=3
	2
	3
	7
output:
 	2*3*7=42  """

n = int(input("enter number : "))
count = 0
out = 1
while count < 3:
    num = int(input("enter number"))
    count += 1
    out = num *out
print(out)