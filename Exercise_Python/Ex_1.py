import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter the hour"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning sir !!!")
elif(hour>=12 and hour<16):
    print("Good afternoon sir !!!")

if(hour>=16 and hour<=24):
    print("Good evening  sir !!!")
