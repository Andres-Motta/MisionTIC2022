data = str(input())
data = data.replace(' ', '')

cont_letra = []
cont_num = []

for letra in data:
  if (cont_letra == [] or letra != cont_letra[-1]):
    cont_letra.append(letra)
    cont_num.append(1)
  elif (letra == cont_letra[-1]):
    cont_num[-1] += 1

cont_letra = ' '.join(cont_letra)
cont_num = [str(num) for num in cont_num]
cont_num = ' '.join(cont_num)
