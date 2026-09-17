num1=int(input("Enter the number : "))
x=0
y=1
print(x,end=" ")
print(y,end=" ")
for i in range(1,num1+1):
    z=x+y
    print(z,end=" ")
    x=y
    y=z