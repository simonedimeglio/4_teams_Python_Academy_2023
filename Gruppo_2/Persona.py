# Classe padre
# attributi: nome, cognome
class Persona:
    # metodo costruttore con attributi: nome, cognome
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    # metodo toString(Stampa una stringa contenente gli attributi dichiarati in precedenza)
    def to_string(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"

