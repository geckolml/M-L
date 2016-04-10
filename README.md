# M-L

1. Introdución a Python
   * Curso rápido de Python.
   * Uso de las paquetes: Matplotlib, NumPy, Pandas, scikit-learn.
   * Nano y Vim. Uso de Jupyter .

2. Algebra Lineal
   * Vectores y Matrices.
   * Valores y vectores propios.

3. Estadística
   * Describiendo un conjunto de datos. Tendencias centrales, dispersión.
   * Correlación. Paradoja de Simpson.
   * Algunas advertencia, acerca de la correlación.
   * Correlación y Causalidad.
   
4. Probabilidad
   * Dependencia y Independencia. Probabilidad Condicional. Teorema de Bayes.
   * Variables Aleatorias.Distribuciones continuas. La distribución Normal.  
   * Teorema del Límite Central.

5. Hipótesis e Inferencia  Estadística
   * Prueba de hipótesis estadística.
   * Intervalos de Confianza.
   * P-hacking. El test A/B.
   * Inferencia Bayesiana.
   
6. Descenso del Gradiente
   * Ideas detrás del método del Gradiente. Estimando el gradiente.
   * Usando el gradiente.
   * Descenso del gradiente estocástico.
   
7. Obtención de Datos
   * Leyendo archivos. Web Scraping. Ejemplos.
   * Usando APIS:JSON y XML y APIS no autenticadas. Encontrando APIS.
   * Usando la API de Twitter.
   
8. Trabajando con Datos
   * Explorando datos de 1,2 y más dimensiones.
   * Manipulando datos, reescalando y reducción de la dimensionalidad
   
9. Machine Learning
   * ¿ Qué es Machine Learning?. Sobreajuste y Subajuste. Exactitud.
   * The Bias-Variance Trade-off.

10. K-vecinos más cercanos
   * El modelo. Ejemplos
   * La maldición de la dimensión.

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

### Weka 

[Weka](http://www.cs.waikato.ac.nz/ml/weka/) (Waikato Environment for Knowledge Acquisition) es una herramienta de Machine Learning y Data Minning escrito en Java. Con Weka podemos hacer Preprocessing data, clustering, classification, regression y ahora Big Data y datos con un driver JDBC.

Para instalar Weka en Ubuntu, desempaquetar el [archivo](http://prdownloads.sourceforge.net/weka/weka-3-6-13.zip) conteniendo a Weka en algún de tu preferencia y luego ir al directorio creado  (weka-3-6-13) y ejecutar

```bash
c-lara@Lara:~$java -Xmx1000M -jar weka.jar
```

### Mahout 

[Mahout](http://mahout.apache.org/) es un proyecto que es es parte del proyecto Apache. Una característica principal de Mahout es su integración con el paradigma Hadoop Map/Reduce para el procesamiento de datos a gran escala. Mahout soporta un gran número de algoritmos incluyendo:

* Naive Bayes Classifier.
* K Means Clustering.
* Recommendation Engine.
* Logistic Regression Classifier.
* Random Forest.


## Lecturas
- [Análisis de los pro y contras de ciertos  algoritmos en Machine Learning](http://www.lauradhamilton.com/machine-learning-algorithm-cheat-sheet).
- [7 pasos para empezar con Machine Learning con Python ](http://www.kdnuggets.com/2015/11/seven-steps-machine-learning-python.html).
- [Un tour sobre los principales algoritmos de Machine Learning](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/).
- [Algoritmos de Machine Learning](http://www.analyticsvidhya.com/blog/2015/08/common-machine-learning-algorithms/).
- [13 framework usados en Machine Learning](http://www.infoworld.com/article/3026262/data-science/13-frameworks-for-mastering-machine-learning.html).
- [R y MongoDb](https://gist.github.com/Btibert3/7751989).
- [Weka 3, software de Data Mining en Java ](http://www.cs.waikato.ac.nz/ml/weka/).
- [Notas de Scikit-Learn como herramienta de Machine Learning](http://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/).
- [Machine Learning Cheat Sheet for scikit-learn](http://peekaboo-vision.blogspot.pe/2013/01/machine-learning-cheat-sheet-for-scikit.html).
- [Página principal de Scikit-learn](http://scikit-learn.org/stable/index.html).
- [Artículo inicial de que es  Machine Learning  ](http://www.analyticsvidhya.com/blog/2015/06/machine-learning-basics/).
- [Uso de Pandas, para Análisis exploratorio de datos ](http://www.analyticsvidhya.com/blog/2014/08/baby-steps-python-performing-exploratory-analysis-python/).
- [Tutorial de datacamp de Machine Learning en R](http://blog.datacamp.com/machine-learning-in-r/).
- [Ciencia de datos con R, Analytics, Big Data, Text Mining](http://togaware.com/onepager/).
- [Tutorial completo acerca de ciencia de datos en R ](http://www.analyticsvidhya.com/blog/2016/02/complete-tutorial-learn-data-science-scratch/).
