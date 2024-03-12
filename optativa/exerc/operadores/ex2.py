dep = float(input("Digite o valor do depósito: "))

tax = float(input("Digite o valor da taxa anual: "))

rend = dep * (tax / 100)

print("Valor de rendimento: R$ %.2f" % rend, "\nValor total: R$ %.2f" % (dep + rend))

