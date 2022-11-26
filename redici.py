#Изчислете броя на всички различни редици от N неотрицателни цели числа, в които всеки елемент е по-малък от дадено число Х, а сумата на елементите е по-малка от дадено число У.

n_tests = int(input())
n_redici_l = []
for i in range(n_tests):
    X_N_Y = input().split(' ')
    try:
        X_N_Y.remove(' ')
    except:
        pass
    X = int(X_N_Y[0])
    N = int(X_N_Y[1])
    Y = int(X_N_Y[2])
    if 1<X<Y<30 == False:
        exit()
    if 0 < N < 20 == False:
        exit()
    X = [i for i in range(X)]


    def product(*args, repeat=1):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)

    X = [i for i in product(X, repeat=N)]
    n_redici = 0
    for i in X:
        if sum(i) < Y:
            n_redici += 1
    n_redici_l.append(n_redici)

print(n_redici_l[0])
print(n_redici_l[1])
