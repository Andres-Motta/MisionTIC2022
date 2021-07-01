# Reto 1

Una lavandería quiere listar cual es cual es la capacidad de trabajo que toma realizar las tareas diarias a la hora de  realizar la limpieza a las prendas recibidas por día. Los factores para listar son  el tiempo de preparación de las prendas, su tiempo de lavado y el numero de tandas de secado. Estos factores son listados para mantener un histórico de su operación y finalmente definir la cantidad de prensistas que necesitan para organizar dichas prendas.

El tiempo de preparación de las prendas no suele ser tanto, ya que generalmente por cada prenda recibida suelen gastar un minuto marcarla y separarla para su siclo de lavado. El tiempo de lavado y tiempo de secado es determinado a partir del numero de prendas recibidas también; usualmente el tiempo de lavado es en minutos el doble del numero de prendas mas unos cuatro minutos que son los que se demoran en programar el tipo de ciclo de lavado de las prendas. Cada tanda de secado de las prendas suele determinarse a partir de la quinta parte del tiempo de lavado más el tiempo de preparación de las prendas ya que cuentan con un secador pequeño al que le caben pocas prendas (tome la función piso para redondear el número de secadas).

Finalmente, de acuerdo al número de tandas de secado de las prendas, la lavandería sabe el número de prensistas que se encargan de organizar la ropa luego de todo su proceso de lavado. Si se realizan menos de 20 tandas, la lavandería requiere un prensista; si se realizan entre 21y 30 tandas, la lavandería requiere dos prensistas, entre 31 y 50 la lavandería requiere tres prensistas y en caso de que se requieran más de 50, como la lavandería tiene recursos limitados requeriría máximo cuatro prensistas y que lo que quede pendiente se organice el siguiente día.

Elabora un programa que permita, dado el número de prendas recibidas por día, conocer los valores obtenidos en los diferentes factores a medir en la lavandería (tiempo de preparación de prendas, tiempo de lavado, número de tandas de secado), así como el número de prensistas que se utilizarán para organizar dichas prendas.

## Input
* 47

## Output
* 47 98 29
* dos
