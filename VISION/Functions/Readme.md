CONTENIDO DEL ALGORITMO:

A cada una de las funciones se le pasa la imagen de la flor correspondiente, la cual se le aplica un filtrado por color
para quedarnos solo con la silueta de la flor. En un principio utilizamos un threshold obtenido por prueba y error del color aproximado
de ese tipo de flor, pero era poco preciso e introudcia demasiado ruido en las imagenes que los procesados no podían eliminar, de modo
que se optó por filtrar mediante clusterización con k=2 grupos, obteniendo mejores resultados.
A continnuación, se realizan una serie de operaciones morfológicas, a saber: un opening para eliminar el ruido, y un closing para tapar
agujeros interiores a la máscara.
Para poder contar los pétalos utilizamos una combinación de dos algoritmos, añadiéndoles un peso a cada uno de ellose en función de cada
planta. Estos pesos se han determinado por prueba y error. 
El primer algoritmo es la detección de esquinas de Harris, sin embargo, a pesar de probar diferentes parámetros, no se consigue que cuente
exclusivamente los picos y valles entre pétalos, por lo que es necesario multiplicarlo por el peso anteriormente mentado.
El segundo algoritmo consiste en contar los defectos del polígono convexo, sin embargo no consigue representar todos los valles
entre pétalos, por lo que ha sido necesario también un factor de ajuste.
La densidad foliar es entonces extraida haciendo la media ponderada entre el resultado de estos dos algoritmos.
Para hallar un número que hable de la salud de la planta, nos hemos guiado por el número de pétalos que le pueden faltar a la planta,
ya que si aunque tenga todos los pétalos epro su color no sea el de una planta sana, el thresholding fallará y será un indicador de que
la panta no esta sana. Para tener una medida de si le faltan pétalos o no, utilizaremos unas relaciones geométricas extraidas a partir
del polígono convexo y del bounding box.
Aspect ratio: Es el resultado de dividir el ancho entre el alto de la bounding box, generalmente las flores son diametralmente
              simétricas, por lo que un aspect ratio cercano a 1 indica que no le faltan pétalos.
Extent: Es el resultado de dividr el área del objeto entre el área del bounding box, idealmente sería dividir el círculo inscrito
        en un cuadrado entre el áreade este, es decir, pi*R^2 / (2R)^2 -> pi/4 que es 0.7853981633975, por lo que valores cercanos a 
        este indican una buena salud en cuanto el número de pétalos de la flor.
Solidity: Es el resultado de dividir el área del objeto entre el área del polígono convexo, dado que una for puede estar sana y
          tener huecos entre los pétalos no hace falta que solidity sea cercano a uno, pero si se buscan valores altos.
Todos estos factores combinados forman un porcentaje de la salud de las plantas.
La función termina devolviendo la densidad de pétalos o foliar por radian y un porcentaje de la salud.

RESULTADOS CON EL ALGORITMO:

Los resultados del algoritmo son bastante diversos, ya que al no tener control de como enfocamos a las plantas o de la posición de estas
para con la cámara el algoritmo no podrá comportarse de manera satisfactoria en las imágenes que no cumplan unos ciertos requisitos.
Dichos requisitos son que el eje de la cámara sea normal al plano que define la flor, y que el fondo sea unicolor, ya sea vegetación,
suelo, cielo o un fondo negro, pero que solo sea la flor y el fondo, o la clusterización fallará.
En aquellas imágenes en las que se cumplían estos requisitos el algoritmo funcionaba relativamente bien, aunque tiene capacidad de mejora
debido a la naturaleza de obtención de los pesos de ponderación.
Sin embargo, a pesar de cumplir con las condiciones antes descritas, el algoritmo no se comporta bien para dos flores en concreto:
las rosas y los tulipanes. La razón radica en la forma de dichas flores, las cualestienen los pétalos demasiado entremezclados como
para poder hallar defectos en el polígono convexo y no tienen picos, por lo que el algoritmo de Harris es inútil.
Por lo tanto solo nos quedan las características geométricas, y aun así no son relevantes pues pueden adoptar formas muy irregulares
a pesar de tener todos los pétalos. El caso del diente de léon se obvia completamente la parte de la densidad foliar por el número
demasiado alto de pétalos y la forma en la que estos se entremezclan en la corona exterior de la flor, por lo que nos guiamos por
sus características geométricas.



