"""""
URI Online Judge 1121
Comprando com desconto

Maria, além de comerciante, era também uma excelente negociante! Por isso, sempre consegue descontos nas suas compras, Ao visitar uma Lop, Maria recebeu a seguinte proposta de um vendedor: "Se comprar minha mercadoria concederem um desconto Fixo de 10% e mais 1% a cada unidade comprada". Infelizmente, Maria está cansada de tanto trabalhar e não quer fazer os cálculos sozinha para descobrir qual será o valor da compra antes e depois do desconto, por isso pediu sua ajuda.
Você irá criar um programa que receba como entrada um número real, indicando o preço da mercadoria comprada por Maria, e um número inteiro, indicando a quantidade de mercadoria comprada, exibir um valor da compra antes do desconto e o valor final, já com o desconto aplicado.
Observação: Para todos os efeitos, assuma que essa loja nunca venda mais do que 40 unidades de uma mesma mercadoria para a mesma pessoa. Repare que não é necessário verificar, basta assumir que isso é verdade.

Entrada
Um número real positivo na primeira linha, indicando o preço da mercadoria, e um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.

Saída
Na primeira linha deve ser impresso um valor real com duas casas decimais, indicando a preço da compra sem o descant° e, na segunda linha, o preço Final corn o desconto aplicado, também com duas casas decimais.
"""

while True:
    Unidade = int(input("Digite a quantidade de unidades: "))
    Preco_Produto = float(input("Digite o preço do produto: "))

    if Unidade <= 40:
        Valor_Total = Unidade * Preco_Produto
        Valor_10_Desconto = Valor_Total * 0.10
        Deconto_1 = (Valor_Total * Unidade) / 100
        Desconto_Final = Valor_Total - Valor_10_Desconto - Deconto_1
        print("Valor total: " f'{Valor_Total:.2f}')
        print("Valor com 10% de desconto: " f'{Desconto_Final:.2f}')
    else:
        print("Não é permitido o desconto para compras acima de 40 unidades. ")

    continuar = input("Deseja continuar? (S/N)")
    if continuar == "N" or continuar == "n":
        break
