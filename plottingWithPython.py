import matplotlib.pyplot as plt
import numpy as np
import sage.all


def plotRange(start, end, delta):
    inicio = float(start)
    temp = [inicio]
    delta2 = float(delta)
    for i in range(sage.all.floor(end - start) / delta):
        temp.append(inicio + (i + 1) * delta2)
    resultado = temp
    return resultado


def J(x):
    sum = 0
    for i in range(1, int(sage.all.log(x) / sage.all.log(2)) + 1):
        sum = sum + 1 / i * sage.all.prime_pi(x ** (1 / i))
    return (sum)


inicio = 1
final = 1000
delta = 1


def func(x): return J(x)


if __name__ == '__main__':
    t1 = plotRange(inicio, final, delta)
    t2 = [float(i) for i in t1]

    iterator = map(lambda x: func(x), t2)
    s2 = list(iterator)

    fig, ax = plt.subplots()
    ax.plot(np.array(t1), np.array(s2))

    ax.set(xlabel='x', ylabel='J(x)',
           title='Graph of J(x)')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
    print(J(100))
