cod = int(input("Digite o código do produto: "))

match cod:
    case 1:
        print("Alimento não-perecível")
    case 2|3|4:
        print("Alimento perecível")
    case 5|6:
        print("Vestuário")
    case 7:
        print("Higiene Pessoal")
    case 8|9|10|11|12|13|14|1215:
        print("Limpeza e Utensílios Domésticos")
    case _:
        print("Código inválido")