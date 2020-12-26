from exp_root import exponentiation
from exp_root import root
from factorial import factorial
from logarithm import logarithm
def main():
    while True:
        func = input('''Choose function to use:
        fact
        log
        lg
        ln
        exp2
        exp3
        root2
        root3''')
        if func == 'fact':
            while True:
                n = input('input integer over 0 to get factorial')
                try:
                    n = int(n)
                    if n < 1:
                        raise ValueError
                    print(factorial.fact(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'log':
            while True:
                n = input('input number over 0 to get log')
                try:
                    n = float(n)
                    if n <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
            while True:
                a = input('input number over 0 as a base of log')
                try:
                    a = float(a)
                    if a <= 0 or a == 1:
                        raise ValueError
                    print(logarithm.log(a, n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'lg':
            while True:
                n = input('input number over 0 to get lg')
                try:
                    n = float(n)
                    if n <= 0:
                        raise ValueError
                    print(logarithm.lg(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'ln':
            while True:
                n = input('input number over 0 to get ln')
                try:
                    n = float(n)
                    if n <= 0:
                        raise ValueError
                    print(logarithm.ln(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'exp2':
            while True:
                n = input('input number to get n^2')
                try:
                    n = float(n)
                    print(exponentiation.exp2(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'exp3':
            while True:
                n = input('input number to get n^3')
                try:
                    n = float(n)
                    print(exponentiation.exp3(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'root2':
            while True:
                n = input('input number over 0 to get square root')
                try:
                    n = float(n)
                    if n < 0:
                        raise ValueError
                    print(root.root2(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        elif func == 'root3':
            while True:
                n = input('input number to get cubic root')
                try:
                    n = float(n)
                    print(root.root3(n))
                    break
                except ValueError:
                    print('wrong value, try again')
                    continue
        else:
            print('wrong value, try again')
            continue
        while True:
            exit = input('do you want to continue?')
            if exit == 'yes' or exit == 'Yes' or exit == 'no' or exit == 'NO':
                break
            else:
                print('wrong value')
                continue
        if exit == 'yes' or exit == 'Yes':
            continue
        elif exit == 'no' or exit == 'No':
            break
main()