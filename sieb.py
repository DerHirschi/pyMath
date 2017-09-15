import math
import time


bis = 100000
wurz = math.sqrt(bis)
print wurz
res = []

start = 2

tim = time.time()

while 1:
    n = start
    while 1:
        temp = start * n
        if temp not in res and temp <= bis:
            print 'start {} * n {} = {}'.format(start, n, temp)
            res.append(temp)

        n += 1
        if temp > bis:
            break

    start += 1
    if start > wurz:
        break


print temp
endres = []

for i in range(res[-1]):
    if i not in res:
        print i
        endres.append(i)

endres = endres[2:]
print endres

tim = time.time() - tim

print 'Sekunden {}'.format(tim)

