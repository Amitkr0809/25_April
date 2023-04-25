"""  solid right angled Triangle
given an interger number N as input write a program to print the right-angled triangle pattern of n lines using asterisk(*) character.
input: 4
output:
*
* *
* * *
* * * *  """


n = int(input("enter number : "))
for i in range(n+1):
    print(i * "*")