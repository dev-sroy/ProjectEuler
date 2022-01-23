# Generate the Fibonacci sequence whose values do not exceed N = 4 million

def fibonacci(N):
    terms = []

    term1 = 1
    term2 = 2

    term3 = 0

    terms.append(term1)
    terms.append(term2)

    while True:
        term3 = term1 + term2
        term1 = term2
        term2 = term3
        if term3<N:
            terms.append(term3)
        else:
            break
    
    return terms

def sumeven(list):
    S = 0
    for element in list:
        if element%2==0:
            S += element
    
    return S

if __name__=='__main__':

    N = 4e6

    series = fibonacci(N)
    S = sumeven(series)

    print(series)
    print(S)