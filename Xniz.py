#Образувайте всички низове с дължина S използвайки първите S малки букви на латинската азбука така, че във всеки образуван низ да не се съдържа една и съща буква, повече от един път. Подредете низовете по азбучен ред (лексикографски) и определете кой е низът стоящ на Х-тото място.
# Sample Input 0
#
# 2
# 2 2
# 3 6
# Sample Output 0
#
# ba
# cba
results = []
import itertools
T = int(input())
def program():
        niz = "abcdefghijklmnopqrstuvwxyz"
        S_X = input().split(' ')
        S = int(S_X[0])
        X = int(S_X[1])
        niz = niz[:S]
        niz = list(niz)
        niz = list(itertools.permutations(niz, S))
        niz = [''.join(i) for i in niz]
        niz.sort()
        return print(niz[X - 1])
for i in range(T):
    program()
# print(results[0])
# print(results[1])
