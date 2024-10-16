from Prodotto import Prodotto
import csv

class Magazzino:
    def __init__(self, lista):
        self.lista = []

    def aggiungi_prodotto(self, Prodotto):
        self.lista.append(Prodotto)

    def rimuovi_prodotto(self, Nome_prodotto):
        for Prodotto in self.lista:
            if Prodotto.nome == Nome_prodotto:
                self.lista.remove(Prodotto)
                return
        print(f"prodotto '{Nome_prodotto}' non trovato nel magazzino")

    def valore_totale(self):
        valore = 0
        for Prodotto in self.lista:
            valore += prodotto.calcola_valore()

    def salva_su_file(self, nome_file):
        nome_file = "Oggetti nel magazzino"
        with open(nome_file, mode='w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)
            csvwriter.writerows(data)

    def visualizza_magazzino(self):
        for Prodotto in self.lista:
            print({Prodotto.nome}, {Prodotto.prezzo}, {Prodotto.quantita})


magazzino= Magazzino()
pizza = Prodotto("pizza", 20,400)
pane = Prodotto("Pane", 2, 1000)
magazzino.aggiungi_prodotto(pizza)
magazzino.aggiungi_prodotto(pane)