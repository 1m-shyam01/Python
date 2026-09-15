age=int(input("Enter the age : "))
day=str(input("Enter the Day Name : "))
price = 12 if age >=18 else 8
if(day== "Wednesday"):
    price-=2
    print("Ticket pricd is $",price)
else:
    print("Ticket price is $",price)