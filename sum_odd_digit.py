num1 = int(input("Enter the number : "))
x = num1
sum = 0
while x > 0:
    digit=x%10
    if(digit%2!=0):
        sum = sum+ digit 
    x = x // 10
print(sum)