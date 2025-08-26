from datetime import datetime

#Criar a Classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = int(ano_nascimento)

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

#Criar o Objeto
usuario1 = Funcionarios('Elena', 'Cabral', ' 2009')

#Criar os parametros
#usuario1.nome = 'Elena'
#usuario1.sobrenome = 'Cabral'
#usuario1.data_nascimento = '12/01/2009'

#Criar os parametros
#usuario2.nome = 'Joao'
#usuario2.sobrenome = 'Marcelo'
#usuario2.data_nascimento = '30/05/2002'

#print
print(Funcionarios.idade_funcionario(usuario1))