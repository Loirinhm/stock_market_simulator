from tkinter.ttk import *
from tkinter import *

from simulator import *
from buysellrequests import *
from stocks import *
from users import *

class Tabela: #para criar tabelas no Tkinter

        def __init__(self, root, numLinhas, numColunas, lista):
            self.root = root
            self.numLinhas = int(numLinhas)
            self.numColunas = int(numColunas)
            self.lista = lista


            # criar tabela
            for i in range(numLinhas):
                self.e = Entry(root, width=20, fg='black',
                               font=('Poppins', 10), justify=CENTER)
                for j in range(numColunas):
                    self.e = Entry(root, width=20, fg='black',
                               font=('Poppins', 10), justify=CENTER)

                    self.e.grid(row=i, column=j,)
                    self.e.insert(END, lista[i][j])

#criar uma lista com os atributos dos titulos para post passar a tabela
def titulosParaLista():
        global listaTitulos
        lista = []
        lista.append(('TÍTULO', 'NOME', 'MOEDA', 'PREÇO ACTUAL - EUR', 'RACIO P/E'))
        for titulo in listaTitulos:
            lista.append((titulo.titulo, titulo.nome, titulo.moeda, titulo.precoActual, titulo.racioPE))
        return lista          


# criar a janela da aplicacao
app = Tk()

# definir a dimensao da janela
app.geometry('500x500')

#definir o titulo
app.title('Simulador da Bolsa de Valores')

#titulo dentro da janela
label_1 = Label(app, text='Utilizadores', font=('Poppins', 20))
label_1.pack(padx=20, pady=20)

