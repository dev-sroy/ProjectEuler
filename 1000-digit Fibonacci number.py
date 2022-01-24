from unicodedata import digit
import numpy as np

def fibonacci(n):
    phi = (1 + np.sqrt(5))/2.0

    logFn = (n * np.log10(phi) - np.log10(5)/2)

    return np.floor(logFn) + 1

n = 0
digits = []

while True:
    num_digits = fibonacci(n)

    if num_digits<3:
        n += 1
    else:
        break

print(n)

