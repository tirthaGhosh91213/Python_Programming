# Strings are immutable ..... ak bar lakha hoia gala  ar change kor ajai na change korte gala new string a change kore 
name="!!! tirtha!!!tirtha tirtha !!!"
print(len(name))
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.replace("tirtha","Ghosh"))
print(name.split(" "))
blogHeading="introduction oF jS"
print(blogHeading.capitalize())
str="Welcome to the console!!!"
print(str.center(60))
print(name.count("tirtha"))
print(str.endswith("!!!"))       #And we can also use endswith
print(str.endswith("to",4,10))
str="He's name is don , he is a goood boy "
print(str.find("is"))
# If there is no "is " in the string thern the compiler shows -1 .
print(str.index("is"))
# If there is no "is " in the string thern the compiler shows Error . 
str="welcomeToTheConsole"
print(str.isalnum())
# The isalnum() function method return true only if entire string only consists of A-Z and 0-9. 
print(str.isalpha())
# The isalnum() function method return true only if entire string only consists of A-Z and  a-z .
str="hey tirtha"
print(str.islower())
print(str.isprintable())
# Ex:- not printable \n
str="     "      #using spacebar
print(str.isspace())
str="       "       #using Tab
print(str.isspace())
str="World Helth Organization"
print(str.istitle())
str1="To kill a moking bird"
print(str1.istitle())
print(str1.swapcase())
print(str1.title())
