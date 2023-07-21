##Questão 1, Loja.

print("Bem vindo a Loja do Leon Graff")

##Definindo a variável que irá armazenar o valor do produto:

valorProduto = int(input("Entre com o valor do produto: "))

##Definindo a variável que irá armazenar a quantidade do produto:

qtdProduto = int(input("Entre com a quantidade do produto: "))

##Calculando 3 tipos de descontos para atribuí-los depois com os condicionais

varDesc_5 = valorProduto*0.05;
varDesc_10 = valorProduto*0.10;
varDesc_15 = valorProduto*0.15;

##Estrutura condicional do código

if(qtdProduto < 200):
    print("O valor SEM desconto: R$" + str(valorProduto))
    print("O valor COM desconto: R$" + str(valorProduto))
elif(qtdProduto >= 200 and qtdProduto < 1000):
    print("O valor SEM desconto: R$" + str(valorProduto))
    valorComDesc = valorProduto - varDesc_5;
    print("O valor COM desconto: R$" + str(valorProduto - varDesc_5))
elif(qtdProduto > 1000 and qtdProduto < 2000):
    print("O valor SEM desconto: R$" + str(valorProduto))
    valorComDesc = valorProduto - varDesc_10;
    print("O valor COM desconto: R$" + str(valorProduto - varDesc_10))
else:
    print("O valor SEM desconto: R$" + str(valorProduto))
    valorComDesc = valorProduto - varDesc_15;
    print("O valor COM desconto: R$" + str(valorProduto - varDesc_15))

    
    
