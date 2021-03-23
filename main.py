"""Ejercicios con vectores en python."""

vector = [
        int(item) for item in input(
            "ingrese los elementos del vector base : "
            ).split()
        ]


def suma_resta_produc_vector(v1, v2):
    """Calcular la suma , resta y producto de dos vectores."""
    v3_suma = suma(v1, v2)
    v3_resta = resta(v1, v2)
    v3_produc = producto(v1, v2)
    return v3_suma, v3_resta, v3_produc


def sumatoria(vector):
    """Calcular la sumatoria de todos los elementos en un vector."""
    acum = 0
    for i in range(len(vector)):
        acum += vector[i]
    return acum


def productoria(vector):
    """Calcular la productoria de todos los elementos en un vector."""
    acum = 1
    for i in range(len(vector)):
        acum = acum * vector[i]
    return acum


def suma(v1, v2):
    """Suma dos vectores."""
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3


def resta(v1, v2):
    """Resta dos vectores."""
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]-v2[i])
    return v3


def producto(v1, v2):
    """Multiplica dos vectores."""
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]*v2[i])
    return v3


def num_mayor_menor(vector):
    """Obtiene el numero mayor y el menor de un vector."""
    numero_mayor = max(vector, key=int)  # Numero mayor
    numero_menor = min(vector, key=int)  # Numero menor
    return numero_mayor, numero_menor


def cant_par_impar_primo(vector):
    """Cuenta los pares,impares y primos de un vector."""
    cant_par = 0
    cant_impar = 0
    cant_primo = 0
    for v in vector:
        if v % 2 == 0:
            cant_par += 1
        if v % 2 != 0:
            cant_impar += 1
        if es_primo(v):
            cant_primo += 1
    return cant_par, cant_impar, cant_primo


def es_primo(num):
    """Valida si un numero es primo."""
    for n in range(2, num):
        if num % n == 0:
            # No es primo
            return False
    # Es primo
    return True


def vector_2_partes(vector):
    """Divide un vector en dos vectores nuevos."""
    long = len(vector)
    v1 = []
    v2 = []
    if long % 2 == 0:
        for i in range(0, (int)(long/2)):
            v1.append(vector[i])
        for i in range((int)(long/2), (int)(long)):
            v2.append(vector[i])
        return v1, v2
    else:
        vector.pop((int)(len(vector)/2))
        long = len(vector)
        for i in range(0, (int)(long/2)):
            v1.append(vector[i])
        for i in range((int)(long/2), (int)(long)):
            v2.append(vector[i])
        return v1, v2


def es_simetrico(vector):
    """Valida si un vector es simetrico."""
    v1, v2 = vector_2_partes(vector)
    if v1 == list(reversed(v2)):
        return True
    else:
        return False


def union(vector1, vector2):
    """Hace la union de dos vectores."""
    vector_union = vector1 + vector2
    return vector_union


def interseccion(vector1, vector2):
    """Hace la interseccion de dos vectores."""
    vector_interseccion = [value for value in vector1 if value in vector2]
    return vector_interseccion


def diferenciaAB(vector1, vector2):
    """Hace la diferencia del vector 1 con el vector 2."""
    return (
        list(
            list(set(vector1)-set(vector2)) + list(set(vector2)-set(vector1))
            )
        )


def diferenciaBA(vector1, vector2):
    """Hace la diferencia del vector 2 con el vector 1."""
    return (
        list(
            list(set(vector2)-set(vector1)) + list(set(vector1)-set(vector2))
            )
        )


print(f"vector base : {vector}\n")

# punto 1
print("punto 1 :")
print(f"sumatoria del vector {vector} : {sumatoria(vector)}")
print(f"productoria del vector {vector} : {productoria(vector)}")
num_mayor, num_menor = num_mayor_menor(vector)
print(f'numero mayor : {num_mayor}\nnumero menor : {num_menor}\n')

# punto 2
print("punto 2 :")
cant_par, cant_impar, cant_primo = cant_par_impar_primo(vector)
print(f'pares : {cant_par} - impares : {cant_impar} - primos : {cant_primo}\n')

# punto 3
print("punto 3 :")
print("porfavor ingrese el vector de la siguiente manera :")
print("ejemplo : 1 2 3 4 5 6 7 => [1, 2, 3, 4, 5, 6, 7]")
lst1 = [
        int(item) for item in input(
            "ingrese los elementos del vector 1 : "
            ).split()
        ]
lst2 = [
        int(item) for item in input(
            "ingrese los elementos del vector 2 : "
            ).split()
        ]

if len(lst1) == len(lst2):
    v3_suma, v3_resta, v3_produc = suma_resta_produc_vector(lst1, lst2)
    print(f'suma de los vectores : {v3_suma}')
    print(f'resta de los vectores : {v3_resta}\n')
else:
    print("ambos vectores deben ser del mismo tamaño\n")

# punto 4
print("punto 4 : ")
print(f"vector : {vector}")
print(f'numero mas repetido : {max(set(vector), key=vector.count)}\n')

# punto 5
print("punto 5 : ")  # vector.copy() crea una copia del vector original
print(f"vector : {vector}")
v1, v2 = vector_2_partes(vector.copy())
print("nuevos vectores despues de division")
print(f'vector 1 : {v1}')
print(f'vector 2 : {v2}')
v3_suma, v3_resta, v3_produc = suma_resta_produc_vector(v1, v2)
print(f'suma del vector 1 y vector 2 : {v3_suma}')
print(f'productoria de los vector 1 y vector 2 : {v3_produc}\n')

# punto 6
print("punto 6 : ")
print(f"el vector {vector} es simetrico ? : {es_simetrico(vector.copy())}\n")

# punto 7
print("punto 7 :")
print(f"vectores : {lst1} - {lst2}")
print(f"union : {union(lst1, lst2)}")
print(f"interseccion : {interseccion(lst1, lst2)}")
print(f"diferencia(A-B) : {diferenciaAB(lst1, lst2)}")
print(f"diferencia(BA-) : {diferenciaBA(lst1, lst2)}")
