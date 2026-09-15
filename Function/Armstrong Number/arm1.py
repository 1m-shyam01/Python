import arm as a
num = int(input("Enter the number : "))
armst=a.armstrong(num)

if armst==num:
    print(num, "is an armstrong number")
else :
    print(num,"is not a armstrong number")
    
