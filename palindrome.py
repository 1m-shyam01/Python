num1=int(input("Enter the number : "))
x=num1
res=0
while x>0:
    rem=x%10
    res=res*10+rem
    x=x//10
if(res==num1):
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")