import math
import time
import threading
from checkResSieb import checkres


bis = 10000
wurz = math.sqrt(bis)

res = []
endres = []
sta = 2
a = sta
tim = time.time()


class i_Count(object):
    a = sta


class Thr(threading.Thread):
    def __init__(self, c_sta, c_a=i_Count.a):
        threading.Thread.__init__(self)
        b = c_sta * c_sta
        pri = []
        while c_a < b:
            if c_a not in res:
                # print a
                endres.append(c_a)
                pri.append(c_a)
            c_a += 1

        i_Count.a = c_a
        #print pri


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

    Thr(sta, a).start()
    sta += 1


tim = time.time() - tim
print endres
print 'Sekunden {}'.format(tim)





#checkres(endres)

