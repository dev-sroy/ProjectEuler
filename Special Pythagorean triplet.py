def check_pythagoras(a, b, c):
    return a**2 + b**2 - c**2 == 0

for a in range(1, 1000):
    for b in range(1, 1000-a):
        c = 1000 - a - b

        if check_pythagoras(a, b, c):
            print(a*b*c, a, b, c)
