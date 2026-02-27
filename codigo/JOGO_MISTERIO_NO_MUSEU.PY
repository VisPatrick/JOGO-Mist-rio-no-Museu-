while True:
    # jogo acontece aqui
    
    resposta = input("Deseja jogar novamente (sim ou nao)? ")
    if resposta == "nao":
        break

while True:
    entrada = input("Escolha a entrada (frente, servico ou telhado): ")
    if entrada in ["frente", "servico", "telhado"]:
        break
tentativas = 0
acertou = False

while tentativas < 3 and not acertou:
    tentativas += 1
    
    correto = False
    # desafio aqui
    
    if correto:
        acertou = True
    else:
        print("Tentativas restantes:", 3 - tentativas)
valores = input().split()

if len(valores) == 3:
    try:
        n1 = int(valores[0])
        n2 = int(valores[1])
        n3 = float(valores[2])

        if 294 % n1 == 0 and n2 == 294 // n1 and n3 == n2 / n1:
            correto = True
    except (ValueError, ZeroDivisionError):
        pass