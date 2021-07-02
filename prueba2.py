#!/Applications/SageMath-9-2.app/Contents/Frameworks/sage.framework/Versions/9.2/local/bin/python3.8 -python
import sage.all
import matplotlib.pyplot as plt

if __name__ == '__main__':
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
                result += (fact - j*sage.all.floor(fact/j))
            return result

import math
def plotprimeish(n):
    n = int(math.floor(n))
    return primeish(n)


p = sage.all.plot(lambda x:plotprimeish(x), (x,2,100)) + sage.all.plot(sage.all.prime_pi,2,100,color='black')
sage.all.show(p)#!/Applications/SageMath-9-2.app/Contents/Frameworks/sage.framework/Versions/9.2/local/bin/python3.8 -python
import sage.all
import matplotlib.pyplot as plt

