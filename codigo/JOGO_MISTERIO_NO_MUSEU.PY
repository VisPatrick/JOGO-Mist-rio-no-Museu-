while True:


    # ESCOLHA DA ENTRADA

    while True:
        entrada = input("Escolha a entrada (frente, servico ou telhado): ")
        if entrada in ["frente", "servico", "telhado"]:
            break

    tentativas = 0
    acertou = False

    # DESAFIO LÓGICO

    while tentativas < 3 and not acertou:
        tentativas += 1

        if entrada == "frente":
            valores = input("Digite dois inteiros e um decimal: ").split()

            if len(valores) == 3:
                try:
                    n1 = int(valores[0])
                    n2 = int(valores[1])
                    n3 = float(valores[2])

                    if n1 != 0 and 294 % n1 == 0 and n2 == 294 // n1 and n3 == n2 / n1:
                        acertou = True
                except Exception:
                    pass

        elif entrada == "servico":
            valores = input("Digite dois inteiros: ").split()

            if len(valores) == 2:
                try:
                    n1 = int(valores[0])
                    n2 = int(valores[1])

                    if n2 != 0 and n1 % n2 == 0 and n2 % 2 != 0 and n1 + n2 > 50:
                        acertou = True
                except Exception:
                    pass

        elif entrada == "telhado":
            valores = input("Digite tres decimais: ").split()

            if len(valores) == 3:
                try:
                    x = float(valores[0])
                    y = float(valores[1])
                    z = float(valores[2])

                    if (x + y > z and x + z > y and y + z > x) and not (x == y == z):
                        acertou = True
                except Exception:
                    pass

        if not acertou:
            if tentativas < 3:
                print("Tentativas restantes:", 3 - tentativas)
            else:
                print("Derrota!")

    if not acertou:
        resposta = input("Deseja jogar novamente (sim ou nao)? ")
        if resposta == "nao":
            break
        else:
            continue


    # FASE DOS ITENS

    while True:
        itens = input("Escolha dois itens: ").split()
        validos = ["lanterna", "chave", "corda"]

        if len(itens) == 2:
            if itens[0] != itens[1]:
                if itens[0] in validos and itens[1] in validos:
                    break

    conjunto_itens = set(itens)


    # RESULTADO FINAL

    if entrada == "frente":
        ideal = {"lanterna", "chave"}
        supremo = "excelente supremo"
        normal = "excelente"

    elif entrada == "servico":
        ideal = {"chave", "corda"}
        supremo = "perfeito supremo"
        normal = "perfeito"

    else:
        ideal = {"lanterna", "corda"}
        supremo = "ninja supremo"
        normal = "ninja"

    if conjunto_itens != ideal:
        print("Final: ruim")
    else:
        if tentativas == 1:
            print("Final:", supremo)
        elif tentativas == 2:
            print("Final:", normal)
        else:
            print("Final: neutro")

    resposta = input("Deseja jogar novamente (sim ou nao)? ")
    if resposta == "nao":
        break
