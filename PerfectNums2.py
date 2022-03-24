def mersenne(a):
    b = a + 1
    c = 1
    d = 2
    
    while c < b:
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
    z = z + 1
    if mersenne(z) == True:
        print(int(z * (z + 1)/2))
        y = y + 1

