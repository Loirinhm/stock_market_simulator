import pickle

def makeBuyRequest(user, stock, price, quantity):
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

def makeSellRequest(user, stock, price, quantity):
    global listSells, sellRequestId
    request = Request(user.id, stock, price, quantity)
    listSells.append(request)
    sellRequestId = int(pedidoVendaId)
    pedidoVendaId += 1
    pedidoVendaId = str(pedidoVendaId)
    with open('pedidoVendaId' + '.txt', 'w') as ficheiro:
        ficheiro.write(pedidoVendaId)
    nome_pedido = 'pedidoVenda_' + pedidoVendaId
    with open(nome_pedido + '.pkl', 'wb') as ficheiro:
        pickle.dump(pedido, ficheiro)
    transacao() #assim que um novo pedido é criado a funcao transacao e executada


def criarPedidos(): #funcao para acrescentar pedidos e guarda-los em formato pickle
   id += 1
   quantidade = input('Inserir quantidade de titulos a vender: ')
   preco= input('Inserir preco do titulo: ')
   utilizador = Utilizador(id, nome, saldo)
   nome_utilizador = str('utilizador_') + str(utilizador.id)
   with open(nome_utilizador + '.pkl', 'wb') as ficheiro:
      pickle.dump(utilizador, ficheiro)

def carregarPedidos(): #para carregar os utilizadores ja criados
   global id, listaUtilizadores
   for i in range(1, 4):
        id += 1
        nome_utilizador = str('utilizador_') + str(id)
        with open(nome_utilizador + '.pkl', 'rb') as ficheiro:
            utilizador = pickle.load(ficheiro)
            listaUtilizadores.append(utilizador)

