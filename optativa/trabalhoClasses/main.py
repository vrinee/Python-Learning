from livro import Livro # não tenho certeza se precisa importar ou não 
from livro import CadastroLivro

cadastro = CadastroLivro()

print("Bem vindo a biblioteca!!!!")
while True:
    op = input("Digite a opção desejada(1-Adicionar livro,2-Listar livros,3-Atualizar livros,4-Excluir livros,5-Sair): ")
    match op:
        case "1":
            cadastro.addLivro()
        case "2":
            cadastro.listarLivros()
        case "3":
            cadastro.atualizarLivros()
        case "4":
            cadastro.excluirLivros()
        case "5":
            break
        case _:
            print("Opção inválida")
            continue
        
print("Obrigado por utilizar a biblioteca!!! E infelizmente o trabalho vai ter que ser entergue e talvez não testado")