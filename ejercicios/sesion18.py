def compras_por_pais (pais):
  """Funcion que permite conocer el numero de compras realizadas en un pais dado"""
  compras = 0
  with open('files/SalesJan2009.csv', 'r') as file:
    for line in file:
      line = line.split(',')
      if pais == line[7]:
        compras += 1
  file.close()
  return compras

print(compras_por_pais('United Kingdom'))

def compras_por_medio (pais):
  """Funcion que permite conocer el numero de compras realizadas con un medio dado"""
  compras = 0
  with open('files/SalesJan2009.csv', 'r') as file:
    for line in file:
      line = line.split(',')
      if pais == line[3]:
        compras += 1
  file.close()
  return compras

print(compras_por_medio('Visa'))
