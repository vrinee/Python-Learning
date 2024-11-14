
class Pessoa:
    def __init__(self,nome,idade,endereco,cpf,sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo
    
    def detalhes(self):
        print("Nome:",self.nome)
        print("Idade:",self.idade)
        print("Endereço:",self.endereco)
        print("CPF:",self.cpf)
        print("Sexo:",self.sexo)
        

class Pai(Pessoa):
    def __init__(self,nome,idade,endereco,cpf,sexo,):
        super().__init__(nome,idade,endereco,cpf,sexo)
        self.esposa = "sem esposa"
        self.filhos = []
    
    def detalhes(self):
        super().detalhes()
        print(self.nome, "é casado com",self.esposa)	
        print(self.nome, "tem",len(self.filhos))
        print(self.nome, "tem os seguintes filhos:")
        for filho in self.filhos:
            print(filho,",",end="")
        
    def addFilho(self,filho):
        self.filhos.append(filho)
        
    def addEsposa(self,esposa):
        self.esposa = esposa
        
    
class Mae(Pessoa):
    def __init__(self,nome,idade,endereco,cpf,sexo):
        super().__init__(nome,idade,endereco,cpf,sexo)
        self.filhos = []
        self.esposo = "sem esposo"
    
    def detalhes(self):
        super().detalhes()
        print(self.nome, "é casada com",self.esposo)
        print(self.nome, "tem",len(self.filhos))
        print(self.nome, "tem os seguintes filhos:")
        for filho in self.filhos:
            print(filho,",",end="")
            
    def addFilho(self,filho):
        self.filhos.append(filho)
    
    def addEsposo(self,esposo):
        self.esposo = esposo
        
    
class Filho(Pessoa):
    def __init__(self,nome,idade,endereco,cpf,sexo):
        super().__init__(nome,idade,endereco,cpf,sexo)
        self.pai = "sem pai"
        self.mae = "sem mãe"
    
    def detalhes(self):
        super().detalhes()
        print(self.pai,"é pai de",self.nome)
        print(self.mae,"é mãe de",self.nome)
    
    def addPai(self,pai):
        self.pai = pai
    
    def addMae(self,mae):
        self.mae = mae
        
miro = Pai("Miro",45,"Rua 1, 123","123.456.789-00","M")
maria = Mae("Maria",40,"Rua 1, 123","123.456.789-00","F")
miro.addEsposa("Maria")
maria.addEsposo("Miro")
joao = Filho("João",20,"Rua 1, 123","123.456.789-00","M")
joao.addPai("Miro")
joao.addMae("Maria")

miro.addFilho("João")
maria.addFilho("João")

miro.detalhes()
print()
maria.detalhes()
print()
joao.detalhes()