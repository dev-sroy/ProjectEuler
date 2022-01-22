import numpy as np

def check_prime(N):
    for i in range(2, int(np.sqrt(N))):
        if N%i==0:
            return 0
    return 1

def greatest_prime_factor(N):
    factors_list = []
    for i in range(2, int(np.sqrt(N))):
        if N%i==0 and check_prime(i)==1:
            factors_list.append(i)
            if check_prime(N//i)==1:
                factors_list.append(N//i)
            
    return max(factors_list)
print(greatest_prime_factor(600851475143))

