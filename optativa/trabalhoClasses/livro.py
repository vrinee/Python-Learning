class Livro:
 def __init__(self, titulo, autor, isbn, ano_publicacao, status):
    self.titulo = titulo 
    self.autor = autor 
    self.isbn = isbn 
    self.ano_publicacao = ano_publicacao 
    self.status = status 
    
    
    
class CadastroLivro:
    def __init__(self):
        self.livros = []
        
    def addLivro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        status = input("Digite o status do livro: ")
        livro = Livro(titulo, autor, isbn, ano_publicacao, status)
        self.livros.append(livro)
        
    def listarLivros(self):
        for livro in self.livros:
            print("Título:", livro.titulo)
            print("Autor:", livro.autor)
            print("ISBN:", livro.isbn)
            print("Ano de publicação:", livro.ano_publicacao)
            print("Status:", livro.status)
            print("\n")
            
    def atualizarLivros(self):
        self.listarLivros()
        op = input("Você deseja inserir titulo(1), isbn(2)? ")
        match op:
            case "1":
                livroAtualizar = input("Digite o título do livro que deseja atualizar: ")
            case "2":
                livroAtualizar = input("Digite o ISBN do livro que deseja atualizar: ")
            case _:
                print("Opção inválida")
                return
        for livro in self.livros:
            if livro.titulo == livroAtualizar or livro.isbn == livroAtualizar:
                op = input("Você deseja atualizar o título(1), autor(2), isbn(3), ano de publicação(4), status(5)? ")
                match op:
                    case "1":
                        livro.titulo = input("Digite o novo título: ")
                    case "2":
                        livro.autor = input("Digite o novo autor: ")
                    case "3":
                        livro.isbn = input("Digite o novo ISBN: ")
                    case "4":
                        livro.ano_publicacao = input("Digite o novo ano de publicação: ")
                    case "5":
                        livro.status = input("Digite o novo status: ")
                    case _:
                        print("Opção inválida")
                        return
                print("Livro atualizado")
                return
        print("Livro não encontrado")
        
    def excluirLivro(self):
        self.listarLivros()
        op = input("Você deseja excluir pelo título(1) ou ISBN(2)? ")
        match op:
            case "1":
                livroExcluir = input("Digite o título do livro que deseja excluir: ")
            case "2":
                livroExcluir = input("Digite o ISBN do livro que deseja excluir: ")
            case _:
                print("Opção inválida")
                return
        for livro in self.livros:
            if livro.titulo == livroExcluir or livro.isbn == livroExcluir:
                self.livros.remove(livro)
                print("Livro excluído")
                return
        print("Livro não encontrado")
        
    

            
