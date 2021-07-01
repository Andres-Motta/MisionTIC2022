# Reto 4

Una familia colecciona las laminas de Panini de los mundiales, curiosamente del 2018 le quedaron unas láminas pendientes y están buscando lugares que tengan catálogo de ellas para poder comprarlas y llenar el álbum. En la tienda de la Universidad Nacional se puede ver el catálogo de las láminas disponibles en formato JSON donde muestra el numero de la lámina y su respectivo precio asociado; realice un programa que dado el diccionario de láminas disponibles y la lista de láminas pendientes de la familia entregue como salida el costo total de comprar las láminas en la tienda de la universidad y la lista de las láminas conseguidas, las cuales le ayudarán a la familia a saber cuánto le cuesta conseguir las láminas la tienda y cuáles van a conseguir.

## Input
* {"312": 1230, "94": 1545, "50": 1378, "360": 2240, "1": 1228, "37": 2009, "240": 1493} <br>
* 312 5 57 82 500 37 1

## Output
* 4467 <br>
* 312 37 1

# Solucion

Dado que las dos entradas por consolas son strings, se debe convertir dichas entradas a un formato manipulable, en el caso del primer input a un diccionario y el segundo a una lista.

```python
catalogue = json.loads(catalogue)             #convierte el string a diccionario
stickersNeeded = stickersNeeded.split(' ')    #convierte el string a lista
```

Posteriormente se definen dos variables las cuales almacenaran la informacion importante que es el **precio total**, el cual estara definido como un int y las **fichas que se han encontrado**, las cuales se almacenaran en una lista de manera individual.

```python
price = 0             # Guarda el precio total de los stickers encontrados
stickersFound = []    # Guarda el numero de los stickers encontrados
```

Una vez definidas las variables, el siguiente paso es recorrer la lista de stickers que la persona necesita (**stickersNeeded**) y comparar si cada stciker se encuentra en el diccionario (**catalogue**). Si el sticker se encuentra en el catalogo, se debe sumar a la variable **price** el precio del mismo y se debe agregar el numero de dicho sticker en la lista **stickersFound**.

```python
for sticker in stickersNeeded:             # sticker = 312 || stickersNeeded = [312, 5, 57, 82, 500, 37, 1]
    if sticker in catalogue:               # 312 in catalogue => si
        price += catalogue[sticker]        # price += catalogue['312'] => 1230
        stickersFound.append(sticker)      #stickersFound = ['312']
```

El ciclo se repite para todos los elementos en stickersNeeded.

Finalmente se imprimen las variables **price** y **stickersFound** sin olvidar convertir la variable stickersFound en un string con el metodo join

```python
print(price)
print(' '.join(stickersFound))
```

Todo el codigo anterior es posible refactorizarlo para poder utilizarlo mediante el llamado de una funcion.

```python
def searchStickers(catalogue, stickersNeeded):
  price = 0
  stickersFound = []

  catalogue = json.loads(catalogue)
  stickersNeeded = stickersNeeded.split(' ')

  for sticker in stickersNeeded:
    if sticker in catalogue:
      price += catalogue[sticker]
      stickersFound.append(sticker)
  
  return price, stickersFound
```

Funcion que devuelve una tupla la cual es necesario desempaquetar para su posterior uso

```python
price, stickersFound = searchStickers(catalogue, stickers)
```
