"""Average of the N number

Input:
4
out:
2.5 """

n = int(input("enter number : "))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print("Sum of",n,"Number : ",sum)

Avg = sum/n
print("Average of",n,"Number is ",Avg)