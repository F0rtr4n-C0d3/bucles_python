# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))

# fin....

fin= int(input('Ingrese el último número de la secuencia\n'))

# for ... in range(....)
for numeros in range(inicio,fin):
    print('Los números son ',numeros)

# Imprimir el valor de la sumatoria

for sumatoria in (inicio,fin):
    suma = numeros + sumatoria
    print('La sumatoria de {} y {} es {}'.format(numeros,sumatoria,suma))

print('terminamos')
