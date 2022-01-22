def check_prime(N):
    for i in range(2, N):
        if N%i==0:
            return 0
    return 1

N = 10001

i = 0

test = 2

while True:
    if check_prime(test)==1:
        i+=1
        print(i, ": ", test)
        if (i==N):
            break
    test +=1
