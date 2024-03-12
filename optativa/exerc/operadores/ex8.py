pesoR = float(input("Digite o peso da refeição: "))
pesoP = float(input("Digite o peso do prato: "))

preço = (pesoR-pesoP)*45

print("O preço a pagar é R$ %.2f" % preço)