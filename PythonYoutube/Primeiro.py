paises = []
resposta = ""
pais = ""

while resposta != "N":
    while len(pais)<3:
        pais = input("Digite o nome de um pais: ").upper()
    paises.append(pais)
    populacao = int(input("Digite a populacao: "))
    paises.append(populacao)
    pais = ""
    resposta = input("Deseja continuar? ").upper()

for p in paises:
    if type(p) == str:
        print("nome do pais: ", p)
    else:
        print("populacao do pais: ", p)