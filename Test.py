import numpy as np
import math

def f(x):
    return x ** 5 + 3 * x ** 3 + 2


def get_Sn(n, a, b):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.array([x[i] for i in range(1, n)])
    return h * (f(a) / 2 + f(b) / 2 + np.sum(f(y)))


def get_S2n(n, a, b):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.array([x[i] for i in range(1, n + 1)])
    x_hat = y - h / 2
    # print(get_Sn(n,a,b))
    return get_Sn(n, a, b) / 2 + h * (sum(f(x_hat))) / 2


def calculate(n, a, b, eps):
    I_n = get_Sn(n, a, b)
    I_2n = get_S2n(n, a, b)
    delta = abs(I_2n - I_n)
    # print(1, delta)
    while (delta > eps):
        print(n, delta)
        n = n * 2
        I_n = I_2n
        I_2n = get_S2n(n, a, b)
        delta = abs(I_2n - I_n)
    return I_2n

# print(get_S2n(5,1,2))
m = 0.075
KE = calculate(5, 0, 0.5, 0.0001)
v = math.sqrt(2 * KE / m)
print("KE:", KE)
print("v:", v)
