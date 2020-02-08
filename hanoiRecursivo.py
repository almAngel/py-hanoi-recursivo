def hanoi(n, torre_inicio, torre_auxiliar, torre_destino):

    if n == 1:
        print(f"Moviendo {n} a torre {torre_destino} desde torre {torre_inicio}")
    else:
        hanoi(n-1, torre_inicio, torre_destino, torre_auxiliar)
        print(f"Moviendo {n} a torre {torre_destino} desde torre {torre_inicio}")
        hanoi(n-1, torre_auxiliar, torre_inicio, torre_destino)


hanoi(3, 'A', 'B', 'C')