# M-L

1. Introduccíon a Python
   * Curso ŕapido de Python.
   * Uso de las paquetes: Matplotlib, NumPy,pandas, scikit-learn.
   * Nano y Vim. Uso de Ipython.

2. Algebra Lineal
   * Vectores y Matrices.
   * Valores y vectores propios.

3. Estad́ıstica
   * Describiendo un conjunto de datos. Tendencias centrales, dispersión.
   * Correlacíon. Paradoja de Simpson.
   * Algunas advertencia, acerca de la correlacíon.
   * Correlacíon y Causalidad.


## Herramientas a  usar 

### Editor Vim

[vim](http://www.vim.org/), un editor de texto que dispone de diferentes modos entre los que se alternan ciertas operaciones, comunes entre los programadores. No obstante, debido a su eficiencia, a su variedad de añadidos ("plugins")", y a sus posibilidades de personalización vim es uno de los editores de texto más populares para programadores y usuarios de sistemas tipo Unix (junto con Emacs*).

Existe un tutorial, que se puede utilizar dentro de Linux (Ubuntu 14.04), escribiendo en el terminal.

```bash
c-lara@Lara:~$ vimtutor
```

Otras fuentes de referencia son:

1 . [Vim en archlinux](https://wiki.archlinux.org/index.php/Vim_%28Espa%C3%B1ol%29).

2 . [Tutorial de Vim](http://www.sromero.org/wiki/linux/aplicaciones/manual_vim).

3 . [Learn Vim Progressively](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/).

### Anaconda 

[Anaconda](https://www.continuum.io/downloads) es una distribución completa  libre de [Python](https://www.python.org/) incluye [paquetes de Python ](http://docs.continuum.io/anaconda/pkg-docs).

Anaconda incluye los instaladores de Python 2.7 y 3.5.  La instalación en **Linux**, se encuentra en la página de Anaconda y es más o menos así

1 . Descargar el instalador de Anaconda para Linux.

2 . Después de descargar el instalar, en el terminal, ejecuta para 3.5

```bash
c-lara@Lara:~$ bash Anaconda3-2.4.1-Linux-x86_64.sh

```

Es recomendable leer, alguna de las característica de Anaconda en el siguiente material [conda 30-minutes test drive](http://conda.pydata.org/docs/test-drive.html).

3 . La instalación de paquetes como [seaborn](http://stanford.edu/~mwaskom/software/seaborn/) o [bokeh](http://bokeh.pydata.org/en/latest/) se pueden realizar a través de Anaconda, de la siguiente manera:



``` bash
c-lara@Lara:~$ conda install bokeh
```

Alternativamente podemos desde PyPI usando **pip**:

```bash
c-lara@Lara:~$ pip install bokeh
``` 

El proyecto [Anaconda](https://www.continuum.io/downloads) ha creado [R Essentials](http://anaconda.org/r/r-essentials), que incluye el IRKernel y alrededor de 80 paquetes para análisis de datos, incluyendo `dplyr`, `shiny`, `ggplot2`,`caret`, etc. Para instalar **R Essentials** en un entorno de trabajo, hacemos

```bash
c-lara@Lara:~$ conda install -c r r-essentials
``` 


## Lecturas
1 .[Pro y contras de los algoritmos en Machine Learning](http://www.lauradhamilton.com/machine-learning-algorithm-cheat-sheet).

2 .[7 pasos para empezar con Machine Learning](http://www.kdnuggets.com/2015/11/seven-steps-machine-learning-python.html).

3 .[Un tour sobre los algoritmos de Machine Learning](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/).

4 .[Algoritmos comunes de Machine Learning](http://www.analyticsvidhya.com/blog/2015/08/common-machine-learning-algorithms/).

5 .[13 framework para Machine Learning](http://www.infoworld.com/article/3026262/data-science/13-frameworks-for-mastering-machine-learning.html).

