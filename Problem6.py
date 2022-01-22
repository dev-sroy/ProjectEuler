N = 101

def sum_squares(N):
    S = 0
    for i in range(1, N):
        S += i**2
    return S

def square_sum(N):
    S = 0
    for i in range(1, N):
        S += i

    return S**2

print(square_sum(N) - sum_squares(N))