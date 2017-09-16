import time


def checkprime(inp):

    ret = True
    div = float(2)
    res = float
    while div < inp and ret:

        res = inp / div
        if int(res) == float(res):
            #print res
            ret = False
            #print 'Nooooo'
            break
        if div % 100000 == 0:
            print res
        div += 1

    return ret


n = long(2252888775)
ti = time.time()
while 1:
    if len(str(n)) > 1 and str(n)[-1] not in [1, 3, 7, 9]:
        if checkprime(n):
            print '{} - {}'.format(n, 'is Prime')
        else:
            print '{} - {}'.format(n, 'no')
        n += long(1)
    #if n >= 10000:
    #    break

print time.time() - ti
