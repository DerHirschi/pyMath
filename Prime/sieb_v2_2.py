# Nach vorbild sieb_wiki.py ( Bool statt int )
import math
import time


bis = 100000000000
wurz = math.sqrt(bis)

tim = time.time()
res = [True] * (bis + bis)
print len(res)
res[0] = False
res[1] = False
#endres = []
sta = 2
a = sta


while sta <= wurz:

    if res[sta]:
        n = sta
        temp = sta * n
        while temp <= bis:
            temp = sta * n
            if res[temp] and temp <= bis:
                # print 'start {} * n {} = {}'.format(start, n, temp)
                res[temp] = False

            n += 1

    b = sta * sta
    #pri = []
    while a < b:
        if res[a]:
            print 'Prime: ' + str(a)
            #endres.append(a)

        a += 1

    #print pri
    sta += 1


tim = time.time() - tim
#print endres
print 'Sekunden {}'.format(tim)

#checkres(endres)

