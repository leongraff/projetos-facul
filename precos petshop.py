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

def cachorro_pelo();
    ## Multiplicadores:
    while True:
        try:
            pelo_dog = int(input("Digite o tipo de pelo do seu cachorro: "));
        
        except ValueError:
            print("Digite um valor válido.")


cachorro_peso();