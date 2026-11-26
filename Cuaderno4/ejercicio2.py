def procedimiento(m, n):
    """ Documentación: Se ha borrado. """
    while n > 0:
        r = n % 10
        for k in range(r, 0, -1):
            print(m, end='')
        print()
        n = n // 10
    return 'nada'
procedimiento('o', 1234321)