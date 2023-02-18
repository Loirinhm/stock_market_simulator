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

ficheiro = open('pedidoCompraID' + '.txt', 'r')
pedidoCompraId = ficheiro.readline()
ficheiro.close()

ficheiro = open('pedidoVendaID' + '.txt', 'r')
pedidoVendaId = ficheiro.readline()
ficheiro.close()

europe = ['NESN.SW', 'ASML.AS', 'ROG.SW', 'AZN.L', 'SHEL.L'] #lista de titulos de empresas europeias
america = ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'GOOGL'] #lista de titulos de empresas americanas

aberturaAmerica = time(9, 0, 0)
fechoAmerica = time(22, 0, 0)

aberturaEuropa = time(8, 0, 0)
fechoEuropa = time(22, 30, 00)

listSells = [] #lista dos pedidos de venda
listBuys = [] #lista dos pedidos de compra
listUsers =[]
listStocks = []

def transaction():
    pass

def simulator():
    global listaCompras, listaVendas, listaUtilizadores, listaTitulos, europa, america

    novaIorque = pytz.timezone("America/New_York")
    relogioNovaIorque = datetime.now(novaIorque).time() #para definir o horario da bolsa americana

    londres = pytz.timezone("Europe/London")
    relogioLondres = datetime.now(londres).time() #para definir o horario da bolsa europeia

    if not listaCompras: #se a tabela listaCompras nao estiver vazia
        pass
    else:
        for pedidoVenda in listaVendas: #iniciar com o pedido de venda
            if pedidoVenda.quantidade == 0:
                continue
            elif pedidoVenda.titulo in america: 
                if not aberturaAmerica < relogioNovaIorque < fechoAmerica: #se a bolsa americana estiver fechada nao ha transacao para os titulos americanos
                    continue
                else:
                    for pedidoCompra in listaCompras:
                        if pedidoCompra.quantidade == 0:
                            continue
                        elif pedidoVenda.titulo == pedidoCompra.titulo: #se os titulos coinci
                            if pedidoVenda.preco <= pedidoCompra.preco and pedidoVenda.quantidade == pedidoCompra.quantidade:
                                utilizadorCompraL = [utilizador for utilizador in listaUtilizadores if pedidoCompra.id == utilizador.id] #saber o utilizador que fez o pedido de compra
                                utilizadorCompra = utilizadorCompraL[0]
                                utilizadorCompra.saldo = float(utilizadorCompra.saldo) - (float(pedidoCompra.preco) * int(pedidoCompra.quantidade)) # atualizar o saldo do utilizador
                                if pedidoCompra.titulo in utilizadorCompra.titulos: #procurar na lista de titulos do utilizador o tilulo da transacao
                                    #se o titulo existir, fazer a atualizacao dos dados
                                    indice = utilizadorCompra.titulos.index(pedidoCompra.titulo) #saber o indice do titulo na lista
                                    utilizadorCompra.quantidade[indice] += pedidoCompra.quantidade #actualizar a quantidade no portefolio do utilizador
                                    utilizadorCompra.valorGasto[indice] += (pedidoCompra.preco * pedidoCompra.quantidade) #actualizar no portefolio o valor gasto neste titulo
                                else:
                                    utilizadorCompra.titulos.append(pedidoCompra.titulo)
                                    utilizadorCompra.quantidade.append(pedidoCompra.quantidade)
                                    utilizadorCompra.valorGasto.append((pedidoCompra.preco * pedidoCompra.quantidade))
                
                                utilizadorVendaL = [utilizador for utilizador in listaUtilizadores if pedidoVenda.id == utilizador.id] #saber que utilizador fez o pedido de venda
                                utilizadorVenda = utilizadorVendaL[0]
                                utilizadorVenda.saldo = float(utilizadorCompra.saldo) + (float(pedidoCompra.preco) * int(pedidoCompra.quantidade))
                                if pedidoVenda.titulo in utilizadorVenda.titulos: #procurar o titulo na lista de titulos do respetivo utilizador
                                    indice = utilizadorVenda.titulos.index(pedidoVenda.titulo)
                                    utilizadorVenda.quantidade[indice] -= pedidoVenda.quantidade
                                    utilizadorVenda.valorGasto[indice] -= (pedidoVenda.quantidade * pedidoVenda.preco)
                                pedidoCompra.quantidade = 0
                                pedidoVenda.quantidade = 0
                                atualizarUtilizadores()
                                atualizarTitulos()
                                atualizarPedidosVenda()
                                atualizarPedidosCompra()
                            elif pedidoVenda.preco <= pedidoCompra.preco and pedidoVenda.quantidade != pedidoCompra.quantidade:
                                if pedidoVenda.quantidade >= pedidoCompra.quantidade:
                                    pedidoVenda.quantidade = pedidoVenda.quantidade - pedidoCompra.quantidade
                                    pedidoCompra.quantidade = 0
                                else:
                                    pedidoCompra.quantidade = pedidoCompra.quantidade - pedidoVenda.quantidade
                                    pedidoVenda.quantidade = 0
                                utilizadorCompraL = [utilizador for utilizador in listaUtilizadores if pedidoCompra.id == utilizador.id] #saber o utilizador que fez o pedido de compra
                                utilizadorCompra = utilizadorCompraL[0]
                                utilizadorCompra.saldo = float(utilizadorCompra.saldo) - (float(pedidoCompra.preco) * int(pedidoCompra.quantidade)) # atualizar o saldo do utilizador
                                if pedidoCompra.titulo in utilizadorCompra.titulos: #procurar na lista de titulos do utilizador o tilulo da transacao
                                    #se o titulo existir, fazer a atualizacao dos dados
                                    indice = utilizadorCompra.titulos.index(pedidoCompra.titulo) #saber o indice do titulo na lista
                                    utilizadorCompra.quantidade[indice] += pedidoCompra.quantidade #actualizar a quantidade no portefolio do utilizador
                                    utilizadorCompra.valorGasto[indice] += (pedidoCompra.preco * pedidoCompra.quantidade) #actualizar no portefolio o valor gasto neste titulo
                                else:
                                    utilizadorCompra.titulos.append(pedidoCompra.titulo)
                                    utilizadorCompra.quantidade.append(pedidoCompra.quantidade)
                                    utilizadorCompra.valorGasto.append((pedidoCompra.preco * pedidoCompra.quantidade))
                
                                utilizadorVendaL = [utilizador for utilizador in listaUtilizadores if pedidoVenda.id == utilizador.id] #saber que utilizador fez o pedido de venda
                                utilizadorVenda = utilizadorVendaL[0]
                                utilizadorVenda.saldo = float(utilizadorCompra.saldo) + (float(pedidoCompra.preco) * int(pedidoCompra.quantidade))
                                if pedidoVenda.titulo in utilizadorVenda.titulos: #procurar o titulo na lista de titulos do respetivo utilizador
                                    indice = utilizadorVenda.titulos.index(pedidoVenda.titulo)
                                    utilizadorVenda.quantidade[indice] -= pedidoVenda.quantidade
                                    utilizadorVenda.valorGasto[indice] -= (pedidoVenda.quantidade * pedidoVenda.preco)
                                atualizarUtilizadores()
                                atualizarTitulos()
                                atualizarPedidosVenda()
                                atualizarPedidosCompra()
                            # tituloL = [titulo for titulo in listaTitulos if titulo == pedidoVenda.titulo]
                            # titulo = tituloL[0]
                            # titulo.precoActual = pedidoVenda.preco #actualizar o precoActual do titulo
                            else:
                                continue
                        else:
                            continue
            elif pedidoVenda.titulo in europa:
                if not aberturaEuropa < relogioLondres < fechoEuropa: #se a bolsa europeia estiver fechada nao ha transacao para os titulos europeus
                    continue
                else:
                    for pedidoCompra in listaCompras:
                        if pedidoCompra.quantidade == 0:
                            continue
                        elif pedidoVenda.titulo == pedidoCompra.titulo: #se os titulos coinci
                            if pedidoVenda.preco <= pedidoCompra.preco and pedidoVenda.quantidade == pedidoCompra.quantidade:
                                utilizadorCompraL = [utilizador for utilizador in listaUtilizadores if pedidoCompra.id == utilizador.id] #saber o utilizador que fez o pedido de compra
                                utilizadorCompra = utilizadorCompraL[0]
                                utilizadorCompra.saldo = float(utilizadorCompra.saldo) - (float(pedidoCompra.preco) * int(pedidoCompra.quantidade)) # atualizar o saldo do utilizador
                                if pedidoCompra.titulo in utilizadorCompra.titulos: #procurar na lista de titulos do utilizador o tilulo da transacao
                                    #se o titulo existir, fazer a atualizacao dos dados
                                    indice = utilizadorCompra.titulos.index(pedidoCompra.titulo) #saber o indice do titulo na lista
                                    utilizadorCompra.quantidade[indice] += pedidoCompra.quantidade #actualizar a quantidade no portefolio do utilizador
                                    utilizadorCompra.valorGasto[indice] += (pedidoCompra.preco * pedidoCompra.quantidade) #actualizar no portefolio o valor gasto neste titulo
                                else:
                                    utilizadorCompra.titulos.append(pedidoCompra.titulo)
                                    utilizadorCompra.quantidade.append(pedidoCompra.quantidade)
                                    utilizadorCompra.valorGasto.append((pedidoCompra.preco * pedidoCompra.quantidade))
                
                                utilizadorVendaL = [utilizador for utilizador in listaUtilizadores if pedidoVenda.id == utilizador.id] #saber que utilizador fez o pedido de venda
                                utilizadorVenda = utilizadorVendaL[0]
                                utilizadorVenda.saldo = float(utilizadorCompra.saldo) + (float(pedidoCompra.preco) * int(pedidoCompra.quantidade))
                                if pedidoVenda.titulo in utilizadorVenda.titulos: #procurar o titulo na lista de titulos do respetivo utilizador
                                    indice = utilizadorVenda.titulos.index(pedidoVenda.titulo)
                                    utilizadorVenda.quantidade[indice] -= pedidoVenda.quantidade
                                    utilizadorVenda.valorGasto[indice] -= (pedidoVenda.quantidade * pedidoVenda.preco)
                                pedidoCompra.quantidade = 0
                                pedidoVenda.quantidade = 0
                                atualizarUtilizadores()
                                atualizarTitulos()
                                atualizarPedidosVenda()
                                atualizarPedidosCompra()
                            elif pedidoVenda.preco <= pedidoCompra.preco and pedidoVenda.quantidade != pedidoCompra.quantidade:
                                if pedidoVenda.quantidade >= pedidoCompra.quantidade:
                                    pedidoVenda.quantidade = pedidoVenda.quantidade - pedidoCompra.quantidade
                                    pedidoCompra.quantidade = 0
                                else:
                                    pedidoCompra.quantidade = pedidoCompra.quantidade - pedidoVenda.quantidade
                                    pedidoVenda.quantidade = 0
                                utilizadorCompraL = [utilizador for utilizador in listaUtilizadores if pedidoCompra.id == utilizador.id] #saber o utilizador que fez o pedido de compra
                                utilizadorCompra = utilizadorCompraL[0]
                                utilizadorCompra.saldo = float(utilizadorCompra.saldo) - (float(pedidoCompra.preco) * int(pedidoCompra.quantidade)) # atualizar o saldo do utilizador
                                if pedidoCompra.titulo in utilizadorCompra.titulos: #procurar na lista de titulos do utilizador o tilulo da transacao
                                    #se o titulo existir, fazer a atualizacao dos dados
                                    indice = utilizadorCompra.titulos.index(pedidoCompra.titulo) #saber o indice do titulo na lista
                                    utilizadorCompra.quantidade[indice] += pedidoCompra.quantidade #actualizar a quantidade no portefolio do utilizador
                                    utilizadorCompra.valorGasto[indice] += (pedidoCompra.preco * pedidoCompra.quantidade) #actualizar no portefolio o valor gasto neste titulo
                                else:
                                    utilizadorCompra.titulos.append(pedidoCompra.titulo)
                                    utilizadorCompra.quantidade.append(pedidoCompra.quantidade)
                                    utilizadorCompra.valorGasto.append((pedidoCompra.preco * pedidoCompra.quantidade))
                
                                utilizadorVendaL = [utilizador for utilizador in listaUtilizadores if pedidoVenda.id == utilizador.id] #saber que utilizador fez o pedido de venda
                                utilizadorVenda = utilizadorVendaL[0]
                                utilizadorVenda.saldo = float(utilizadorCompra.saldo) + (float(pedidoCompra.preco) * int(pedidoCompra.quantidade))
                                if pedidoVenda.titulo in utilizadorVenda.titulos: #procurar o titulo na lista de titulos do respetivo utilizador
                                    indice = utilizadorVenda.titulos.index(pedidoVenda.titulo)
                                    utilizadorVenda.quantidade[indice] -= pedidoVenda.quantidade
                                    utilizadorVenda.valorGasto[indice] -= (pedidoVenda.quantidade * pedidoVenda.preco)
                                atualizarUtilizadores()
                                atualizarTitulos()
                                atualizarPedidosVenda()
                                atualizarPedidosCompra()
                            # tituloL = [titulo for titulo in listaTitulos if titulo == pedidoVenda.titulo]
                            # titulo = tituloL[0]
                            # titulo.precoActual = pedidoVenda.preco #actualizar o precoActual do titulo
                            else:
                                continue
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