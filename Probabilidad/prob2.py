# Distribucion Binomial usando scipy.stats

from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculamos los primeros momentos:

n, p = 5, 0.4
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')

# Mostramos el pmf de la variable aleatoria  (``pmf``):

x = np.arange(binom.ppf(0.01, n, p),
              binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='pmf binomial')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
ax.legend(loc='best', frameon=False)


# Comprobar la exactitud del  ``cdf`` y  ``ppf``:

prob = binom.cdf(x, n, p)
np.allclose(x, binom.ppf(prob, n, p))


# Generamos numeros aleatorios

r = binom.rvs(n, p, size=1000)
plt.show()
    