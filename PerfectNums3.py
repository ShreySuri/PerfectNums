x = int(input(print("How many perfect numbers do you want printed? ")))
y = 0
z = 1
d = 2

while y < x:
    z = 2*z + 1
    while (z/d) != int(z/d) and d < z:
        d = d + 1
    if d == z:
        print(int(z * (z + 1)/2))
        y = y + 1
    d = 2