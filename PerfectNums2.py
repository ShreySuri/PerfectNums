def mersenne(a):
    b = a + 1
    c = 1
    while b < c:
        c = 2c
    if b == c:
        
    else:
        return False
        
   



x = input(print("How many perfect numbers do you want printed?"))
x = int(x)
y = 2
for i in range (0,x):
    z = 2 ** y - 1
    for i in range (0,z):
        if 