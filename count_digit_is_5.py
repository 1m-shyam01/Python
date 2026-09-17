num1 = int(input("Enter the number : "))
x = num1
count = 0
while x > 0:
    digit=x%10
    if(digit==5):
        count = count+1 
    x = x // 10
print(count)