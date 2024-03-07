resumo = str.upper("Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'.")
resumo_2 = str.lower ("Thiago é um cara de 27 anos que deseja mudar de profissão, por isso está esudando python")
resumo_1 = str.title ("Thiago é um cara de 27 anos que deseja mudar de profissão, por isso está esudando python")
resumo_3 = str.capitalize ("Thiago é um cara de 27 anos que deseja mudar de profissão, por isso está esudando python")
idade = 25 
# Imprima na tela a variável "resumo"
print(resumo)

# Imprima na tela apenas a segunda letra da variável
print (resumo [1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")
print (resumo[23:25])

# Imprima na tela o trecho final da variável
print (resumo[31:])

# Converta todos as letras para minúsculo e imprima na tela
print (resumo_2)

# Converta todas as letras para maiúscula e imprima na tela

print (resumo)

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela

print (resumo_1)

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela

print (resumo_3)

# Imprima na tela uma string utilizando uma variável, usando o recurso string format

print ("Thiago é um cara de 27 anos que deseja mudar de profissão, por isso está esudando python" .format(idade))