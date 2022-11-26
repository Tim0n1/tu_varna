
#колко различни комплекта от Р на брой покупки и В на брой подаръчни хартии могат да се съставят от Х различни вида покупки и У различни вида подаръчни хартии. Във всеки комплект видовете подаръци и хартии не трябва да се повтарят.
import itertools
T = int(input())
for i in range(T):
    P_B_X_Y = input().split(' ')
    P = int(P_B_X_Y[0])
    B = int(P_B_X_Y[1])
    X = int(P_B_X_Y[2])
    Y = int(P_B_X_Y[3])
    P = [i for i in range(1, P + 1)]
    B = [i for i in range(1, B + 1)]
    X = [i for i in range(1, X + 1)]
    Y = [i for i in range(1, Y + 1)]
