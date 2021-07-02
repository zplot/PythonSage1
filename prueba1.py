#!/Applications/SageMath-9-2.app/Contents/Frameworks/sage.framework/Versions/9.2/local/bin/python3.8 -python
import sage.all
import matplotlib.pyplot as plt



if __name__ == '__main__':

    def J(x):
        sum = 0
        for i in range(1, int(sage.all.log(x) / sage.all.log(2)) + 1):
            sum = sum + 1 / i * sage.all.prime_pi(x ** (1 / i))
        return (sum)

    print(J(100))

    plt.plot([i*i for i in range(10)])
    plt.show()










