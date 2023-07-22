# Sistema de cobrança de banho para um petshop

nomeAluno = "Leon Graff"
print("Bem vindo a Pet Shop do {}".format(nomeAluno))

## achei interessante nesse caso em especial tentar trabalhar com tuplas para pegar os preços dos intervalos de peso

pesos_precos = {(3, 3): 10, (3, 10): 50, (10, 30): 60, (30, 50): 70}


## funcao para fazer a chamada de preco no intervalo de pesos


def obterPreco(peso, tabelaPreco):
    ## intervalo aqui recebe a tupla, preco recebe o valor atribuido a tupla
    for intervalo, preco in tabelaPreco.items():
        ## se o peso, passado no parametro da função estiver entre esses intervalos, ele retorna o preco correspondente
        if intervalo[0] <= peso <= intervalo[1]:
            return preco
    return None


# função para retornar o preço de acordo com o peso.


def cachorro_peso():
    peso_dog = 0
    while True:
        try:
            peso_dog = int(input("Entre com o peso do cachorro: "))
            if peso_dog < 3:
                print("Não aceitamos cachorros tão pequenos.")
                print("Por favor, entre com o peso do cachorro novamente.")
            elif peso_dog > 50:
                print("Não aceitamos cachorros tão grandes.")
                print("Por favor, entre com o peso do cachorro novamente.")
            else:
                preco_peso = obterPreco(peso_dog, pesos_precos)
                return preco_peso
                ##print(preco_peso)
                break
        except ValueError:
            print("Você digitou um valor não numérico.")
            print("Por favor, entre com o peso do cachorro novamente.")


# função para retornar o multiplicador correto e receber o input dos pelos


def cachorro_pelo():
    ## definindo os multiplicadores
    pelo_curto = 1
    pelo_medio = 1.5
    pelo_longo = 2
    mult = 0

    while True:
        # printando as opções disponíveis
        print("Entre com o pelo do cachorro")
        print("c - Pelo curto")
        print("m - Pelo médio")
        print("l - Pelo longo")
        try:
            pelo_dog = input("Digite o tipo de pelo do seu cachorro: ")
            if pelo_dog == "c":
                mult = pelo_curto
                break
            elif pelo_dog == "m":
                mult = pelo_medio
                break
            elif pelo_dog == "l":
                mult = pelo_longo
                break
            else:
                print("Digite um valor válido.")
        except ValueError:
            print("Digite um valor válido.")

    # print(mult)
    return mult  # Imprime o multiplicador válido


# função que calcula os serviços adicionais


def cachorro_extra():
    extra = 0
    while True:
        try:
            print("Deseja adicionar mais algum serviço?")
            print("1 - Corte de unhas - R$ 10,00")
            print("2 - Escovar dentes - R$ 12,00")
            print("3 - Limpeza de orelhas - R$ 15,00")
            print("0 - Não desejo mais nada")
            serv_adc = int(input())
            if serv_adc in (1, 2, 3, 0):
                if serv_adc == 1:
                    extra += 10
                elif serv_adc == 2:
                    extra += 12
                elif serv_adc == 3:
                    extra += 15
                elif serv_adc == 0:
                    extra += 0
                    ##print(extra)
                    return extra
                    break
        except ValueError:
            print("Por favor digite um valor válido.")


# calculando o valor total usando os returns de cada função


def main():
    preco_peso = cachorro_peso()
    mult = cachorro_pelo()
    extra = cachorro_extra()
    total_pagar = preco_peso * mult + extra
    print(
        "Total a pagar: R$ {},00 (peso: R$ {} * pelo: {} + adicional(is): R$ {})".format(
            total_pagar, preco_peso, mult, extra
        )
    )


main()
