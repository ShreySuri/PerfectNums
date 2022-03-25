import math


def prime(a):
   b = int(math.sqrt(a)) + 1
   c = 2
   while (a/c) != int(a/c) and c < b:
       c = c + 1
   if c == b:
       return True
   else:
       return False
   
 

x = int(input(print("How many perfect numbers do you want printed? ")))
y = 0
z = 1


while y < x:
    z = 2*z + 1
    if prime(z) == True:
        print(int(z * (z + 1)/2))
        y = y + 1
