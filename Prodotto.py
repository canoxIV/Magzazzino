class Prodotto:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def getnome(self, nome):
        return self.nome

    def getprezzo(self, prezzo):
        return self.prezzo

    def getquantita(self, quantita):
        return self.quantita

    def setnome(self, nome):
        self.nome = nome

    def setprezzo(self, prezzo):
        self.prezzo = prezzo

    def setquantita(self, quantita):
        self.quantita = quantita

    def calcola_valore(self, prezzo, quantita):
        return prezzo*quantita

    def aggiorna_quantita(self, nuova_quantita):
        self.quantita = nuova_quantita

    def tostring(self):
        return "nome: " + self.nome + ",prezzo: " + str(self.prezzo) + ",quantita " + str(self.quantita)

