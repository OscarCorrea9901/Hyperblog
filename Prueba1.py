#print("Mi nombre es ", end=" \"")
#print("Monty Python.")
#print("Mi", "nombre", "es", "Monty", "Python.", sep="\n")
#print("Mi", "nombre", "es", sep="_", end="*")
#print("Monty", "Python.", sep="*", end="*\n")
beatles=[]

# paso 1
print("Paso 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCarney")
beatles.append("George Harrison")
# paso 2
print("Paso 2:", beatles)
for i in range(2):
    aux = input("Ingrese dos integrantes más: ")
    beatles.append(aux)

# paso 3
print("Paso 3:", beatles)
del beatles[3]
del beatles[3]
# etapa 4
print("Paso 4:", beatles)
beatles.insert(0,"Ringo Starr")
# paso 5
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
