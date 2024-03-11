nome = input ("Nome: ")
total_dias = int(input("Número total de dias estudados: "))
total_horas = float(input("Total de horas estudadas em média por dia: "))
curso = input("Nome do curso: ")

print("{} se dedicou ao curso {} por {} dias, em média {} horas por semana" .format(nome, curso, total_dias, total_dias*total_horas))