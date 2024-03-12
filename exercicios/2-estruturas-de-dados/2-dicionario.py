pessoa = {"nome" : "Thiago", 
          "idade" : 27, 
          "ano_formatura" : 2017, 
          "linguagens_de_program": "python",
          "brasileiro": True,
          "hobby": ["surfar","correr","xadres","muscia","pintar"],
          "animal_estimacao": True}

# Imprima na tela o valor equivalente a chave "hobby"
print (pessoa["hobby"])

# Imprima na tela uma lista apenas com os valores do dicionário
print (pessoa.values())

# Imprima na tela uma lista apenas com as chaves do dicionário
print (pessoa.keys())

# Insira um novo par chave-valor no dicionário
pessoa["ano_nasc"] = 1996
print (pessoa)