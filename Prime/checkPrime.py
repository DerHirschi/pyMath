import time


def checkprime(inp):

    ret = True
    div = float(2)
    res = float
    while div < inp and ret:

        res = inp / div
        if res % 1 == 0:
            #print res
            ret = False
            #print 'Nooooo'
            break

        div += 1

    return ret


n = long(2)
ti = time.time()
while 1:
    if str(n)[-1] not in [1, 3, 7, 9] and n % 2 != 0:
        if checkprime(n):
            print '{} - {}'.format(n, 'is Prime')

    n += long(1)
    #if n >= 1000:
    #    break

#print time.time() - ti
