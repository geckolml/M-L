## Curso: Tópicos de investigación (Machine Learning)

###  Material de referencias

* Libros de Machine Learning.
  - Python Machine Learning, Sebastian Raschka, Pack Publishing, 2015.
  - [Machine Learning: a Probabilistic Perspective](http://www.cs.ubc.ca/%7Emurphyk/MLbook/index.html) de Kevin Murphy (2012).
  . [Pattern Recognition and Machine Learning](http://research.microsoft.com/en-us/um/people/cmbishop/prml/) de Chris Bishop  (2006). 

* Probabilidad
  
  - [Notas ](http://www.statslab.cam.ac.uk/~rrw1/prob/prob-weber.pdf) de  Richard Weber.
  - Capitulo 2 del libro de Kevin P. Murphy o Chris Bishop.
  - [Notas](http://cs229.stanford.edu/section/cs229-prob.pdf) de probabilidades de las clases de Machine Learning de Stanford.
 
* Álgebra Lineal
  - [Coding The Matrix: Linear Algebra Through Computer Science Applications](http://codingthematrix.com/), fantástico libro de Philip Klein (Revisar los diapositivas que acompañan al libro).
  - [Notas](http://cs229.stanford.edu/section/cs229-linalg.pdf) de álgebra lineal de las clases de Machine Learning de Stanford.
  - Apendice C del libro de Chris Bishop.
  - [Notas ](http://cs.nyu.edu/%7Edsontag/courses/ml12/notes/linear_algebra.pdf) de Sam Roweis.
  
* Optimización
  - [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) de Stephen Boyd y  Lieven Vandenberghe.
  - Notas de Optimización de las clases de Machine Learning de Stanford:
    * [Convex Optimization Overview 1](http://cs229.stanford.edu/section/cs229-cvxopt.pdf).
    * [Convex Optimization Overview 2](http://cs229.stanford.edu/section/cs229-cvxopt2.pdf).

## Temario

* Clase 1: Introducción al Machine Learning 
    - Lectura obligatoria: [Capitulo1 de Kevin P. Murphy](http://www.cs.ubc.ca/%7Emurphyk/MLbook/pml-intro-22may12.pdf).
    - [Diapositiva 1]().
* Clase 2: Introducción al aprendizaje: Funciones de pérdida, algoritmo del perceptrón, prueba de errores del perceptrón.
    - [Diapositiva 2]()
    - 
* Clase 3: Clasificadores lineales: Introducción al SVM.
    - [Diapositiva 3]().
* Clase 4: SVM: Introducción a la optimización convexa
  - [Gradient, Subgradient and how they may affect your grade](http://cs.nyu.edu/~dsontag/courses/ml16/slides/notes_convexity16.pdf)
  - Lectura obligatoria: [Support Vector Machines](http://cs229.stanford.edu/notes/cs229-notes3.pdf) de Andrew Ng.
  - Notas adicionales: [Linear Support Vector Machines](https://davidrosenberg.github.io/ml2015/docs/svm-notes.pdf) de David S. Rosenberg.
  - [Diapositiva 4]().
* Clase 5: Descenso de gradiente estocástico
  - [Diapositiva 5]().
  
* Clase 6: Métodos del Kernel: Métodos del Kernel para SVM y classificación multiclases.
 - [Notas](http://cs229.stanford.edu/notes/cs229-notes3.pdf) sobre Kernels (sección 7).
 - [Pegasos Algorithm y  Kernels](http://cs.nyu.edu/~dsontag/courses/ml16/slides/lecture6_notes.pdf).
 - [Shalev-Shwartz & Ben-David](http://www.cs.huji.ac.il/%7Eshais/UnderstandingMachineLearning/index.html), capítulo 16 sobre métodos de kernels.
 - [Shalev-Shwartz & Ben-David](http://www.cs.huji.ac.il/%7Eshais/UnderstandingMachineLearning/index.html), secciones Sections 17.1 & 17.2 sobre multiclases.
 . [Diapositiva 6]().
 
Clase 7: Regularización L1 y introducción a la teoria del aprendizaje
  - [Diapositiva 7]().
  
Clase 8: Teoria del aprendizaje: Clases de hipótesis finitas
  - [Notas](http://cs229.stanford.edu/notes/cs229-notes4.pdf) de teoria del aprendizaje de Andrew Ng. Secciones 1 -3.
  - [Diapositiva 8]().
  
Clase 9: Teoria de aprendizaje: Dimensión VC
  - [Notas](http://cs229.stanford.edu/notes/cs229-notes4.pdf) de teoria del aprendizaje de Andrew Ng. Sección 4.
  - Lectura opcional: [A Tutorial on Support Vector Machines for PatternRecognition](http://cs.nyu.edu/%7Edsontag/courses/ml14/notes/burges_SVM_tutorial.pdf). Páginas 29-31.
  - [Diapositiva 9]

Clase 10 : Árboles de decisión.
  - [Trees](https://jeremykun.com/2012/09/16/trees-a-primer/).
  - [Decision trees ](https://jeremykun.com/2012/10/08/decision-trees-and-political-party-classification/).
  - [Tom M. Mitchel: Capitulo 3](http://www.cs.princeton.edu/courses/archive/spr07/cos424/papers/mitchell-dectrees.pdf).
  - Lectura opcional: [Cynthia Rudin: Decision Trees](https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/lecture-notes/MIT15_097S12_lec08.pdf)
  
## Herramientas a  usar 

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

### Proyecto Jupyter y el Jupyter Nbviewer

El [Proyecto Jupyter](http://jupyter.org/)  es una aplicación web que te permite crear y compartir documentos que contienen código de diversos lenguajes de programación, ecuaciones,  visualizaciones y texto en diversos formatos. El uso de Jupyter incluye la ciencia de datos, simulación numérica, la modelización en estadística, Machine Learning, etc.


[Jupyter nbviewer](https://nbviewer.jupyter.org/)  es un servicio web gratuito que te permite compartir las versiones de archivos realizados por Jupyter, permitiendo el renderizado de diversos fórmatos incluyendo, código latex.

- [Jupyter Documentation](https://jupyter.readthedocs.io/en/latest/).


### Git y Github

[Git](https://git-scm.com/) es un sistema de control de versiones de gran potencia y versatilidad en el manejo de un gran número de archivos de  código fuente a a través del desarrollo no lineal, es decir vía la gestión rápida de ramas y mezclado de diferentes versiones.

Para poder revisar y aprender los comandos necesarios de Git, puedes darle una ojeada al excelente [tutorial de CodeSchool](https://try.github.io/levels/1/challenges/1) o a la [guía](http://rogerdudler.github.io/git-guide/index.es.html) de Roger Dudle para aprender  Git.

[Github](https://github.com/) es una plataforma de desarrollo colaborativo de software utilizado para alojar proyectos (muchos proyectos importantes como paquetes de R, Django, el Kernel de Linux, se encuentran alojados ahí) utilizando Git y el framework Ruby on Rails.

Podemos instalar Git en Ubuntu utilizando el administrador de paquetes `Apt`:

```bash
c-lara@Lara:~$sudo apt-get update
c-lara@Lara:~$sudo apt-get install git
```

Referencias y Lecturas

- [Usando el GIT](http://www.cs.swarthmore.edu/~newhall/unixhelp/git.php).
- [Practical Git Introduction](http://marc.helbling.fr/2014/09/practical-git-introduction).
- [Visual Git Guide](http://marklodato.github.io/visual-git-guide/index-es.html).

### Otras herramientas

### Weka 

[Weka](http://www.cs.waikato.ac.nz/ml/weka/) (Waikato Environment for Knowledge Acquisition) es una herramienta de Machine Learning y Data Minning escrito en Java. Con Weka podemos hacer Preprocessing data, clustering, classification, regression y ahora Big Data y datos con un driver JDBC.

Para instalar Weka en Ubuntu, desempaquetar el [archivo](http://prdownloads.sourceforge.net/weka/weka-3-6-13.zip) conteniendo a Weka en algún de tu preferencia y luego ir al directorio creado  (weka-3-6-13) y ejecutar

```bash
c-lara@Lara:~$java -Xmx1000M -jar weka.jar
```

Podemos aprender un poco de Weka usando el [video](https://www.youtube.com/watch?v=m7kpIBGEdkI) de Brandon Weinberg o el [canal de Youtube](https://www.youtube.com/user/WekaMOOC) de Weka.

### Mahout 

[Mahout](http://mahout.apache.org/) es un proyecto que es es parte del proyecto Apache. Una característica principal de Mahout es su integración con el paradigma Hadoop Map/Reduce para el procesamiento de datos a gran escala. Mahout soporta un gran número de algoritmos incluyendo:

* Naive Bayes Classifier.
* K Means Clustering.
* Recommendation Engine.
* Logistic Regression Classifier.
* Random Forest.

Lecturas

-  Mahout in Action de Sean Owen, Robin Anil, Ted Dunning y Ellen Friedman, Manning Publications, 2011.

### Spark
[Spark](http://spark.apache.org/) es un framework de análisis distribuido en memoría y nos permite ir más allá de las operaciones en batch de Hadoop MapReduce: procesamiento de streaming, machine learning (MLlib), cálculo de grafos (GraphX), integración con lenguje R (Spark R) y análisis interactivos. 

Al igual que su predecesor, MapReduce  que  logra prácticamente una relación lineal de escalabilidad, Spark mantiene la escalabilidad lineal y la tolerancia a fallos de MapReduce, pero amplía sus bondades gracias a varias funcionalidades:

* DAG (Directed Acyclic Graph).
* RDD (Resilient Distributed Dataset).


Algunas lecturas y referencias


- [¿What is Apache Spark?](https://www.mapr.com/ebooks/spark/).
- [First steps with Spark](http://spark.apache.org/screencasts/1-first-steps-with-spark.html).
- [Spark Examples ](https://spark.apache.org/examples.html).
- [Apache Spark Videos](https://www.youtube.com/user/TheApacheSpark/videos).
- [Spark vs Hadoop](https://acadgild.com/blog/spark-vs-hadoop/).

