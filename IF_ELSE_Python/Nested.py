num = int(input("Enter the number :-"))
if(num<0):
    print("The number is Negative")
elif(num>0):
    if(num<=10):
        print("Number is layes between 1 to 10")
    elif(num<10 and num<=20):
        print("number layes between 11 to 20")
    else:
        print("number is layes between 21 to infinite")
else:
    print("The number is  positie ")
print("I am Heppy")