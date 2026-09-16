num1=int(input("Enter the value : "))
k=1;
for i in range(1,num1+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k +=1
    print()