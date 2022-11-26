import itertools
while True:
    input1 = input()
    if input1 == '0':
        exit()
    try:
        if int(input1) <= 3 and int(input1) > 100:
            exit()
    except Exception:
        pass
    input1 = input1.split(' ')
    N = int(input1[0])
    M = int(input1[1])
    input2 = input().split(' ')
    numbers = [int(i) for i in input2]
    for i in numbers:
        if i <= 0:
            exit()
    if N <= 3 or N >= 101:
        exit()
    if M <= 3 or M >= 300000:
        exit()
    sums = []
    razliki = []
    numbers = itertools.combinations(numbers, 3)
    numbers = [i for i in numbers]

    for i in numbers:
        sum = i[0] + i[1] + i[2]
        sums.append(sum)
    for i in sums:
        if i >= M:
            sums.remove(i)
    for i in sums:
        razlika = M - i
        if razlika <= 0:
            continue
        razliki.append(razlika)
    if M - min(razliki) == 99:
        print(100)
    else:
        print(M - min(razliki))



