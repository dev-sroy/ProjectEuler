N = 1000

S=0

for i in range(N):
    if i%3==0 or i%5==0:
        S += i

print(S)