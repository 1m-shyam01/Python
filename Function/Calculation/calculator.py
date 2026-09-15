def sum(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2

def calc(num1, num2,choice):
   while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Exit")


    if choice==1:
        print("Addition is : ",num1+num2)
    elif choice==2:
        if num1<num2:
             print("Num1 is lesser than Num2")
        else:
            print("subtraction is : ",num1-num2)
    elif choice==3:
        print("Multiplcation is : ",num1*num2)
    elif choice==4:
        if num2==0:
            print("Not Divisible")
        else:
            print("Division is : ",num1/num2)
    elif choice==5:
        if num2==0:
            print("Can not found Modulus")
        else:
            print("Modulus is : ",num1%num2)
    elif choice==6:
        if num2==0:
            print("Can not found Floor Division")
        else:
            print("FloorDivision is : ",num1//num2)
    elif choice==7:
        break
