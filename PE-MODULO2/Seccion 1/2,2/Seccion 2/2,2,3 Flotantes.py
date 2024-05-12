# Ahora es tiempo de hablar acerca de otro tipo, el cual esta designado para representar y almacenar los números que (como lo diría un matemático) tienen una parte decimal no vacía.

# Son números que tienen (o pueden tener) una parte fraccionaria después del punto decimal, y aunque esta definición es muy pobre, es suficiente para lo que se desea discutir.

# Cuando se usan términos como dos y medio o menos cero punto cuatro, pensamos en números que la computadora considera como números punto-flotante:

print(3.4)
print(3.)
#El punto decimal es esencialmente importante para reconocer números punto-flotantes en Python.


# Cuando se desea utilizar números que son muy pequeños o muy grandes, se puede implementar la notación científica.

# Por ejemplo, la velocidad de la luz, expresada en metros por segundo. Escrita directamente se vería de la siguiente manera: 300000000.

# Para evitar escribir tantos ceros, los libros de texto emplean la forma abreviada, la cual probablemente hayas visto: 3 x 108.

# Se lee: tres por diez elevado a la octava potencia.

# En Python, el mismo efecto puede ser logrado de una manera similar - observa lo siguiente:

print(3e10)

# La letra E (también se puede utilizar la letra minúscula e - proviene de la palabra exponente) la cual significa por diez a la n potencia.

# Nota:

# El exponente (el valor después de la E) debe ser un valor entero;
# La base (el valor antes de la E) puede ser un valor entero o flotante.

