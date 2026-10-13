def fib(num1):
    a=0
    b=1
    print(0,end=" ")
    print(1,end=" ")
    for i in range(0,num1-2):
        z=a+b
        print(z,end=" ")
        a=b
        b=z
