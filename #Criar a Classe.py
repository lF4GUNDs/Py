#Criar a Classe
class Funicionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        

#Criar o Objeto
usuario1 = Funicionarios('Elena', 'Cabral', ' 12/01/2009')

#Criar os parametros
#usuario1.nome = 'Elena'
#usuario1.sobrenome = 'Cabral'
#usuario1.data_nascimento = '12/01/2009'

#Criar os parametros
#usuario2.nome = 'Joao'
#usuario2.sobrenome = 'Marcelo'
#usuario2.data_nascimento = '30/05/2002'

#print
print(usuario1.nome)