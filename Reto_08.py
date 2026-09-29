"""En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]"""

list = [20, 50, "Curso", 'Python', 3.14]

print("Lista original:", list)

dato1 = input("Ingrese el primer dato para sustiuir: ")
dato2 = input("Ingrese el segundo dato para sustiuir: ")

list[0] = dato1
list[1] = dato2

print("Lista modificada:", list)