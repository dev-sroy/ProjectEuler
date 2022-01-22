import math

N = 20

#List all primes below N
def check_prime(N):
    for i in range(2, N):
        if N%i==0:
            return 0
    return 1

primes = []

for i in range(2, N):
    if check_prime(i):
        primes.append(i)

#Find highest power of primes smaller than or equal to N
power_primes = [x**math.floor(math.log(N, x)) for x in primes]

#Take the product of all these numbers
lcm = math.prod(power_primes)

print(lcm)

