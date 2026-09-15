num1=int(input("Enter the value : "))
for i in range(1,num1+1):
    for j in range(1,num1-i+1):
         print(" ",end=" ")
    for k in range(1,i*2):
            print ("*",end=" ")
    print()