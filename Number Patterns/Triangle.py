num1=int(input("Enter the value : "))
for i in range(1,num1+1):
    for j in range(1,num1-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()