def utilizador1(): #janela para o utilizador 1
    app1 = Toplevel(app)

    app1.geometry('800x800')

    app1.title('Utilizador 1')

    def TabelaTitulosMercado(): #criar tabela com titulos mercado qnd premimos botao
        tab = Toplevel(app1)
        tab.title('Títulos Disponíveis no Mercado')

        lista = titulosParaLista()
        numLinhas = len(lista)
        numColunas = 5
        tabela = Tabela(tab, numLinhas, numColunas, lista)

    #botao para mostrar os titulos disponiveis 
    botaoTitulosCompra = Button(app1, text="Títulos Disponíveis no Mercado",  font=('Poppins, 16'), command=TabelaTitulosMercado)
    botaoTitulosCompra.place(x=20, y=20)

    #Para mostrar o saldo do utilizador
    labelSaldo = Label(app1, text=saldo_1, font=('Poppins, 16'))
    labelSaldo.place(x=450, y=25)

    ########### Para comprar titulos ###########
    labelCompra = Label(app1, text='Comprar Título', font=('Poppins, 16'))
    labelCompra.place(x=20, y=100)

    def comprar(): #para inicializar o pedido de compra
        utilizador = listaUtilizadores[0]
        titulo = comprarInputTitulo.get(1.0, "end-1c")
        quantidade = comprarInputQuantidade.get(1.0, "end-1c")
        preco = comprarInputPreco.get(1.0, "end-1c")
        if int(utilizador.saldo) >= int(quantidade) * float(preco): #para verificar se o saldo do utilizador é suficiente
            criarPedidoCompra(utilizador, titulo, quantidade, preco)
            comprarInputTitulo.delete(1.0, END) #para remover o que estava escrito nos campos
            comprarInputQuantidade.delete(1.0, END)
            comprarInputPreco.delete(1.0, END)
            saldoOK = Label(app1, text='Pedido feito com sucesso', font=('Poppins', 10), fg='green')
            saldoOK.place(x=140, y=308)
        else:  #se nao tiver saldo suficiente
            saldoErro = Label(app1, text='Saldo insuficiente', font=('Poppins', 10), fg='red')
            saldoErro.place(x=140, y=308)
    
    #Para receber o input do nome do titulo a comprar
    labelComprarInserirTitulo = Label(app1, text='Inserir nome do título', font=('Poppins, 8'))
    labelComprarInserirTitulo.place(x=30, y=140)
    comprarInputTitulo = Text(app1, height=1, width=25, font=('Poppins, 11'))
    comprarInputTitulo.place(x=30, y=160)

    #Para receber o input da quantidade a comprar
    labelComprarInserirQuantidade = Label(app1, text='Inserir quantidade', font=('Poppins, 8'))
    labelComprarInserirQuantidade.place(x=30, y=190)
    comprarInputQuantidade = Text(app1, height=1, width=25, font=('Poppins, 11'))
    comprarInputQuantidade.place(x=30, y=210)

    #Para receber o input do preco a pagar
    labelComprarInserirPreco = Label(app1, text='Inserir preço', font=('Poppins, 8'))
    labelComprarInserirPreco.place(x=30, y=240)
    comprarInputPreco = Text(app1, height=1, width=25, font=('Poppins, 11'))
    comprarInputPreco.place(x=30, y=260)

    botaoComprarTitulos = Button(app1, text="Comprar", font=('Poppins, 16'), command=comprar)
    botaoComprarTitulos.place(x=30, y=300)

    ########### Para Vender titulos ###########
    labelVenda = Label(app1, text='Vender Título', font=('Poppins, 16'))
    labelVenda.place(x=420, y=100)

    def vender(): #para inicializar o pedido de compra
        utilizador = listaUtilizadores[0]
        titulo = venderInputTitulo.get(1.0, "end-1c")
        quantidade = venderInputQuantidade.get(1.0, "end-1c")
        preco = venderInputPreco.get(1.0, "end-1c")
        criarPedidoVenda(utilizador, titulo, quantidade, preco)
        venderInputTitulo.delete(1.0, END) #para remover o que estava escrito nos campos
        venderInputQuantidade.delete(1.0, END)
        venderInputPreco.delete(1.0, END)

    #Para receber o input do nome do titulo a vender
    labelVenderInserirTitulo = Label(app1, text='Inserir nome do título', font=('Poppins, 8'))
    labelVenderInserirTitulo.place(x=430, y=140)
    venderInputTitulo = Text(app1, height=1, width=25, font=('Poppins, 11'))
    venderInputTitulo.place(x=430, y=160)

    #Para receber o input da quantidade a vender
    labelVenderInserirQuantidade = Label(app1, text='Inserir quantidade', font=('Poppins, 8'))
    labelVenderInserirQuantidade.place(x=430, y=190)
    venderInputQuantidade = Text(app1, height=1, width=25, font=('Poppins, 11'))
    venderInputQuantidade.place(x=430, y=210)

    #Para receber o input do preco a pagar
    labelVenderInserirPreco = Label(app1, text='Inserir preço', font=('Poppins, 8'))
    labelVenderInserirPreco.place(x=430, y=240)
    venderInputPreco = Text(app1, height=1, width=25, font=('Poppins, 11'))
    venderInputPreco.place(x=430, y=260)

    botaoVenderTitulos = Button(app1, text="Vender", font=('Poppins, 16'), command=vender)
    botaoVenderTitulos.place(x=430, y=300)


    #Label para o Portefolio
    app1_label1 = Label(app1, text='Portefólio', font=('Poppins', 20))
    app1_label1.place(x=100, y=400)

    #Numero de linhas e colunas total do Portefolio
    numLinhasPortefolio = len(utilizador_1.titulos) + 1
    numColunasPortefolio = 3

    #Tabela com o conteudo do portefolio
    frameTabela = Frame(app1)
    frameTabela.place(x=110, y=450)
    tabelaPortefolio = Tabela(frameTabela, numLinhasPortefolio, numColunasPortefolio, portefolio1)


