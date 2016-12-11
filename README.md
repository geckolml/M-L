##  Curso: Tópicos de investigación (Machine Learning)

Lectura previa:

* Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython de Wes McKinney. 

## Temario

* Introducción 
 - Conceptos básicos.
 
* Aprendizaje Supervisado
 - Nociones  sobre  aprendizaje supervisado. LMS.
 - Regresión logística. Perceptron. Familia exponencial.
 - Algoritmos de aprendizaje generativo. Análisis de  discriminante Gaussiano. Naive Bayes.
 - Máquina de Soporte Vectorial.
 - Selección de modelos y selección de características .
 - Bagging y Boosting (Ensemble methods).


* Teoría del aprendizaje
 - Solución bias-varianza. Unión y cotas de Chernoff-Hoeffding.
 - VC dimensión .
 - Notas cómo utilizar algoritmos de aprendizaje.

* Aprendizaje no Supervisado

 - Clustering. K-medias.
 - EM. Mixture Gaussiana.
 - Análisis factorial.
 - PCA (Análisis de componentes principales).
 - ICA (Análisis de componentes independientes).

## Libros de Texto

1 .Machine Learning: Hands-On for Developers and Technical Professionals, Jason Bell, Wiley 2015.

2 .Coding The Matrix Linear Algebra Through Computer Science Applications, Newtonian Press, Phillip Klein, 2012.

3 .Numerical Python: A Practical Techniques Approach for Industry, Robert Johansson, Apress 2015.

4 .Fundamentals of Machine Learning for Predictive Data Analytics: Algorithms, Worked Examples, and Case Studies, Aoife D'Arcy, Brian Mac Namee, John D. Kelleher, MIT 2015.

5 .Mastering Machine Learning With scikit-learn, Gavin Hackeling, Packt Publishing, 2014.

