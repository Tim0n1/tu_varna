#В детската градина са подредени в кръг 2n кутии. Първите n кутии са сини и празни, вторите n са зелени и пълни с подаръци. Започваме от първата кутия (която е празна) и отваряме всяка к-та кутия. Ако попаднем на кутия с подаръци ги отделяме настрана, изваждаме кутията от кръга и продължаваме от следващата. Ако попаднем на празна кутия губим и връщаме всички подаръци. Ако отворим всички кутии с подаръци преди да сме попаднали на празна кутия печелим и можем да вземем подаръците. Нека да помогнем на децата да спечелят играта и се върнат у дома с много подаръци.
import itertools

n = int(input())
n_2 = 2 * n
N = [i for i in range(1, n_2 + 1)]
pulni = N[:n]
prazni = N[n:]
print(pulni, prazni)
for i in itertools.cycle(N):
    print(i)

