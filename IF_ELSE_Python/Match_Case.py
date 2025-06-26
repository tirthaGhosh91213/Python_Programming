x=int(input("Enter the number :- "))
match x:
    case 4:
        print("It is case 4")
    case 5:
        print("It is the case 5")
    case _ if x!=40:
        print( x ," is not match")
    case _ if x!=50:
        print(x," is not 60")
    case _ :
        print(x)
