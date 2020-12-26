def fact(n):
    if n == 1:
        return 1
    n = n*fact(n-1)
    return n
