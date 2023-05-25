from Persona import Persona
import random
from Controllo import controllo

# Classe figlio
# attributi ereditati: nome, cognome
# attributi proprietari: password, primo_ingresso, ore_ferie, inquadramento_aziendale, reparto
class Dipendente(Persona):
    password = ""
    primo_ingresso = True
    ore_Ferie = 0

    def __init__(self, nome, cognome, inquadramento_aziendale, reparto):
        super().__init__(nome, cognome)
        self.inquadramento_aziendale = inquadramento_aziendale
        self.reparto = reparto

    # metodo che genera una password d'accesso in maniera randomica
    def genera_password(self, n):
        self.password = ""
        char_list = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "a",
            "B",
            "b",
            "C",
            "c",
            "D",
            "d",
            "E",
            "e",
            "F",
            "f",
            "G",
            "g",
            "H",
            "h",
            "I",
            "i",
            "J",
            "j",
            "K",
            "k",
            "L",
            "l",
            "M",
            "m",
            "N",
            "n",
            "O",
            "o",
            "P",
            "p",
            "Q",
            "q",
            "R",
            "r",
            "S",
            "s",
            "T",
            "t",
            "U",
            "u",
            "V",
            "v",
            "W",
            "w",
            "X",
            "x",
            "Y",
            "y",
            "Z",
            "z",
        ]
        for i in range(0, n):
            self.password += char_list[random.randint(0, 61)]
        return self.password

    def to_string(self):
        return (
            super().to_string()
            + f" lavora nel reparto {self.reparto} con un inquadramento_aziendale {self.inquadramento_aziendale}"
        )

    # metodo che calcolo lo stipendio del Dipendente in base ad un parametro
    def calcola_stipendio(self):
        stipendio_base = {1: 1200, 2: 1500, 3: 2000, 4: 3000}
        coefficiente = {1: 1, 2: 1.1, 3: 1.2, 4: 1.3, 5: 1.4, 6: 1.5, 7: 2, 8: 2.5}
        stipendio = (
            stipendio_base[self.reparto] * coefficiente[self.inquadramento_aziendale]
        )
        print(f"Il tuo stipendio è: {stipendio}€")

    # metodo per inserire le ferie
    def settaFerie(self):
        flag = True
        while flag:
            print("Aggiungi orario ferie")
            print("Premi 1 per aggiornare le tue ferie 2 per uscire")
            scelta = input("Inserisci la tua risposta\n")
            if scelta == "1":
                print("Puoi richiedere fino a un massimo di 5 ore di ferie")
                nuove_ore = input("Inserisci le ore che vuoi richiedere\n")
                if controllo(1, 6, nuove_ore):
                    self.ore_Ferie = int(nuove_ore)
                    print("Ferie accettate")
                    flag = False
                else:
                    print("Inserire un comando valido")

            elif scelta == "2":
                print("Stai uscendo dal sistema...")
                flag = False

            else:
                print("Inserisci numero valido\n")

