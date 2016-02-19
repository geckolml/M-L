import math, random
from collections import Counter
from matplotlib import pyplot as plt


def bernoulli_prueba(p):
    return 1 if random.random() < p else 0

def binomial(n,p):
    return sum(bernoulli_prueba(p) for _ in range(n))
    

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def graf_histograma(p, n, num_puntos):
    data = [binomial(n, p) for _ in range(num_puntos)]

    # usamos un grafico de barras para mostrar las muestras binomiales
    histograma  = Counter(data)
    plt.bar([x - 0.4 for x in histograma .keys()],
            [v / num_puntos for v in histograma .values()],
            0.8,
            color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    # usamos un grafico de  lineas para mostrar una  aproximacion normal
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs,ys)
    plt.title("Distribucion Binomial vs. Approximacion Normal")
    plt.show()

graf_histograma(0.75, 100, 10000) 