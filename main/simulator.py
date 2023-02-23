from abc import ABC, abstractmethod
from currency_converter import CurrencyConverter #para converter as diferentes moedas
from datetime import datetime # importar formato data
from datetime import time   #importar formato tempo
from tkinter.ttk import *
from tkinter import *
import pytz    #importar relogio inter
import pickle

from stocks import *
from users import *
from buysellrequests import *

with open('pedidoCompraID' + '.txt', 'r') as file:
    buyRequestId = file.readline()

with open('pedidoVendaID' + '.txt', 'r') as file:
    sellRequestId = file.readline()

europe = ['NESN.SW', 'ASML.AS', 'ROG.SW', 'AZN.L', 'SHEL.L'] #lista de titulos de empresas europeias
america = ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'GOOGL'] #lista de titulos de empresas americanas

aberturaAmerica = time(9, 0, 0)
fechoAmerica = time(22, 0, 0)

aberturaEuropa = time(8, 0, 0)
fechoEuropa = time(22, 30, 00)

listSells = [] #list with the sell request
listBuys = [] #list with the buy request
listUsers =[] #list with the users
listStocks = [] #list with the stocks

def transaction(buyRequest, sellRequest):
    global listSells, listBuys, listUsers, listStocks, listUsers

    if sellRequest.price <= buyRequest.price and sellRequest.quantity == buyRequest.quantity:
        buyingUser = [user for user in listUsers if buyRequest.id == user.id] #saber o utilizador que fez o pedido de compra
        buyingUser = buyingUser[0]
        buyingUser.saldo = float(buyingUser.balance) - (float(buyRequest.price) * int(buyRequest.quantity)) # atualizar o saldo do utilizador
        if buyRequest.stock in buyingUser.stocks: #procurar na lista de titulos do utilizador o tilulo da transacao
            #se o titulo existir, fazer a atualizacao dos dados
            index = buyingUser.stocks.index(buyRequest.stock) #saber o indice do titulo na lista
            buyingUser.quantity[index] += buyRequest.quantity #actualizar a quantidade no portefolio do utilizador
            buyingUser.valueSpend[index] += (buyRequest.price * buyRequest.quantity) #actualizar no portefolio o valor gasto neste titulo
        else:
            buyingUser.stocks.append(buyRequest.stock)
            buyingUser.quantity.append(buyRequest.quantity)
            buyingUser.valueSpend.append((buyRequest.price * buyRequest.quantity))
                
        sellingUser = [user for user in listUsers if sellRequest.id == user.id] #saber que utilizador fez o pedido de venda
        sellingUser = sellingUser[0]
        sellingUser.balance = float(sellingUser.balance) + (float(buyRequest.price) * int(buyRequest.quantity))
        index = sellingUser.stocks.index(sellRequest.stock)
        sellingUser.quantity[index] -= sellRequest.quantity
        sellingUser.valueSpend[index] -= (sellRequest.quantity * sellRequest.price)
        if sellingUser.quantity[index] == 0:
            del sellingUser.stocks[index]
            del sellingUser.quantity[index]
            del sellingUser.valueSpend[index]
        
        updateUsers()
        updateStocks()


def simulator():
    global listSells, listBuys, listUsers, listStocks, listUsers, europe, america

    #novaIorque = pytz.timezone("America/New_York")
    #relogioNovaIorque = datetime.now(novaIorque).time() #para definir o horario da bolsa americana

    #londres = pytz.timezone("Europe/London")
    #relogioLondres = datetime.now(londres).time() #para definir o horario da bolsa europeia

    if not listBuys: #se a tabela listaCompras nao estiver vazia
        pass
    else:
        for sellRequest in listSells: #iniciar com o pedido de venda
            if sellRequest.quantity == 0:
                continue
            elif sellRequest.stock in america: 
                if not aberturaAmerica < relogioNovaIorque < fechoAmerica: #se a bolsa americana estiver fechada nao ha transacao para os titulos americanos
                    continue
                else:
                    for buyRequest in listBuys:
                        if buyRequest.quantity == 0:
                            continue
                        elif sellRequest.stock == buyRequest.stock and sellRequest.price <= buyRequest.price: #se os titulos coinci
                            transaction(buyRequest, sellRequest)
                            if sellRequest.quantity == buyRequest.quantity:
                                buyRequest.quantity = 0
                                sellRequest.quantity = 0
                            else:
                                if sellRequest.quantity >= buyRequest.quantity:
                                    sellRequest.quantity -= buyRequest.quantity
                                    buyRequest.quantity = 0
                                else:
                                    buyRequest.quantity -= sellRequest.quantity
                                    sellRequest.quantity = 0
                            stock = [stock for stock in listStocks if stock.symbol == buyRequest.stock]
                            stock = stock[0]
                            stock.lastPrice = buyRequest.price #actualizar o precoActual do titulo
                            updateBuyRequests()
                            updateSellRequests
                        else:
                            continue
            elif sellRequest.stock in europe: 
                if not aberturaAmerica < relogioNovaIorque < fechoAmerica: #se a bolsa americana estiver fechada nao ha transacao para os titulos americanos
                    continue
                else:
                    for buyRequest in listBuys:
                        if buyRequest.quantity == 0:
                            continue
                        elif sellRequest.stock == buyRequest.stock and sellRequest.price <= buyRequest.price: #se os titulos coinci
                            transaction(buyRequest, sellRequest)
                            if sellRequest.quantity == buyRequest.quantity:
                                buyRequest.quantity = 0
                                sellRequest.quantity = 0
                            else:
                                if sellRequest.quantity >= buyRequest.quantity:
                                    sellRequest.quantity -= buyRequest.quantity
                                    buyRequest.quantity = 0
                                else:
                                    buyRequest.quantity -= sellRequest.quantity
                                    sellRequest.quantity = 0
                            stock = [stock for stock in listStocks if stock.symbol == buyRequest.stock]
                            stock = stock[0]
                            stock.lastPrice = buyRequest.price #actualizar o precoActual do titulo
                            updateBuyRequests()
                            updateSellRequests()
                        else:
                            continue

utilizador_1 = listaUtilizadores[0]
saldo_1 = 'Saldo disponível: ' + str(utilizador_1.saldo) + ' €'
portefolio1 = utilizador_1.paraLista()
utilizador_2 = listaUtilizadores[1]
saldo_2 = 'Saldo disponível: ' + str(utilizador_2.saldo) + ' €'
portefolio2 = utilizador_2.paraLista()
utilizador_3 = listaUtilizadores[2]
saldo_3 = 'Saldo disponível: ' + str(utilizador_3.saldo) + ' €'
portefolio3 = utilizador_3.paraLista()