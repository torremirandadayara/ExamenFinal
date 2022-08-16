diccionario = {"codigo": ["001", "002", "003", "004", "005"],
               "nombre": ["Juan", "Carlos", "Jay", "Pedro", "Matias"],
               "cursos": ["Ingles", "Ciencias Sociales", "Matematica"]}

listaproductos = []
promedio = 0
resp = "s"
while resp == "s":
    codigoIn = input("Ingrese el codigo del alumno: ")
    cursoTemp = input("Ingrese el nombre del curso: ")
    nota = int(input("Ingrese la primera nota: "))
    nota1 = int(input("Ingrese la segunda nota: "))
    nota2 = int(input("Ingrese la tercera nota: "))
    x = 0
    for i in diccionario["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            nombreTemp = diccionario["nombre"][x]
            promTemp = nota + nota1 + nota2
            promedio = promTemp / 3
            registro = codigoTemp, '\t', nombreTemp, '\t' '\t', cursoTemp, '\t', nota, nota1, nota2
            listaproductos.append(registro)
        x += 1
    print("---------------------------------------------")
    resp = input("¿Desea seguir ingresando datos? : s/n ")

print("Cod", '\t', "Nombre", '\t', "Curso", '\t' '\t', "Notas")
for x in listaproductos:
    print(*x, end="\n")

print("El promedio es: ", promedio)
