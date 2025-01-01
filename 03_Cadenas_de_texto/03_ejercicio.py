# Declarar una variable text

my_string = "Aprendiendo Python"
print(my_string)
print(len(my_string))

# Concatenar dos cadenas

first_string = "Hola"
second_string = "Python"

print(first_string + " " + second_string)

# Crear cadena con salto de linea

print("\n Hola! Este es un salto de línea")

# Formateo de cadenas

name, surname, age = "Iza", "Blake", 23
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# Desempaquetar caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Extraer slice

language_slice = language[1:3]
print(language_slice)

# Invertir cadenas

reversed_language = language[ ::-1]
print(reversed_language)

# Convertir cadenas

lenguaje = "aprendiendo python"
print(lenguaje.upper())

# Contar las veces de la letra n

pala = "Programación en Python"
print(pala.count("n"))

# Verificar la cadena

num = "12345"
print(num.isnumeric())