def utilizador2():
    app2 = Toplevel(app)

    app2.geometry('800x800')

    app2.title('Utilizador 2')

    def TabelaTitulosMercado(): #criar tabela com titulos mercado qnd premimos botao
        tab = Toplevel(app2)
        tab.title('Títulos Disponíveis no Mercado')

        lista = titulosParaLista()
        numLinhas = len(lista)
        numColunas = 5
        tabela = Tabela(tab, numLinhas, numColunas, lista)

    #botao para mostrar os titulos disponiveis 
    botaoTitulosCompra = Button(app2, text="Títulos Disponíveis no Mercado",  font=('Poppins, 16'), command=TabelaTitulosMercado)
    botaoTitulosCompra.place(x=20, y=20)

    #Para mostrar o saldo do utilizador
    labelSaldo = Label(app2, text=saldo_2, font=('Poppins, 16'))
    labelSaldo.place(x=450, y=25)

    ########### Para comprar titulos ###########
    labelCompra = Label(app2, text='Comprar Título', font=('Poppins, 16'))
    labelCompra.place(x=20, y=100)

    def comprar(): #para inicializar o pedido de compra
        utilizador = listaUtilizadores[1]
        titulo = comprarInputTitulo.get(1.0, "end-1c")
        quantidade = comprarInputQuantidade.get(1.0, "end-1c")
        preco = comprarInputPreco.get(1.0, "end-1c")
        if int(utilizador.saldo) >= int(quantidade) * float(preco): #para verificar se o saldo do utilizador é suficiente
            criarPedidoCompra(utilizador, titulo, quantidade, preco)
            comprarInputTitulo.delete(1.0, END) #para remover o que estava escrito nos campos
            comprarInputQuantidade.delete(1.0, END)
            comprarInputPreco.delete(1.0, END)
            saldoOK = Label(app2, text='Pedido feito com sucesso', font=('Poppins', 10), fg='green')
            saldoOK.place(x=140, y=308)
        else: #se nao tiver saldo suficiente
            saldoErro = Label(app2, text='Saldo insuficiente', font=('Poppins', 10), fg='red')
            saldoErro.place(x=140, y=308)

    #Para receber o input do nome do titulo a comprar
    labelComprarInserirTitulo = Label(app2, text='Inserir nome do título', font=('Poppins, 8'))
    labelComprarInserirTitulo.place(x=30, y=140)
    comprarInputTitulo = Text(app2, height=1, width=25, font=('Poppins, 11'))
    comprarInputTitulo.place(x=30, y=160)

    #Para receber o input da quantidade a comprar
    labelComprarInserirQuantidade = Label(app2, text='Inserir quantidade', font=('Poppins, 8'))
    labelComprarInserirQuantidade.place(x=30, y=190)
    comprarInputQuantidade = Text(app2, height=1, width=25, font=('Poppins, 11'))
    comprarInputQuantidade.place(x=30, y=210)

    #Para receber o input do preco a pagar
    labelComprarInserirPreco = Label(app2, text='Inserir preço', font=('Poppins, 8'))
    labelComprarInserirPreco.place(x=30, y=240)
    comprarInputPreco = Text(app2, height=1, width=25, font=('Poppins, 11'))
    comprarInputPreco.place(x=30, y=260)

    botaoComprarTitulos = Button(app2, text="Comprar", font=('Poppins, 16'), command=comprar)
    botaoComprarTitulos.place(x=30, y=300)

    ########### Para Vender titulos ###########
    labelVenda = Label(app2, text='Vender Título', font=('Poppins, 16'))
    labelVenda.place(x=420, y=100)

    def vender(): #para inicializar o pedido de compra
        utilizador = listaUtilizadores[1]
        titulo = venderInputTitulo.get(1.0, "end-1c")
        quantidade = venderInputQuantidade.get(1.0, "end-1c")
        preco = venderInputPreco.get(1.0, "end-1c")
        criarPedidoVenda(utilizador, titulo, quantidade, preco)
        venderInputTitulo.delete(1.0, END) #para remover o que estava escrito nos campos
        venderInputQuantidade.delete(1.0, END)
        venderInputPreco.delete(1.0, END)

    #Para receber o input do nome do titulo a vender
    labelVenderInserirTitulo = Label(app2, text='Inserir nome do título', font=('Poppins, 8'))
    labelVenderInserirTitulo.place(x=430, y=140)
    venderInputTitulo = Text(app2, height=1, width=25, font=('Poppins, 11'))
    venderInputTitulo.place(x=430, y=160)

    #Para receber o input da quantidade a vender
    labelVenderInserirQuantidade = Label(app2, text='Inserir quantidade', font=('Poppins, 8'))
    labelVenderInserirQuantidade.place(x=430, y=190)
    venderInputQuantidade = Text(app2, height=1, width=25, font=('Poppins, 11'))
    venderInputQuantidade.place(x=430, y=210)

    #Para receber o input do preco a pagar
    labelVenderInserirPreco = Label(app2, text='Inserir preço', font=('Poppins, 8'))
    labelVenderInserirPreco.place(x=430, y=240)
    venderInputPreco = Text(app2, height=1, width=25, font=('Poppins, 11'))
    venderInputPreco.place(x=430, y=260)

    botaoVenderTitulos = Button(app2, text="Vender", font=('Poppins, 16'), command=vender)
    botaoVenderTitulos.place(x=430, y=300)


    #Label para o Portefolio
    app1_label1 = Label(app2, text='Portefólio', font=('Poppins', 20))
    app1_label1.place(x=100, y=400)

    #Numero de linhas e colunas total do Portefolio
    numLinhasPortefolio = len(utilizador_2.titulos) + 1
    numColunasPortefolio = 3

    #Tabela com o conteudo do portefolio
    frameTabela = Frame(app2)
    frameTabela.place(x=110, y=450)
    tabelaPortefolio = Tabela(frameTabela, numLinhasPortefolio, numColunasPortefolio, portefolio2)


