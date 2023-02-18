from abc import ABC, abstractmethod
from currency_converter import CurrencyConverter #para converter as diferentes moedas
import pickle

from simulator import *

class Stock(ABC):  #information about the stocks   
    def __init__(self, symbol, company, currency, lastPrice, peRacio):
        self.symbol = str(symbol)
        self.company = str(company)
        self.currency = str(currency)
        self.peRacio = float(peRacio)

    @abstractmethod
    def convertCurrency(self, lastPrice):
        pass

class Europe(Stock): #stocks from Europe Markets
    def __init__(self, symbol, company, currency, lastPrice, peRacio):
        super().__init__(symbol, company, currency, lastPrice, peRacio)
        self.lastPrice = self.convertCurrency(lastPrice)
        
    def convertCurrency(self, value):
        converter = CurrencyConverter()
        value = float(value) #make sure the value is a float variable
        if self.currency == "GBP": #convert pounds to euros
            convertedValue = converter.convert(value, 'GBP', 'EUR')
            return float(convertedValue)
        elif self.currency == "CHF": #converter francos suicos para euros
            convertedValue = converter.convert(value, 'CHF', 'EUR')
            return float(convertedValue)
        else:
            return value
        
class America(Stock): #stocks from American Markets
    def __init__(self, symbol, company, currency, lastPrice, peRacio):
        super().__init__(symbol, company, currency, lastPrice, peRacio)
        self.lastPrice = self.convertCurrency(lastPrice)

    def convertCurrency(self, value):
        converter = CurrencyConverter()
        value = float(value)
        if self.currency == "USD": #convert dollar to euro
            convertedValue = converter.convert(value, 'USD', 'EUR')
            return convertedValue
        else:
            return value

def importEuropeStocks(): #function to manualy import the stock informantion from existing txt files
    global europe, listStocks
    for symbol in europe:
        file = open(symbol + '.txt', 'r') #to open "txt" files with the stock information
        lines = file.readlines()
        filteredLines = list(map(lambda s: s.strip(), lines)) #removes the '\n'
        file.close()
        stock = Europe(filteredLines[0], filteredLines[1], filteredLines[2], filteredLines[3], filteredLines[4])
        listStocks.append(stock)

def importAmericaStocks(): #function to manualy import the stock informantion from existing txt files
    global america, listStocks
    for symbol in america:
        file = open(symbol + '.txt', 'r') #to open "txt" files with the stock information
        lines = file.readlines()
        filteredLines = list(map(lambda s: s.strip(), lines)) #removes the '\n'
        file.close()
        stock = America(filteredLines[0], filteredLines[1], filteredLines[2], filteredLines[3], filteredLines[4])
        listStocks.append(stock)

def updateStocks(): #function to update the "pck" file with the stock information
    global listStocks
    for stock in listStocks:
        with open(stock.symbol + '.pkl', 'wb') as file:
            pickle.dump(stock, file)

def loadStocks():
    global europe, america, listStocks
    for symbol in europe:
        with open(symbol + '.pkl', 'rb') as file:
            stock = pickle.load(file)
            listStocks.append(stock)
    for symbol in america:
        with open(symbol + '.pkl', 'rb') as file:
            stock = pickle.load(file)
            listStocks.append(stock)