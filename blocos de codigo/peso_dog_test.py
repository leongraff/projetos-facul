# Tabela de preços
pesos_precos = {
    (0, 5): 10.00,
    (6, 10): 15.00,
    (11, 20): 20.00,
    (21, 30): 25.00
}

# Função para obter o preço com base no peso
def obter_preco_por_peso(peso, tabela_precos):
    for intervalo, preco in tabela_precos.items():
        if intervalo[0] <= peso <= intervalo[1]:
            return preco
    return None  # Retorna None se o peso não se encaixar em nenhum intervalo

# Função para calcular o preço com base no peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso_cachorro = float(input("Digite o peso do cachorro (em kg): "))
            if peso_cachorro < 0:
                raise ValueError  # Lançar exceção se o peso for negativo
            if peso_cachorro >= 50:
                print("O peso do cachorro não pode ser igual ou acima de 50kg. Tente novamente.")
            else:
                preco_base = obter_preco_por_peso(peso_cachorro, pesos_precos)
                if preco_base is not None:
                    return preco_base
                else:
                    print("Não foi encontrado preço para o peso informado. Tente novamente.")
        except ValueError:
            print("Por favor, insira um valor numérico positivo para o peso do cachorro.")

# Exemplo de uso da função cachorro_peso()
preco_final = cachorro_peso()
print(f"O preço base para o peso do cachorro é: R$ {preco_final:.2f}")
