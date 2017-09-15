import time

f1 = 0
f2 = 1
count = 0

while 1:
    temp = f2
    f2 = f2 + f1
    f1 = temp
    count = count + 1
    print "\nIritation: {}\nResult: {}\n\n".format(count, f2)
    time.sleep(0.1)
