# Sistema de cobrança de banho para um petshop
# variaveis: peso, valor, pelo (multiplicador), adicionais
# adicionais(unhas, dentes, orelhas, nada (?))
#
# valor final = base * multiplicador + extra
nomeAluno = "Leon Graff";
print("Bem vindo a Pet Shop do {}".format(nomeAluno))

pesos_precos = {
    (3, 3): 10,
    (3, 10): 50,
    (10, 30): 60,
    (30, 50): 70
}

## funcao para fazer a chamada de preco no intervalo de pesos
def obterPreco(peso, tabelaPreco):
    ## intervalo aqui recebe a tupla, preco recebe o valor atribuido a tupla
    for intervalo, preco in tabelaPreco.items():
        ## se o peso, passado no parametro da função estiver entre esses intervalos, ele retorna o preco correspondente
        if intervalo[0] <= peso <= intervalo[1]:
            return preco
    return None

## como criei uma função para obter preço ali em cima
## uso aqui uma função para inserir o peso e retornar o preço através da função

def cachorro_peso():
    ## aqui ele deixa um loop antes do try except, obrigatorio?
    peso_dog = 0;
    while True:
        try:
            peso_dog = int(input("Por gentileza, digite o peso do seu cachorro: "));
            if(peso_dog < 3):
                print("O peso do cachorro não pode ser menor do que 3kg.");
            elif(peso_dog > 50):
                print("O peso do cachorro não pode ser maior do que 50kg.");
            else:
                preco_peso = obterPreco(peso_dog,pesos_precos);  
                print(preco_peso);
                break;
        except ValueError:
            print("Valor inválido, tente novamente.")


def cachorro_pelo():
    ## Multiplicador
    pelo_curto = 1
    pelo_medio = 1.5
    pelo_longo = 2
    mult = 0
    
    while True:
        try:
            pelo_dog = input("Digite o tipo de pelo do seu cachorro: ")
            if pelo_dog.lower() == "curto":
                mult = pelo_curto
                break  # Se o valor for válido, encerra o loop e retorna o multiplicador
            elif pelo_dog.lower() == "médio" or pelo_dog.lower() == "medio":
                mult = pelo_medio
                break  # Se o valor for válido, encerra o loop e retorna o multiplicador
            elif pelo_dog.lower() == "longo":
                mult = pelo_longo
                break  # Se o valor for válido, encerra o loop e retorna o multiplicador
            else:
                print("Digite um valor válido.")  # Valor inválido, imprime mensagem de erro e continua o loop
        except ValueError:
            print("Digite um valor válido.")  # Caso ocorra uma exceção, imprime mensagem de erro e continua o loop

    print(mult)
    return mult  # Imprime o multiplicador válido



cachorro_peso();
cachorro_pelo();