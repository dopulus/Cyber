import random

def lancia_pallina():
    return random.randint(0, 36)

def verifica_vincita(tipo_giocata, scelta, numero_estratto):
    if tipo_giocata == "numero":
        return scelta == numero_estratto

    elif tipo_giocata == "parita":
        if numero_estratto == 0:
            return False
        if scelta == "pari":
            return numero_estratto % 2 == 0
        else:
            return numero_estratto % 2 != 0

    return False

def calcola_vincita(tipo_giocata, puntata):
    if tipo_giocata == "numero":
        return puntata * 36
    elif tipo_giocata == "parita":
        return puntata * 2
    elif tipo_giocata == "colore":
        return puntata * 2
    return 0

def coloreAssegato(numero):
    rosso = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
    nero = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}
    if numero in rosso:
        return "rosso"
    elif numero in nero:
        return "nero"
    else:
        return "verde"

def main(crediti=None):
    if crediti is None:
        crediti = 100
    print(f"Benvenuto alla Roulette! Crediti iniziali: {crediti}")

    while crediti > 0:
        try:
            puntata = input("Quanto vuoi puntare? (Numero/tutto): ")
            if puntata == "tutto":
                puntata = crediti
            else:
                puntata = int(puntata)
            if puntata <= 0 or puntata > crediti:
                print("Puntata non valida.")
                continue
        except ValueError:
            print("Inserisci un numero valido.")
            continue

        tipo_giocata = input("Tipo di giocata (numero/parita/colore): ").lower()

        if tipo_giocata == "numero":
            try:
                scelta = int(input("Scegli un numero tra 0 e 36: "))
                if scelta < 0 or scelta > 36:
                    print("Numero non valido.")
                    continue
            except ValueError:
                print("Devi inserire un numero.")
                continue

        elif tipo_giocata == "parita":
            scelta = input("Scegli (pari/dispari): ").lower()
            if scelta not in ["pari", "dispari"]:
                print("Scelta non valida.")
                continue
        
        elif tipo_giocata == "colore":
            scelta = input("Scegli (rosso/nero): ").lower()
            if scelta not in ["rosso", "nero"]:
                print("Scelta non valida.")
                continue
        else:
            print("Tipo di giocata non valido.")
            continue

        crediti -= puntata
        numero_estratto = lancia_pallina()

        if tipo_giocata == "colore":
            colore = coloreAssegato(numero_estratto)
            if scelta == colore:
                vincita = calcola_vincita(tipo_giocata, puntata)
                crediti += vincita
                print(f"Hai vinto! Numero estratto: {numero_estratto} ({colore})")
            else:
                print(f"Hai perso. Numero estratto: {numero_estratto} ({colore})")
        elif verifica_vincita(tipo_giocata, scelta, numero_estratto):
            vincita = calcola_vincita(tipo_giocata, puntata)
            crediti += vincita
            print(f"Hai vinto! Numero estratto: {numero_estratto}")
        else:
            print(f"Hai perso. Numero estratto: {numero_estratto}")

        print(f"Crediti rimanenti: {crediti}")

        if crediti == 0:
            print("Hai finito i crediti. Gioco terminato.")
            break

        if input("Vuoi continuare? (si/no): ").lower() != "si":
            break

    print("Grazie per aver giocato!")

if __name__ == "__main__":
    main()