6 .Probability: The Analysis of Data, Volumen 1, Guy Lebanon. El libro se puede leer de manera online en [theanalysisofdata.com](http://theanalysisofdata.com/).

7 . Statistical inference for data science, Brian Caffo (Con código en R). El libro pueder se leído en Leanpub [Little Inference Book](https://leanpub.com/LittleInferenceBook).

8 .Numerical Algorithms: Methods for Computer Vision, Machine Learning and Graphics, Justin Solomon, CRC Press, 2015.

9 .An Introduction to Statistical Learning, Springer Texts in Statistics, Gareth James, Daniela Witten, Trevor Hastle y Robert Tibshirani, 2013.

10 .Business Intelligence in Plain Language: A practical guide to Data Mining and Business Analytics, Jeremy Kolbs. Applied Data Labs Inc, 2012.

11 . groking Algorithms, An illustred guide for programmers and other curious people, Aditya Y. Bhargava, Manning 2016.

12 . Python Machine Learning, Sebastian Raschka, Pack Publishing, 2015.

## Herramientas a  usar 


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


### Latex 

[LaTeX](https://www.latex-project.org/) es como un lenguaje de alto nivel para TeX, que es un sistema de preparación de documentos creados por Donald E. Knuth. Latex es en si un conjunto de macros y convenciones pensadas de modo que con pocas intrucciones seamos capaces de producir un documento de calidad profesional, como lo son los artículos  publicados por la comunidad científica. Mayor información se puede encontrar en :

- [Arbitrary Latex reference](http://latex.knobs-dials.com/).
- [TeX - LaTeX Stack Exchange](http://tex.stackexchange.com/)
- [Wikibooks Latex](https://en.wikibooks.org/wiki/LaTeX).

En ubuntu, la manera facil de instalar Latex, es usando `TexLive`

```bash
c-lara@Lara:~$sudo apt-get install texlive-latex-base texlive-latex-recommended texlive-latex extra
```
Se pueden instalar paquetes extras, que no se encuentran en los paquetes anteriores. Por ejemplo los paquetes relacionados con algoritmos como `algorithm.sty` se puede instalar con

```bash
c-lara@Lara:sudo apt-get install texlive-science
```

Si se desea instalar todo los paquetes de `TexLive`, se puede hacer de la siguiente manera:


```bash
c-lara@Lara:sudo apt-get install texlive-full
```

Una página interesante para aprender los símbolos de latex, se pueden encontrar en [detexify](http://detexify.kirelabs.org/classify.html).

Un editor muy completo para trabajar con latex es: [TeXstudio](http://www.texstudio.org/), que se puede instalar en Ubuntu de la siguiente manera:

```bash
c-lara@Lara:wget http://download.opensuse.org/repositories/home:/jsundermeyer/xUbuntu_14.04/amd64/texstudio_2.10.8-5.1_amd64.deb
c-lara@Lara :sudo dpkg -i texstudio_2.10.8-5.1_amd64.deb
```


### MongoDB

[MongoDB](https://www.mongodb.org/) es una sistema de base de datos NoSQL de código abierto utilizado  en aplicaciones web modernas, escrito en C++ le confiere cierta cercanía a los recursos del hardware, de modo que es bastante rápido a la hora de ejecutar sus tareas. MongoDB es una base de datos orientada a documentos, es decir guarda los datos en documentos que son almacenados en un representación binaria de JSON, llamado BSON.

Genbeta:dev tiene una lista de [artículos](http://www.genbetadev.com/bases-de-datos/una-introduccion-a-mongodb) para empezar en el mundo de las bases de datos NoSQL y MongoDB. Es interesantes ver los videos colgados en Youtube sobre MongoDB.

- [¿Qué es MongoDB?](https://www.youtube.com/watch?v=CvIr-2lMLsk).
- [Comparación de SQL y MongoBD](https://www.youtube.com/watch?v=kDSjVTpu8kI).
- [Contruyendo tu primera aplicación con MongoDB](https://www.youtube.com/watch?v=ClAQEARNUoQ).

Para poder instalar en Ubuntu, es preferible revisar la [documentación](http://docs.mongodb.org/master/tutorial/install-mongodb-on-ubuntu/) desde la página de MongoDB.




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



### R y Rstudio

[R](https://www.cran.r-project.org/) y [RStudio](https://www.rstudio.com/) . RStudio es un IDE para R. Es software libre con licencia GPLv3 y se puede ejecutar sobre distintas plataformas  o incluso desde la web usando [RStudio Server](https://support.rstudio.com/hc/en-us/articles/200552306-Getting-Started).


```bash
c-lara@Lara:~$ wget https://download1.rstudio.org/rstudio-0.99.893-amd64.deb
c-lara@Lara:~$sudo dpkg -i *.deb
c-lara@Lara:~$rm *.deb
```

Referencias

- [Basic Tutorial of Rstudio](http://web.cs.ucla.edu/~gulzar/rstudio/basic-tutorial.html).
- [Webinars and Videos of Rstudio](https://github.com/rstudio/webinars).

### Spyder 

[Spyder](https://github.com/spyder-ide/spyder]) es un entorno de desarrollo para Python, con múltiples características como edición avanzada, testeo, depuración y características de instrospección, además de la capacidad de utilizar vía Ipython las librerías científicas de Numpy, Simpy o MatplotLib.  Si se tiene instalado Anaconda, entonces solo basta escribir en el terminal lo siguiente

```bash
c-lara@Lara:~$ spyder
``` 



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

## Artículos

- [Machine Learning introduction](https://jeremykun.com/2012/08/04/machine-learning-introduction/).
- [Tutorial of Scikit-Learn for Classifier](http://www.kdnuggets.com/2016/01/scikit-learn-tutorials-introduction-classifiers.html).
- [Deception of supervised learning](http://www.kdnuggets.com/2016/09/deception-of-supervised-learning.html).
- [Approaching (Almost) Any Machine Learning Problem](http://blog.kaggle.com/2016/07/21/approaching-almost-any-machine-learning-problem-abhishek-thakur/).
- [Metric spaces introduction](https://jeremykun.com/2012/08/26/metric-spaces-a-primer/).
- [k-nearest-neighbors](https://jeremykun.com/2012/08/26/k-nearest-neighbors-and-handwritten-digit-classification/).
- [Inner product spaces](https://jeremykun.com/2011/07/25/inner-product-spaces-a-primer/).
- [Geometric interpretation of covariance matrix](http://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/).
- [Eigenvectors, PCA,covariance and entropy](http://deeplearning4j.org/eigenvector).
- [PCA, eigenvectors and eigenvalues](http://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues).
- [Clustering key-terms](http://www.kdnuggets.com/2016/10/clustering-key-terms-explained.html)
- [The Perceptron, and All the Things it can't Perceive](https://jeremykun.com/2011/08/11/the-perceptron-and-all-the-things-it-cant-perceive/).
- [Trees](https://jeremykun.com/2012/09/16/trees-a-primer/).
- [Decision trees ](https://jeremykun.com/2012/10/08/decision-trees-and-political-party-classification/).
- [k-Means Clustering ](https://jeremykun.com/2013/02/04/k-means-clustering-and-birth-rates/).
- [Support Vector Machine  ](http://www.analyticsvidhya.com/blog/2015/10/understaing-support-vector-machine-example-code/).
- [Set theory](https://jeremykun.com/2011/07/09/set-theory-a-primer/).
- [Probability theory introduction](https://jeremykun.com/2013/01/04/probability-theory-a-primer/).
- [Decision Tree concise technical overview](http://www.kdnuggets.com/2016/10/decision-trees-concise-technical-overview.html)
- [Linear Regression](https://jeremykun.com/2013/08/18/linear-regression/).
- [Tree decision and modeling](http://www.analyticsvidhya.com/blog/2016/04/complete-tutorial-tree-based-modeling-scratch-in-python/).
- [Practical Guide to implementing Neural Networks in Python (using Theano)](http://www.analyticsvidhya.com/blog/2016/04/neural-networks-python-theano/).
- [ Naives Bayes explained](http://www.analyticsvidhya.com/blog/2015/09/naive-bayes-explained/).
- [Introduction boosting algorithms for machine learning](http://www.analyticsvidhya.com/blog/2015/11/quick-introduction-boosting-algorithms-machine-learning/).
- [How Bayesian Inference works](http://www.kdnuggets.com/2016/11/how-bayesian-inference-works.html)
- [Quick introduction Neural network](http://www.kdnuggets.com/2016/11/quick-introduction-neural-networks.html)


## Lecturas

- [Tutoriales de Machine Learning](https://github.com/ujjwalkarn/Machine-Learning-Tutorials).
- [Top Algorithms Used by Data Scientists](http://www.kdnuggets.com/2016/09/poll-algorithms-used-data-scientists.html)
- [Una guía de bolsillo para la Ciencia de datos](http://www.kdnuggets.com/2016/04/pocket-guide-data-science.html).
- [Learning from Data: Machine learning course](https://work.caltech.edu/lectures.html).
- [El cookbook del paquete Scipy ](http://scipy-cookbook.readthedocs.org/).
- [Página principal de Scikit-learn](http://scikit-learn.org/stable/index.html).
- [A visual introduction to machine learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/).
- [Difference machine learning and learning statistical modeling](http://www.analyticsvidhya.com/blog/2015/07/difference-machine-learning-statistical-modeling/).
- [Weka – GUI way to learn Machine Learning](http://www.analyticsvidhya.com/learning-paths-data-science-business-analytics-business-intelligence-big-data/weka-gui-learn-machine-learning/).
- [Uso de Pandas, para Análisis exploratorio de datos ](http://www.analyticsvidhya.com/blog/2014/08/baby-steps-python-performing-exploratory-analysis-python/).
- [Análisis de los pro y contras de ciertos  algoritmos en Machine Learning](http://www.lauradhamilton.com/machine-learning-algorithm-cheat-sheet).
- [7 pasos para empezar con Machine Learning con Python ](http://www.kdnuggets.com/2015/11/seven-steps-machine-learning-python.html).
- [Un tour sobre los principales algoritmos de Machine Learning](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/).
- [Algoritmos de Machine Learning](http://www.analyticsvidhya.com/blog/2015/08/common-machine-learning-algorithms/).
- [13 framework usados en Machine Learning](http://www.infoworld.com/article/3026262/data-science/13-frameworks-for-mastering-machine-learning.html).
- [Modelado predictivo, aprendizaje supervisado y clasificación de patrones](http://sebastianraschka.com/Articles/2014_intro_supervised_learning.html).
- [R y MongoDb](https://gist.github.com/Btibert3/7751989).
- [Weka 3, software de Data Mining en Java ](http://www.cs.waikato.ac.nz/ml/weka/).
- [Notas de Scikit-Learn como herramienta de Machine Learning](http://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/).
- [Machine Learning Cheat Sheet for scikit-learn](http://peekaboo-vision.blogspot.pe/2013/01/machine-learning-cheat-sheet-for-scikit.html).
- [Tutorial de datacamp de Machine Learning en R](http://blog.datacamp.com/machine-learning-in-r/).
- [Ciencia de datos con R, Analytics, Big Data, Text Mining](http://togaware.com/onepager/).
- [Tutorial completo acerca de ciencia de datos en R ](http://www.analyticsvidhya.com/blog/2016/02/complete-tutorial-learn-data-science-scratch/).
- [Visualización con d3.js para la Ciencia de Datos y Inteligencia de negocios](http://www.analyticsvidhya.com/learning-paths-data-science-business-analytics-business-intelligence-big-data/newbie-d3-js-expert-complete-path-create-interactive-visualization-d3-js/).
- [Un tour de algoritmos de machine learning](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/).
- [Machine learning en gráficos](http://www.denizyuret.com/2014/02/machine-learning-in-5-pictures.html).
- Algunos canales de YouTube para aprender Inferencia estadistica:
  * [Brandon Foltz](https://www.youtube.com/user/BCFoltz).
  * [jbstatistics](https://www.youtube.com/user/jbstatistics).
  * [Analytics University](https://www.youtube.com/channel/UC2XO4HDxzfMOZIV1l795g1Q).
  * [NPTEL HRD](https://www.youtube.com/user/nptelhrd).

## Otros tópicos
- [Eigenfaces for Facial recognition](https://jeremykun.com/2011/07/27/eigenfaces/).
- [Boosting and AdaBoost](https://jeremykun.com/2015/05/18/boosting-census/).
- [Machine learning as a batch process](http://onlinelibrary.wiley.com/doi/10.1002/9781119183464.ch10/summary). Libro de Jason Bell: Machine Learning- Hands-on for developers and technical professionals.
- [Árboles aleatorios en python y R](http://www.analyticsvidhya.com/blog/2015/09/random-forest-algorithm-multiple-challenges/).
- [Machine Learning for Static Ranking](http://www.msr-waypoint.com/pubs/68149/staticrank.pdf).
- [Inductive Learning Algorithms and Representations for Text Categorization](http://www.miv.t.u-tokyo.ac.jp/ishizuka/pr-class/Dumais-CIKM98.pdf).
- [Genetic Algorithms](http://lethain.com/genetic-algorithms-cool-name-damn-simple/).
- [Gaussian Process for Machine Learning](http://www.gaussianprocess.org/gpml/chapters/).
- [CrossValidation](https://en.wikipedia.org/wiki/Cross-validation_(statistics))
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/).
