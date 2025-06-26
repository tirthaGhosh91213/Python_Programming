# Defalt argument
def average(a=6,b=1):
  print("the average of the sum is = ",(a+b)/2)

average(b=4)

# KeyWard arguments dont flow the order 
average(b=3,a=1)

# Required argument :- in case we dont pass the argument with a key= value syntax thenit is nessary to pass the argument in the currect positional order and the number of arguments pass shuld match the actual function definition 
def avg3(a,b,c=2):
  print("The Average of the sum is = ",(a+b+c)/3)

avg3(3,4)

# Keyward arbitary arguments
def avg(*number):
  sum=0
  for i in number:
    sum = sum +i
  return sum/len(number)

c = avg(3,4,5,8,9)
print("Average is =",c)