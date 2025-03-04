
"""
Ejercicio 1: Encuentra los números que aparecen una sola vez
Dada una lista de números, encuentra cuáles aparecen solo una vez.
"""
# numeros = int(input("Digite 10 números: ") for _ in rang(10));
# ##### SOLUCIÓN SÍN MÉTODO AVANZADO
entrada = [4, 3, 2, 4, 1, 3, 2, 5, 6] 
conteo = {}
for num in entrada:
    if num in conteo:
        conteo[num] += 1
    else:
        conteo[num] = 1

unico = [num for num in entrada if conteo[num] ==1  ]
print(f"Números que no se repiten: {unico}")
print("_______________________________________________________________________________________")

# ##### SOLUCIÓN CON MÉTODO AVANZADO
entrada = [4, 3, 2, 4, 1, 3, 2, 5, 6] 
conteo = {}
for num in entrada:
    conteo[num] = conteo.get(num, 0)+1

unicos = [num for num in entrada if conteo[num]==1]
print(f"Números que no se repiten: {unicos}")
print("_______________________________________________________________________________________")
   
"""
Ejercicio 2: Ordena una lista de tuplas por el segundo elemento
Dada una lista de tuplas (nombre, edad), ordena la lista según la edad de menor a mayor.
ejemplo: 
        personas = [("Ana", 25), ("Juan", 30), ("Luis", 20)]  
        # Salida esperada: [("Luis", 20), ("Ana", 25), ("Juan", 30)]
"""