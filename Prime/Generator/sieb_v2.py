import math
import time


bis = 100000000000
wurz = math.sqrt(bis)

res = []
endres = []
sta = 2
a = sta
tim = time.time()

while sta <= wurz:

    if sta not in res:
        n = sta
        temp = sta * n
        while temp <= bis:
            temp = sta * n
            if temp not in res and temp <= bis:
                # print 'start {} * n {} = {}'.format(start, n, temp)
                res.append(temp)

            n += 1

    b = sta * sta
    #pri = []
    while a < b:
        if a not in res:
                # print a
            endres.append(a)
            #pri.append(a)
        a += 1

    #print pri
    sta += 1


tim = time.time() - tim
print endres
print 'Sekunden {}'.format(tim)

#checkres(endres)

