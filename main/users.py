import pickle

from simulator import *

class User():
    def __init__(self, id, name, balance, stocks=[], quantity=[], valueSpend=[]):
        self.id = id
        self.name = str(name)
        self.balance = float(balance)
        self.stocks = str(stocks)
        self.quantity = int(quantity)
        self.valueSpend = float(valueSpend)
    
    def paraLista(self): #criar uma lista com os valores do portefolio de forma a ser apresentado numa tabela
        lista = []
        lista.append(('STOCK', 'QUANTTIY', 'VALUE SPEND'))
        for i in range(len(self.titulos)):
            lista.append((self.titulos[i], self.quantidade[i], self.valorGasto[i]))
        return lista

def createUser(): #funcao para acrescentar utilizadores e guarda-los em formato pickle
    id += 1
    name = input('Inserir nome de utilizador: ')
    balance = input('Inserir saldo do utilitador: ')
    user = User(id, name, balance)
    userName = str('utilizador_') + str(user.id)
    with open(userName + '.pkl', 'wb') as file:
        pickle.dump(user, file)

def updateUsers(): #para carregar os utilizadores ja criados
   global id, listUsers
   for i in range(1, 4):
        id += 1
        userName = str('user_') + str(id)
        with open(userName + '.pkl', 'rb') as file:
            user = pickle.load(file)
            listUsers.append(user)

def loadUsers():
    global listUsers
    id = 0
    for user in listUsers:
        id += 1
        userName = str('user_') + str(id)
        with open(userName + '.pkl', 'wb') as file:
            pickle.dump(user, file)