#!/usr/bin/env python
# Quelle : https://mail.python.org/pipermail/edu-sig/2009-January/009028.html
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


ti = time.time()
res = primes(60000000)
print time.time() - ti

print res[-1]