def utilizador3():
    app3 = Toplevel(app)

    app3.geometry('800x800')

    app3.title('Utilizador 3')

    def TabelaTitulosMercado(): #criar tabela com titulos mercado qnd premimos botao
        tab = Toplevel(app3)
        tab.title('Títulos Disponíveis no Mercado')

        lista = titulosParaLista()
        numLinhas = len(lista)
        numColunas = 5
        tabela = Tabela(tab, numLinhas, numColunas, lista)

    #botao para mostrar os titulos disponiveis 
    botaoTitulosCompra = Button(app3, text="Títulos Disponíveis no Mercado",  font=('Poppins, 16'), command=TabelaTitulosMercado)
    botaoTitulosCompra.place(x=20, y=20)

    #Para mostrar o saldo do utilizador
    labelSaldo = Label(app3, text=saldo_3, font=('Poppins, 16'))
    labelSaldo.place(x=450, y=25)

    ########### Para comprar titulos ###########
    labelCompra = Label(app3, text='Comprar Título', font=('Poppins, 16'))
    labelCompra.place(x=20, y=100)

    def comprar(): #para inicializar o pedido de compra
        utilizador = listaUtilizadores[2]
        titulo = comprarInputTitulo.get(1.0, "end-1c")
        quantidade = comprarInputQuantidade.get(1.0, "end-1c")
        preco = comprarInputPreco.get(1.0, "end-1c")
        if int(utilizador.saldo) >= int(quantidade) * float(preco):
            criarPedidoCompra(utilizador, titulo, quantidade, preco)
            comprarInputTitulo.delete(1.0, END) #para remover o que estava escrito nos campos
            comprarInputQuantidade.delete(1.0, END)
            comprarInputPreco.delete(1.0, END)
            saldoOK = Label(app3, text='Pedido feito com sucesso', font=('Poppins', 10), fg='green')
            saldoOK.place(x=140, y=308)
        else:
            saldoErro = Label(app3, text='Saldo insuficiente', font=('Poppins', 10), fg='red')
            saldoErro.place(x=140, y=308)

    #Para receber o input do nome do titulo a comprar
    labelComprarInserirTitulo = Label(app3, text='Inserir nome do título', font=('Poppins, 8'))
    labelComprarInserirTitulo.place(x=30, y=140)
    comprarInputTitulo = Text(app3, height=1, width=25, font=('Poppins, 11'))
    comprarInputTitulo.place(x=30, y=160)

    #Para receber o input da quantidade a comprar
    labelComprarInserirQuantidade = Label(app3, text='Inserir quantidade', font=('Poppins, 8'))
    labelComprarInserirQuantidade.place(x=30, y=190)
    comprarInputQuantidade = Text(app3, height=1, width=25, font=('Poppins, 11'))
    comprarInputQuantidade.place(x=30, y=210)

    #Para receber o input do preco a pagar
    labelComprarInserirPreco = Label(app3, text='Inserir preço', font=('Poppins, 8'))
    labelComprarInserirPreco.place(x=30, y=240)
    comprarInputPreco = Text(app3, height=1, width=25, font=('Poppins, 11'))
    comprarInputPreco.place(x=30, y=260)

    botaoComprarTitulos = Button(app3, text="Comprar", font=('Poppins, 16'), command=comprar)
    botaoComprarTitulos.place(x=30, y=300)

    ########### Para Vender titulos ###########
    labelVenda = Label(app3, text='Vender Título', font=('Poppins, 16'))
    labelVenda.place(x=420, y=100)

    def vender(): #para inicializar o pedido de compra
        utilizador = listaUtilizadores[2]
        titulo = venderInputTitulo.get(1.0, "end-1c")
        quantidade = venderInputQuantidade.get(1.0, "end-1c")
        preco = venderInputPreco.get(1.0, "end-1c")
        criarPedidoVenda(utilizador, titulo, quantidade, preco)
        venderInputTitulo.delete(1.0, END) #para remover o que estava escrito nos campos
        venderInputQuantidade.delete(1.0, END)
        venderInputPreco.delete(1.0, END)

    #Para receber o input do nome do titulo a vender
    labelVenderInserirTitulo = Label(app3, text='Inserir nome do título', font=('Poppins, 8'))
    labelVenderInserirTitulo.place(x=430, y=140)
    venderInputTitulo = Text(app3, height=1, width=25, font=('Poppins, 11'))
    venderInputTitulo.place(x=430, y=160)

    #Para receber o input da quantidade a vender
    labelVenderInserirQuantidade = Label(app3, text='Inserir quantidade', font=('Poppins, 8'))
    labelVenderInserirQuantidade.place(x=430, y=190)
    venderInputQuantidade = Text(app3, height=1, width=25, font=('Poppins, 11'))
    venderInputQuantidade.place(x=430, y=210)

    #Para receber o input do preco a pagar
    labelVenderInserirPreco = Label(app3, text='Inserir preço', font=('Poppins, 8'))
    labelVenderInserirPreco.place(x=430, y=240)
    venderInputPreco = Text(app3, height=1, width=25, font=('Poppins, 11'))
    venderInputPreco.place(x=430, y=260)

    botaoVenderTitulos = Button(app3, text="Vender", font=('Poppins, 16'), command=vender)
    botaoVenderTitulos.place(x=430, y=300)


    #Label para o Portefolio
    app1_label1 = Label(app3, text='Portefólio', font=('Poppins', 20))
    app1_label1.place(x=100, y=400)

    #Numero de linhas e colunas total do Portefolio
    numLinhasPortefolio = len(utilizador_3.titulos) + 1
    numColunasPortefolio = 3

    #Tabela com o conteudo do portefolio
    frameTabela = Frame(app3)
    frameTabela.place(x=110, y=450)
    tabelaPortefolio = Tabela(frameTabela, numLinhasPortefolio, numColunasPortefolio, portefolio3)
    


#botoes para abrir a interface do utilizador
botao1 = Button(app, text='Utilizador 1', font=('Poppins, 16'), command=utilizador1)
botao1.pack(padx=20, pady=20)
botao2 = Button(app, text='Utilizador 2', font=('Poppins, 16'), command=utilizador2)
botao2.pack(padx=20, pady=20)
botao3 = Button(app, text='Utilizador 3', font=('Poppins, 16'), command=utilizador3)
botao3.pack(padx=20, pady=20)


mainloop()