estudante = {}
estudante['nome'] = input('Qual seu nome? ')
estudante['ano_conheceu_linkedin'] = int(input('Em qual ano você conheceu o LinkedIn Learning? '))
estudante['ano_atual'] = int(input('Qual é o ano atual? '))
cursos = input('Quais os cursos você já fez no LinkedIn Learning? (separe-os com vírgula) ')

estudante['cursos'] = cursos.split(', ')

print(f"Oi {estudante['nome']}, desde {estudante['ano_conheceu_linkedin']} você conhece o LinkedIn. Nesses {estudante['ano_atual'] - estudante['ano_conheceu_linkedin']} anos, você realizou {len(estudante['cursos'])} cursos, sendo o primeiro curso '{estudante['cursos'][0]}' e último '{estudante['cursos'][-1]}'.")
