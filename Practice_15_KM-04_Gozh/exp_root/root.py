def root2(n):
    return n ** 0.5

def root3(n):
    a = 0
    if n < 0:
        a = -((-n)**(1/3))
    else:
        a = n**(1/3)
    return a