def primeish(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 2
    else:
        result = -1
        fact = 1
        for j in range(3,n+1):
            fact = fact*(j-2)
            result += (fact - j*floor(fact/j))
        return result

import math
def plotprimeish(n):
    n = int(math.floor(n))
    return primeish(n)

pretty_print(html("The number of primes up to 20000 this formula gives is $%s$"%primeish(20000)))
pretty_print(html("The real function in Sage gives $%s$"%prime_pi(20000)))
pretty_print(html("And let's compare plots:"))
p = plot(lambda x:plotprimeish(x), (x,2,100)) + plot(prime_pi,2,100,color='black')
show(p)