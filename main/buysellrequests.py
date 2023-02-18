import pickle

from simulator import *

class Request():
    def __init__(self, id, stock, price, quantity):
        self.id = int(id)
        self.stock = str(stock)
        self.price = float(price) #preco por cada accao
        self.quantity = int(quantity)

def createBuyRequest(user, stock, price, quantity):
    global listBuys, buyRequestId
    request = Request(user.id, stock, price, quantity)
    listBuys.append(request)
    buyRequestId = int(buyRequestId) + 1
    buyRequestId = str(buyRequestId)
    with open('buyRequestId' + '.txt', 'w') as file:
        file.write(buyRequestId)
    requestName = 'buyRequest_' + buyRequestId
    with open(requestName + '.pkl', 'wb') as file:
        pickle.dump(request, file)
    simulator() #assim que um novo pedido é criado a funcao transacao e executada

def createSellRequest(user, stock, price, quantity):
    global listSells, sellRequestId
    request = Request(user.id, stock, price, quantity)
    listSells.append(request)
    sellRequestId = int(sellRequestId) + 1
    sellRequestId = str(sellRequestId)
    with open('sellRequestId' + '.txt', 'w') as file:
        ficheiro.write(sellRequestId)
    requestName = 'sellRequest_' + sellRequestId
    with open(requestName + '.pkl', 'wb') as ficheiro:
        pickle.dump(request, ficheiro)
    simulator() #assim que um novo pedido é criado a funcao transacao e executada

def loadRequest():
    global buyRequestId, sellRequestId, listBuys, listSells
    for i in range(0, int(buyRequestId)):
        id = 1
        requestName = 'buyRequest_' + str(id)
        with open(requestName + '.pkl', 'rb') as file:
            request = pickle.load(file)
        listBuys.append(request)
        id += 1
    for i in range(0, int(sellRequestId)):
        id = 1
        requestName = 'sellRequest_' + str(id)
        with open(requestName + '.pkl', 'rb') as file:
            request = pickle.load(file)
        listSells.append(request)
        id += 1

def atualizarPedidosCompra():
    global listaCompras
    for pedido in listaCompras:
        id = 1
        nome_pedido = 'pedidoCompra_' + str(id)
        with open(nome_pedido + '.pkl', 'wb') as ficheiro:
            pickle.dump(pedido, ficheiro)
        id += 1

def atualizarPedidosVenda():
    global listaVendas
    for pedido in listaVendas:
        id = 1
        nome_pedido = 'pedidoVenda_' + str(id)
        with open(nome_pedido + '.pkl', 'wb') as ficheiro:
            pickle.dump(pedido, ficheiro)
        id += 1