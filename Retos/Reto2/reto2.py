op_j = str(input())
op_k = str(input())
respuesta = str(input())

p_j = 0
p_k = 0
resultado = ''


def comparacion(letra, opciones):
	"""Funcion que valida si una letra se encuentra en un string y retorna 1 si se cumple y 0 si no"""
	if letra in opciones:
		return 1
	return 0


def puntuacion(p_j, p_k):
	"""Funcion que compara dos valores enteros y devuelve una letra dependiendo si el valor es mayor, menor o igual"""
	if p_j > p_k:
		return 'J'
	elif p_j < p_k:
		return 'K'
	elif p_j == p_k:
		return 'L'


for letra in iniciales:
	p_j += comparacion(letra, op_j)
	p_k += comparacion(letra, op_k)

	resultado += puntuacion(p_j, p_k)

print(resultado)
