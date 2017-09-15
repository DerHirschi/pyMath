import time


inp = raw_input('Bitte Zahlen eingeben.. Leertaste zwischen Zahlen ')

inp = inp.split(' ')
for i in range(len(inp)):
    inp[i] = int(inp[i])

ti = time.time()
le = len(inp)

while le >= 0:
    t = -1
    for i in range(le):
        if inp[i] > t:
            t = inp[i]

    if t != -1:
        inp.remove(t)
        print inp
        inp.insert(le - 1, t)
    le -= 1


print time.time() - ti
print inp


