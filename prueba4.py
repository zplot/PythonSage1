import matplotlib.pyplot as plt
import numpy as np
import sage.all


def J(x):
    sum = 0
    for i in range(1, int(sage.all.log(x) / sage.all.log(2)) + 1):
        sum = sum + 1 / i * sage.all.prime_pi(x ** (1 / i))
    return (sum)

if __name__ == '__main__':

    # Data for plotting
    t1 = range(1, 100, 1)
    t2 = np.array(t1)
    s1 = range(1, 100, 1)
    iterator = map(lambda x: J(x), s1)
    s2 = list(iterator)
    s3 = np.array(s2)


    fig, ax = plt.subplots()
    ax.plot(t2, s3)

    ax.set(xlabel='x', ylabel='J(x)',
           title='Graph of J(x)')
    ax.grid()

    fig.savefig("test.png")
    plt.show()