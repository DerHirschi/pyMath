import time

def checkprime(inp):

    ret = True
    div = float(2)
    while div < inp and ret:

        res = inp / div
        if res % 1 == 0:
            ret = False
            break
        div += 1
    return ret


def pfz(n):
    ret = []

    for i in range(2, n + 1, 1):
        if checkprime(i) and n > 1:
            n = float(n)
            while n / i % 1 == 0:
                n = n / i
                if n % 1 == 0:
                    ret.append(i)
                    print ret
                    print n

                else:
                    break

    return ret

ti = time.time()
print pfz(240)
print time.time() - ti

