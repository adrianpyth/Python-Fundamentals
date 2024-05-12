#La funcion print tiene dos palabras claves para cambiar un poco su comportamiento
#Las cuales son end y sep

print("Mi nombre es python", end="L")
print("Monty Python ")
# Para usarlo, es necesario conocer algunas reglas:

# Un argumento de palabra clave consta de tres elementos: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento;
# cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)

print("Mi","nombre", "es ", "monty", sep="-")

#La palabra clave sep se utiliza para separar por guiones o lo que pongas en entre las comilolas al igual que el argumento end los arguemntos 