def mersenne(a):
    b = a + 1
    c = 1
    d = 2
    
    while b < c:
        c = 2*c
    if b == c:
        while (a/d) != int(a/d) and d < a:
            d = d + 1
        if d == a:
            return True
        else:
            return False
    else:
        return False
        

y = 0
z = 2
x = input(print("How many perfect numbers do you want printed?" ))

x = int(x)
while y < x:
    if mersenne(z) == True:
        print(z * (z + 1)/2)
        y = y + 1
    else:
        z = z + 1
