distance=int(input("Enter your marks : "))
if(distance<3):
    print("Walk")
elif(distance<16):
    print("Bike")
elif(distance>15):
    print("Car")
else:
    print("Invalid distance, Choose distance again")