# dicionarios em python
"""
comportamento semelhante ao de objetos em javascript
colaborador = {
nome: joao,
setor: manutenção,
salario: 2500

}

"""
lista_colaboradores = []
id_global = 0


def cadastrar_colaborador(id):
    print("xx")


## nome id e salario
"""
C.	Deve-se criar uma função chamada cadastrar_colaborador(id) 
em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
a.	Pergunta nome, setor, pagamento do colaborador;
b.	Armazena o id (este é fornecido via parâmetro da função), 
nome, setor, salário dentro de um dicionário;
c.	Copiar o dicionário dentro para dentro da da 
lista_colaboradores;
 
"""


def consultar_colaborador(id):
    print("xx")


## 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor
#  / 4. Retornar ao menu) e   realizar o print “Opção inválida"
# se entrar com valor diferente de 1, 2, 3 ou 4


def remover_colaborador(id):
    # pergunta o id e remove o colaborador
    print("xx")


def main():
    print("main")


"""
F.	Deve-se criar uma estrutura de menu no main em que: 
a.	Deve-se pergunta qual opção deseja (1. Cadastrar Colaborador / 
2. Consultar Colaborador / 3. Remover Colaborador / 
4. Encerrar Programa) e realizar o print “Opção inválida" 
se entrar com valor diferente de 1, 2, 3 ou 4 :
i.	Se Cadastrar Colaborador, acrescentar em um a variavel id_ global
 e chamar a função cadastrar_colaborador(id_ global);
ii.	Se Consultar Colaborador, chamar função consultar_colaborador();
iii.	Se Remover Colaborador, chamar função remover_colaborador();
iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução
 do código);


"""
