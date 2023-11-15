#trainning PEP 8

#Espaçamento_
#Errado - Use o underline para indicar espaçamento

x = "Thiago"

def printhiworld(x):
    
    return x * 2

#Certo 

x = 2

def print_hi_world(x):

    return x * 2
    
#------------------------------------------------------------------------------------------------------------------

#Para váriaveis
#Não use letras como x, y, z e afins. Use nomes que facilitarão a leitura do código

nota1 = 2           
nota2 = 10 
qtde_notas = 2         

def calculo_nota_final(nota1, nota2):
    
    nota_final = (nota1 + nota2)/qtde_notas #Calculo de uma média
    
    #Use se necessário abreviações, mas de uma forma que seja notável a intenção
    
    return nota_final
    
#----------------------------------------------------------------------------------------------------

#Para Classes

class Hello:
    #Classes começam com letras maiusculas(não necessáriamente, porém esse comentário vai
    #ajudar o programador que irá ler o código)
    def __init__(self, message): 
        #self no começo para evitar erros
        self.inicio = message
    pass
#----------------------------------------------------------------------------------------------------
    
    
#def retorno_funcao_args(
#   arg_one, arg_two, 
#   arg_three, arg_four):

#Correto :
def retorno_função(arg_one, arg_two,
                   arg_three, arg_four):
    return
#----------------------------------------------------------------------------------------------------

#Váriaveis

value = 0 #Totalmente certo, com espaçamento correto
value=0 #errado
value =0 #errado

#----------------------------------------------------------------------------------------------------

class nome:
    #Classes começam com letras maiusculas(não necessáriamente, porém esse comentário vai
    #ajudar o programador que irá ler o código)
    def __init__(self, nome): 
        #self no começo para evitar erros
        self.inicio = nome
        print(f"Meu nome é {nome}")
    pass

#----------------------------------------------------------------------------------------------------

#Constantes

CONSTANTE = 450 #Note a Capslock ativada