num=int(input("Enter a Number : "))
length = len(str(num))
fd=num
s=0
while(num>0):
    d=num%10
    s=s+d**length
    num=num//10
if fd==s:
    print(fd, "is an armstrong number")
else :
    print(fd,"is not a armstrong number")
