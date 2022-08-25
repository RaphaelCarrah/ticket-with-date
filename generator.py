import string
from datetime import datetime
dtf = datetime.now()
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

def formatar(data):
    parametros = {'1': 'Ano: ','2': 'Mês: ','3': 'Dia: ','4': 'Hora: ','5': 'Min: '}
    texto = int(input(parametros[data]).lstrip('0'));
    return texto

def chave(posicao):
    chave = 'ZABCDEFGHIJKLMNOPQRSTUVWXY1234567890'
    return chave[posicao]

def tipo():
    entrada = int(input('Escolha o tipo: \n\n Documento   [1]\n Equipamento [2]\n\nDigite:      '))
    ticket = '0HD'
    return ticket[entrada]

def menu():
    entrada = int(input('\n Gerar Automaticamente [1]\n Definir data          [2]\n \nDigite:  ')) 
    return entrada

x=1

while x == 1:
    clearConsole()
    tipo_de_doc = tipo()
    clearConsole()
    opcao = menu()
    clearConsole()

    if opcao == 2:
        ano = str(formatar('1'))[-2:]
        clearConsole()
        mes = formatar('2')
        clearConsole()
        dia = formatar('3')
        clearConsole()
        hora = formatar('4')
        clearConsole()
        min = formatar('5')
    else:
        ano = str(dtf.strftime('%Y'))[-2:]
        mes = int(dtf.strftime('%m'))
        dia = int(dtf.strftime('%d'))
        hora = int(dtf.strftime('%H'))
        min = int(dtf.strftime('%M'))

    if  opcao == 2:  
        clearConsole()
        print('\n\n-->  #'+tipo_de_doc+ano+chave(mes)+chave(dia)+chave(hora)+str(min).zfill(2)+"  <--\n\n") 
    

    else:
        clearConsole()
        print('\n\n-->  #'+tipo_de_doc+ano+chave(mes)+chave(dia)+chave(hora)+str(min).zfill(2)+"  <--\n\n")

    x = int(input('\n\n Digite [1] - Para Repetir\n Pressione qualquer tecla para sair\n ---->'))

        

    
