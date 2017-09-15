import math
import time
import threading
from checkResSieb import checkres


class MainThread:

    bis = 100000
    wurz = math.sqrt(bis)
    sta = 2
    res = []
    endres = [2]
    threa = 12

    def __init__(self):
        tim = time.time()
        for i in range(self.threa):

            MainThread.calThread(MainThread).start()
            if i != self.threa - 1:
                time.sleep(0.1)
                #print '222222222!!!!'
                MainThread.sta += 1


        temp = MainThread.sta

        #t = MainThread.calThread(MainThread)
        #t.start()

        while MainThread.sta <= MainThread.wurz:
            print MainThread.sta
            #print MainThread.res

            while temp == MainThread.sta:
                pass
                #print MainThread.sta
                #print 'wait'
                #time.sleep(0.1)

            #temp = temp - 1
            b = temp * temp
            a = temp
            temp = MainThread.sta
            MainThread.calThread(MainThread).start()
            while a < b:
                if a not in MainThread.res and a not in MainThread.endres:
                    # print a
                    MainThread.endres.append(a)
                a += 1

        a = int(MainThread.wurz)
        b = a * a
        while a < b:
            if a not in MainThread.res and a not in MainThread.endres:
                # print a
                MainThread.endres.append(a)
            a += 1

        print MainThread.endres

        tim = time.time() - tim

        print 'Sekunden {}'.format(tim)
        checkres(MainThread.endres)

    class calThread(threading.Thread):
        def __init__(self, mthr):
            threading.Thread.__init__(self)
            self.mainth = mthr

        def run(self):
            sta = MainThread.sta
            bis = self.mainth.bis
            if sta not in MainThread.res:
                n = sta
                temp = sta * n
                while temp <= bis:
                    temp = sta * n
                    if temp not in MainThread.res and temp <= bis:
                        #print 'start {} * n {} = {}   th : {}'.format(sta, n, temp, self)
                        MainThread.res.append(temp)
                    n += 1

            MainThread.sta += 1


"""         
        b = sta * sta
        while a < b:
            if a not in MainThread.res:
                    # print a
                MainThread.endres.append(a)
            a += 1

            print MainThread.endres
            

        time.sleep(1)
        tim = time.time() - tim
        print MainThread.endres
        print 'Sekunden {}'.format(tim)
"""
    # checkres(endres)


MainThread()

