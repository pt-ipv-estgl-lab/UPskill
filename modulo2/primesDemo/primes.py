def primos(n):
    nums = [] # incializa a lista de nºs primos
    if n < 2:
        return nums # devolve lista vazia
    
    vals = [True for i in range(n)] # lista auxiliar com todos o nºs sendo primos
    vals[0] = vals[1] = False # 0 e 1 nunca são primos
    for i in range(2, n): # processo de eliminação de todos os multiplos a parir de 2
        if vals[i]:
            nums += [i] # acrescenta i (número primo) à lista
            for j in range(i*i, n, i): # eliminação de todos os múltiplos de i
                vals[j] = False
    return nums

num = int(input('Número? '))
while( num > 0 ): # repete enquanto o utilizador não introduzir zero
    print('primos:', primos(num))
    num = int(input('Número (0 para terminar)? ')) # > 0 para continuar

