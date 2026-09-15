marks=int(input("Enter your marks : "))
if(marks<60):
    print("You achieve F grade")
elif(marks<70):
    print("You achieve D grade")
elif(marks<80):
    print("You achieve C grade")
elif(marks<90):
    print("You achieve B grade")
elif(marks<=100):
    print("You achieve A grade")
else:
    print("Invalid marks, Choose marks b/w 1-100")