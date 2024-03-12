contaCorrente = float(input("Digite o valor depositado:"))

for i in range(1, 3):
    cheque = float(input("Digite o valor do cheque:"))
    contaCorrente -= cheque+(cheque*0.0038)

print("Saldo da conta corrente: R$ %.2f" % contaCorrente)
