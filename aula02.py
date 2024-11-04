    # ATIVIDADE DA 1 ATÉ A 4


set = set()
frutas_vermelhas = {'morango', 'cereja', 'framboesa'} 

set.add('maçã')
set.add("banana")
set.add("uva")
set.add("laranja")
set.add('morango')
frutas_vermelhas.remove('morango')
print("banana" in set)
print(set)
print(frutas_vermelhas)



procurado = input("Digite sua fruta aqui: ")

if procurado in set and procurado not in frutas_vermelhas: 
  print(f"Sua fruta: {procurado} está nos set, porem não está nas frutas vermelhas")

elif procurado not in set and procurado in frutas_vermelhas:
  print(f"Sua fruta: {procurado} não está no set, porem está nas frutas vermelhas")

elif procurado in set and procurado in frutas_vermelhas:
  print(f"Sua fruta: {procurado} está em ambos")
else: 
  print("Não está em nenhumas")


     #  Atividade 5 e 6

A = {"Sla", "anham"}
B = {"RIÁ", "S-L-A", "anham"}

print(A.intersection(B))


A.update(B)
print(A)

      # ATIVIDADE 7



lista1 = {"A", "B", "C"}
lista2 = {"A", "D", "E"}

lista1.intersection_update(lista2)
print(lista1)


# ATIVIDADE 8

pessoas = {
    "João": 25,
    "Maria": 30,
    "Pedro": 22
}


print("Informações das pessoas:")
for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")


# ATIVIDADE 9




pessoas2 = {
    "João": 25,
    "Maria": 30,
    "Pedro": 22
}


print("Chaves do dicionário:")
for nome in pessoas2.keys():
    print(nome)



print("\nValores do dicionário:")
for idade in pessoas2.values():
    print(idade)


# ATIVIDADE 10


def adicionar_ou_atualizar(dicionario, chave, valor):
    dicionario[chave] = valor
    return dicionario


dicionario = {'a': 1, 'b': 2}
chave = input("Digite a chave: ")
valor = int(input("Digite o valor: "))
resultado = adicionar_ou_atualizar(dicionario, chave, valor)
print("Dicionário atualizado:", resultado)




# ATIVIDADE 11
def verificar_chaves(dicionario, lista_chaves):
    return all(chave in dicionario for chave in lista_chaves)


dicionario = {'a': 1, 'b': 2, 'c': 3}
lista_chaves = ['a', 'b', 'd']
resultado = verificar_chaves(dicionario, lista_chaves)
print("Todas as chaves existem no dicionário?", resultado)




 # ATIVIDADE 12

votos = {}
print("Digite 0 para encerrar a votação.")

while True:
    opcao = input("Digite sua opção de voto: ")
    if opcao == '0':
        break
    if opcao in votos:
        votos[opcao] += 1
    else:
        votos[opcao] = 1

print("\nResultados da votação:")
for opcao, contagem in votos.items():
    print(f"Opção '{opcao}': {contagem} votos")


# ATIVIDADE 13


alunos = {
    "João": [8, 7, 9],
    "Maria": [10, 9, 10],
    "Pedro": [7, 6, 8]
}

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome}: média de notas {media:.2f}")



# ATIVIDADE 14

# NÃO CONSEGUIR

# ATIVIDADE 15


conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto3 = {5, 6, 7}

uniao = conjunto1 | conjunto2 | conjunto3
print("Conjunto resultante da união:", uniao)



# DESAFIO PRÁTICO 

alunos = []


while True:
    opcao = input("\nDigite '1' para cadastrar um aluno, '0' para sair: ")
    if opcao == '0':
        break
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    notas = (
        float(input("Nota de Matemática: ")),
        float(input("Nota de Ciências: ")),
        float(input("Nota de História: "))
    )
    aluno = {"nome": nome, "idade": idade, "notas": notas}
    alunos.append(aluno)


print("\nAlunos cadastrados:")
for aluno in alunos:
    media = sum(aluno['notas']) / len(aluno['notas'])
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Média: {media:.2f}")


melhor_aluno = max(alunos, key=lambda x: sum(x['notas']) / len(x['notas']))
melhor_media = sum(melhor_aluno['notas']) / len(melhor_aluno['notas'])
print(f"\nAluno com a melhor média: {melhor_aluno['nome']} com média {melhor_media:.2f}")
