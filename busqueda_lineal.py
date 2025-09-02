def busqueda_lineal(
    arreglo: list[int], k: int
):  # S(n) = 1 + 1 = 2, porque se pasan por referencia
    comparaciones: int = 0  # T(n) = 1, S(n) = 1

    for elemento in arreglo:  # T(n) = n, S(n) = 1
        comparacion: bool = elemento == k  # T(n) = 1, S(n) = 1
        comparaciones += 1  # T(n) = 1, S(n) = 0

        if comparacion:  # T(n) = 1, S(n) = 0
            break  # T(n) = 1, S(n) = 0

    return comparaciones  # T(n) = 1, S(n) = 0

    # T(n)= 1 + 4n + 1 = 4n + 2
    # S(n)= 2 + 1 + 1 + 1 = 5
