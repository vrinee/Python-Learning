import time
import os
class carro:
    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 2024
    km_rodados = 0
    motor = False
    andando = False
    
    def detalhes(self):
        print("Cor:",self.cor)
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Ano:",self.ano)
        print("Quilometragem:",self.km_rodados)
        print("Motor ligado: ",self.motor)
        
    def adicionaKm(self,km):
        self.km_rodados += km
    
    def ligarMotor(self):
        self.motor = True
    
    def desligarMotor(self):
        self.motor = False
    
    def andar(self):
        if self.motor == True:
            self.andando = True
            for i in range(100):
                print(
                   " "*i,    "         .--------.\n",
                   " "*i,    "   ____/_____|___ \___\n",
                   " "*i,    "  O    _   - |   _   ,*\n",
                   " "*i,    "   '--(_)-------(_)--'\n" ,
                    
                    
                    
                )
                time.sleep(0.2)
                self.adicionaKm(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            self.parar
        else:
            print("Motor não esta ligado")
    
    def parar(self):
        self.andando = False
        
carrin = carro()

while(True):
    op = int(input("Digite a ação(1-ligar,2-desligar,3-andar,4-detalhes):"))
    match op:
        case 1:
            carrin.ligarMotor()
        case 2:
            carrin.desligarMotor()
        case 3:
            carrin.andar()
        case 4:
            carrin.detalhes()
        case _:
            print("Input invalido")


    

        