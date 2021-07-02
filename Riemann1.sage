print("*****************************************************************")
r = 193
print(r)
def J(x):
    sum = 0
    for i in range(1, int(log(x)/log(2)) + 1):
        sum = sum + 1 / i * prime_pi(x**(1/i))
    return(sum)
print(J(100))


p = plot(J, (x, 1, 200))
show(p)