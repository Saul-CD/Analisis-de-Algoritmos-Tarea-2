from busqueda_lineal import busqueda_lineal


def probar(func):
    assert func([], 5) == 0
    assert func([5, 1, 2, 3], 5) == 1
    assert func([1, 2, 5, 6], 5) == 3
    assert func([1, 2, 3, 5], 5) == 4
    assert func([1, 2, 3, 4], 99) == 4

    arreglo = list(range(1, 100001))
    assert func(arreglo, 100000) == 100000
    assert func(arreglo, 200000) == 100000
    assert func(arreglo, 1) == 1

    print("Todas las pruebas pasaron")


probar(busqueda_lineal)
