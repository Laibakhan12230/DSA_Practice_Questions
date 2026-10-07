num = int(input("Enter a number: "))
n = num
temp = 0
while num>0:
    digit = num % 10
    temp = (temp * 10) + digit
    num = num // 10
if temp==n:
     print("Palindrome")
else:
    print("Not a Palindrome")
