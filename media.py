#!/usr/bin/python3
# Ler o nome de um aluno
# ler duas notas e calcular a media
#mostrar a media e o nome do alunooo

aluno = input("Nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
# aluno = aluno.upper()
# aluno = aluno.title()
# aluno = aluno.lower()
# aluno = aluno.replace('a', '@')
aluno = aluno.strip()
media = (nota1+nota2) /2

# print("A média do(a) Aluno(a) {} é {}".format(aluno.title(),media))

#if media >= 7:
#    print('Aluno aprovado!')
#else:
#    print('Aluno reprovado')


if media >= 7:
    result = 'aprovado'
elif media < 7 and media > 4:
    result = 'Recuperacao'
else:
    result = 'Reprovado'

print("""aluno: {}
        media: {}
        Resultado: {}
        """.format(aluno, media, result))
