broas = int(input("Digite o número de broas vendidas: "))*1.50
paes = int(input("Digite o número de pães vendidos: "))*0.50

renda = broas + paes
arrecadacao = renda*0.10

print("Renda do dia: R$ %.2f" % renda, "\nArrecadação do dia: R$ %.2f" % arrecadacao, "\nLucro: R$ %.2f" % (renda-arrecadacao))