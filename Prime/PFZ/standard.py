import time

def primes(n):

   s = set(range(3, n+1, 2))

   if n >= 2:
       s.add(2)
   m = 3
   while m * m < n:
       s.difference_update(range(m*m, n+1, 2*m))
       m += 2
       while m not in s:
           m += 2

   return sorted(s)

def pfz(n):
    ret = []
    prime = primes(n)
    for i in range(len(prime)):
        if n > 1.0:
            n = float(n)
            p = prime[i]
            while n / p % 1 == 0:
                n = n / p
                if n % 1 == 0:
                    ret.append(p)
                    print ret
                    print n

                else:
                    break
        elif n == 1.0:
            break

    if n == 1.0:
        return ret
    else:
        return []

ti = time.time()
print pfz(56436588)
print time.time() - ti
#print primes(464364)

