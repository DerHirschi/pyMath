import math
import time
import threading
from checkResSieb import checkres


class MainThread:

    bis = 1000
    wurz = math.sqrt(bis)

    res = []
    endres = []

    def __init__(self):
        t = self.calThread(self)
        t2 = self.calThread(self)
        t.start()
        t2.start()

    class calThread(threading.Thread):
        def __init__(self, mthr):
            threading.Thread.__init__(self)
            self.mainth = mthr

        def run(self):
            sta = 2
            a = sta
            wurz = self.mainth.wurz
            bis = self.mainth.bis
            tim = time.time()

            while sta <= wurz:

                if sta not in MainThread.res:
                    n = sta
                    temp = sta * n
                    while temp <= bis:
                        temp = sta * n
                        if temp not in MainThread.res and temp <= bis:
                            #print 'start {} * n {} = {}'.format(sta, n, temp)
                            MainThread.res.append(temp)

                        n += 1

                b = sta * sta
                while a < b:
                    if a not in MainThread.res:
                            # print a
                            MainThread.endres.append(a)
                    a += 1

                print MainThread.endres
                sta += 1

            time.sleep(1)
            tim = time.time() - tim
            print MainThread.endres
            print 'Sekunden {}'.format(tim)

# checkres(endres)


MainThread()