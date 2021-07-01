# Reto 3

Junior, Katerine y la Abuela ahora van regreso a casa, no sin antes pasar por los helados apostados anteriormente, ya que aún no tienen batería en sus celulares, los buses están muy llenos y les da cosita meterse a lugares tan repletos con su abuela; deciden irse caminando a la casa de regreso y pensar en qué juego inventarse para pasar el rato.

La abuela les dice que hagan la cuenta de las iniciales de las placas de los taxis que ven camino a la casa. Realice un programa que reciba una lista con las primeras letras de las placas vistas (separadas por un espacio) e imprima en una fila las letras que fueron viendo (separadas por un espacio), y en otra fila las veces seguidas que vieron dicha letra (separadas por un espacio).

## Input
* D D D D Q Q Q S S S F F F C W W W F Q Q H H Q Q Q

## Output
* D Q S F C W F Q H Q <br>
* 4 3 3 3 1 3 1 2 2 3

# Solucion

![LogicaR3](https://github.com/Juan-Motta/MisionTIC2022/blob/main/Retos/Reto3/img/LogicaR3.png)

Se recibe una entrada la cual es un string que contiene las iniciales de las placas separados por espacio, por lo tanto para poder manipular dicho string de una manera mas sencilla, es posible eliminar los espacios en blanco de separacion.

```python
data = str(input())             # Lee la entrada y la almacena en data
data = data.replace(' ', '')    # Elimina todos los espacios en blanco 'D D D D Q Q Q ...' => 'DDDDQQQ...'
```

Posteriormente se definen dos variables las cuales se encargaran de almacenar las iniciales de las placas **cont_letra** y el numero de veces que se repiten de manera seguida **cont_num**

```python
cont_letra = []   # Guarda la inicial de la placa
cont_num = []     # Guarda el numero de veces que se repite de manera seguida la placa en el mismo orden
```

Una vez definidas las variables el primer paso es recorrer el listado de placas **data**, y se analizan 3 casos:
* si es el primer dato, se agrega la primera letra a la lista que almacena las placas **cont_letra** y se agrega el valor de 1 a la lista **cont_num** el cual indica las veces que se va repitiendo la letra seleccionada, esto debido a que las listas inicialmente estaran vacias.
* si el dato es el primero y este es igual al ultimo dato almacenado en la lista **cont_letra**, se le suma 1 al ultimo valor de la lista **cont_num**
* si el dato no es el primero y este es diferente al ultimo dato almacenado en la lista **cont_letra**, se agrega este valor a la lista **cont_letra** y se agrega el valor de 1 a la lista **cont_num**

```python
# CASO 1 - PRIMERA LETRA
for letra in data:                                       # letra = D in data = [DDDDQQQ...] || primera letra
  if (cont_letra == []):                                 # [] == [] => si  ||  cont_letra = []  
    cont_letra.append(letra)                             # cont_letra = ['D']
    cont_num.append(1)                                   # cont_num = [1]
  elif (letra == cont_letra[-1]):
    cont_num[-1] += 1
  elif (letra != cont_letra[-1]):
    cont_letra.append(letra)
    cont_num.append(1)
    
#CASO 2 - LETRA IGUAL A LA ANTERIOR
for letra in data:                                       # letra = D in data = [DDDDQQQ...] || segunda letra
  if (cont_letra == []):                                 # ['D'] == [] => no  ||  cont_letra = ['D'] 
    cont_letra.append(letra)
    cont_num.append(1)
  elif (letra == cont_letra[-1]):                        # D == D => si  ||  cont_letra[-1] = D
    cont_num[-1] += 1                                    # cont_num[-1] += 1  ||  cont_num = [2]
  elif (letra != cont_letra[-1]):                        # D != ['D'] => no  ||  cont_letra[-1] = ['D'] 
    cont_letra.append(letra)
    cont_num.append(1)
    
#CASO 2 - LETRA DIFERENTE A LA ANTERIOR
for letra in data:                                      # letra = Q in data = [DDDDQQQ...]  ||  quinta letra
  if (cont_letra == []):                                # ['D'] == [] => no  ||  cont_letra = ['D']
    cont_letra.append(letra)
    cont_num.append(1)
  elif (letra == cont_letra[-1]):                       # Q == D => no  ||  cont_letra[-1] = D
    cont_num[-1] += 1
  elif (letra != cont_letra[-1]):                       # Q != D => si  ||  cont_letra = ['Q'] 
    cont_letra.append(letra)                            # cont_letra = ['D', 'Q'] 
    cont_num.append(1)                                  # cont_num = [4, 1]
```

Como el primer if y el ultimo if contienen el mismo bloque de codigo en su interior, estos dos if se unen para simplificar el codigo mediante el uso de la expresion or (se cumple uno o el otro)

```python
for letra in data:
  if (cont_letra == [] or letra != cont_letra[-1]):
    cont_letra.append(letra)
    cont_num.append(1)
  elif (letra == cont_letra[-1]):
    cont_num[-1] += 1
```

Finalmente la lista **cont_letra** se convierte a un string separando cada elemento con espacio mediante el uso del metodo join y la lista **cont_num** dado que contiene numeros en su interior y el metodo join no permite operar datos de tipo int, los valores de la lista deben ser convertidos a caracteres uno por uno.

```python
cont_letra = ' '.join(cont_letra)
cont_num = [str(num) for num in cont_num]   # cambia cada numero de la lista a tipo string 
cont_num = ' '.join(cont_num)
```
