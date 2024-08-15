dta = input("Digite a data(separe com /): ")

dta = dta.split("/")

if dta[1] == "01":
    mes = "Janeiro"
elif dta[1] == "02":
    mes = "Fevereiro"
elif dta[1] == "03":
    mes = "Março"
elif dta[1] == "04":
    mes = "Abril"
elif dta[1] == "05":
    mes = "Maio"
elif dta[1] == "06":
    mes = "Junho"
elif dta[1] == "07":
    mes = "Julho"
elif dta[1] == "08":
    mes = "Agosto"
elif dta[1] == "09":
    mes = "Setembro"
elif dta[1] == "10":
    mes = "Outubro"
elif dta[1] == "11":
    mes = "Novembro"
else:
    mes = "Dezembro"
    
print(dta[0], "de", mes, "de", dta[2])