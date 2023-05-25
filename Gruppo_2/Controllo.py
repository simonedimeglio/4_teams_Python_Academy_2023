# Funzione controllo: verifica se un elemento (str) sia compreso nel range tra a e b (int)
def controllo(a, b, elemento):
    valori_accettabili = [str(iteratore) for iteratore in range(a, b)]
    if elemento in valori_accettabili:
        return True
    else:
        return False

