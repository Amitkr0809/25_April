"""     Read N inputs
the first line of input will contain a positive integer, N
the following N lines contain an integer in each line.
input: 3
	 8
	 11
	 25
output:
8
11
25     """

n = int(input("enter number : "))
count = 0
while count < 3:
    num = int(input("enter number"))
    count = count + 1
    print(num)
