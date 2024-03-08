# Crie uma lista apenas com elementos numéricos
lista_numerica = [125, 2, 235, 258, 3.44, 1]
print (lista_numerica)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = ['Thiago', 12, 13, 14, 'python', [1,2,3,4,5], True]
print (lista_mista)

# Imprima na tela apenas os 5 primeiros elementos da lista
lista_mista = ['Thiago', 12, 13, 14, 'python', [1,2,3,4,5], True]
print (lista_mista[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
lista_numeros_par = [1,2,3,4,5,6,7,8,9]
print (lista_numeros_par[1:8:2])

# Remova da lista o último item
lista_numerica.pop()
print (lista_numerica)

# Insira na lista um novo item
lista_numerica = [1, 254, 332, 3.44, 2.55]
lista_numerica.append(1.0)
print (lista_numerica)

# Remova da lista um item específico
lista_mista = ['Thiago', 12, 13, 14, 'python', [1,2,3,4], True]
lista_mista.remove('python')
print (lista_mista)