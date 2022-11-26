#На първият ред има едно цяло число N, определящо общия брой на страниците в книжката. На втория ред има цифра C, определяща коя е цифрата в номера на страницата, която Женя е открила, че се среща поне веднъж в скъсаните страници с картинки. Следва ред с номерата на страниците, съдържащи цифрата C, които са останали, след като сестричката е скъсала и скрила откъснатите листи. Номерата на страниците в реда са разделени помежду си с интервал.
#На един ред в изхода се извежда изчисления брой на откъснатите страници, които са във всичките листи, скъсани и скрити от сестричката на Женя на тайното място.
# Constraints
# 0<=C<=9 2<=N<=50000
N = int(input())
if not 3<=N<=50000:
    exit()
N = [str(i) for i in range(1, N + 1)]
C = str(input())
if not 1<=int(C)<=9:
    exit()
pages = input().split(' ')
pages = [str(i) for i in pages]
for i in pages:
    if C not in i:
        exit()
N_l = []
c_pages = []
length = 0
for _ in range(len(N)):
    i = 0
    if len(N) == 1:
        N_l.append([N[i]])
    else:
        N_l.append([N[i], N[i+1]])
    if len(N) == 2 or len(N) == 1:
        break
    N.pop(i)
    N.pop(i)
for i in N_l:
        for j in i:
            if C in j:
                c_pages.append(i)
#print(N_l)
c_pages2 = c_pages.copy()
for i in c_pages:
    for j in pages:
        if j in i:
            c_pages2.remove(i)
            break
#print(c_pages)
c_pages2 = [item for sublist in c_pages2 for item in sublist]
c_pages2 = set(c_pages2)
print(len(c_pages2))

