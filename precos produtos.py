nomeAluno = "Leon Graff";
boasvindas = "Bem vindo a sorveteria do {}".format(nomeAluno);
strX = "|  Nº DE BOLAS  |  Sabor Tradicional (tr)  |  Sabor Premium (pr)  |  Sabor Especial (es)  |";
str1 = "|       1       |          R$ 6,00         |       R$ 7,00        |        R$ 8,00        |";
str2 = "|       2       |         R$ 10,00         |      R$ 12,00        |       R$ 14,00        |";
str3 = "|       3       |         R$ 14,00         |      R$ 17,00        |       R$ 20,00        |";
# Array para ter os valores de cada qualidade de sorvete...
sabores = {
    'tr': [6, 11, 15],
    'es': [8, 15, 21],
    'pr': [7, 13, 18]
}

## Criando a função que vai ser responsável por toda a operação
def sorveteria(sabores): ## puxando a array
    valorFinal = 0;
    while True: ## criando o loop
        ## limitando os valores de entrada aos que preciso
        saborSorv = input("Entre com o sabor desejado (tr,es,pr): ");
        ## se o valor de entrada está entre os que procuro
        if saborSorv not in sabores:  # condiçao excludente
            print("Sabor de Sorvete Inválido. Tente novamente.")
            continue 
        if saborSorv in sabores:
            ## perguntando sobre o numero de bolas
            numeroBolas = int(input("Entre com o número de bolas de sorvete desejado (1/2/3): "))
            if numeroBolas not in (1,2,3):  # Verifica se o numero de bolas
                print("Numero de bolas inválido. Tente novamente.")
                continue 
            if numeroBolas in (1, 2, 3):
                ## tratando os diferentes valores para diferentes tipos de sorvete etc
                trad = "TRADICIONAL";
                espe = "ESPECIAL";
                prem = "PREMIUM";
                if saborSorv == "tr":
                    if numeroBolas == 1:
                        valorFinal += 6;
                        print("Você pediu {} bola do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                    if numeroBolas == 2:
                        valorFinal += 11;
                        print("Você pediu {} bolas do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                    if numeroBolas == 3:
                        valorFinal += 15;
                        print("Você pediu {} bolas do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                elif saborSorv == "es":
                    if numeroBolas == 1:
                        valorFinal += 8;
                        print("Você pediu {} bola do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                    if numeroBolas == 2:
                        valorFinal += 14;
                        print("Você pediu {} bolas do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                    if numeroBolas == 3:
                        valorFinal += 20;
                        print("Você pediu {} bolas do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                elif saborSorv == "pr":
                    if numeroBolas == 1:
                        valorFinal += 7;
                        print("Você pediu {} bola do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                    if numeroBolas == 2:
                        valorFinal += 11;
                        print("Você pediu {} bolas do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))
                    if numeroBolas == 3:
                        valorFinal += 15;
                        print("Você pediu {} bolas do sabor {}: R$ {},00".format(numeroBolas,trad,valorFinal))

                simNao = input("Deseja mais algum sabor de sorvete (s/digite outra tecla)? ")

                if simNao != "s" and simNao != "S":
                    print("O total da compra ficou em: R${},00".format(valorFinal));
                    break
## Print das boas vindas              
print(boasvindas);
print(len(strX)*"-");
print(strX);
print(str1);
print(str2);
print(str3);
print(len(strX)*"-");

## Chamando a funçao
sorveteria(sabores)