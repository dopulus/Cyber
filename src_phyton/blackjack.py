import random

# Mazzo di carte
valori = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

semi = ["♠", "♥", "♦", "♣"]

def crea_mazzo():
    mazzo = []
    for valore in valori:
        for seme in semi:
            mazzo.append((valore, seme))
    random.shuffle(mazzo)
    return mazzo

def calcola_punteggio(mano):
    totale = sum(valori[carta[0]] for carta in mano)
    assi = sum(1 for carta in mano if carta[0] == "A")

    while totale > 21 and assi:
        totale -= 10
        assi -= 1

    return totale

def blackjack_naturale(mano):
    return calcola_punteggio(mano) == 21 and len(mano) == 2

def main(crediti=None):
    if crediti is None:
        crediti = 100

    print(f"Benvenuto al Blackjack! Crediti iniziali: {crediti}")

    while crediti > 0:
        mazzo = crea_mazzo()
        print("\n----------------------")
        print(f"Crediti: {crediti}")

        puntata = int(input("Inserisci la puntata: "))
        if puntata <= 0 or puntata > crediti:
            print("Puntata non valida.")
            continue

        giocatore = [mazzo.pop(), mazzo.pop()]
        banco = [mazzo.pop(), mazzo.pop()]

        print(f"Tua mano: {giocatore}")
        print(f"Carta scoperta del banco: {banco[0]}")

        # Blackjack naturale
        if blackjack_naturale(giocatore):
            if blackjack_naturale(banco):
                print("Pareggio: entrambi Blackjack.")
            else:
                vincita = int(puntata * 1.5)
                print(f"BLACKJACK! Vinci {vincita}")
                crediti += vincita
            continue

        # Turno giocatore
        doppio = False
        while True:
            punteggio = calcola_punteggio(giocatore)
            print(f"Totale: {punteggio}")

            if punteggio > 21:
                print("Hai sballato!")
                crediti -= puntata
                break

            scelta = input("Hit (h), Stai (s), raddoppia (d): ").lower()

            if scelta == "h":
                giocatore.append(mazzo.pop())
                print(f"Nuova carta: {giocatore[-1]}")
            elif scelta == "d" and crediti >= puntata:
                puntata *= 2
                doppio = True
                giocatore.append(mazzo.pop())
                print(f"Doppio! Carta: {giocatore[-1]}")
                break
            else:
                break

        if calcola_punteggio(giocatore) > 21:
            continue

        # Turno banco
        print(f"Mano banco: {banco}")
        while calcola_punteggio(banco) < 17:
            banco.append(mazzo.pop())

        punteggio_g = calcola_punteggio(giocatore)
        punteggio_b = calcola_punteggio(banco)

        print(f"Banco totale: {punteggio_b}")

        if punteggio_b > 21 or punteggio_g > punteggio_b:
            print("Hai vinto!")
            crediti += puntata
        elif punteggio_g < punteggio_b:
            print("Hai perso!")
            crediti -= puntata
        else:
            print("Pareggio!")

    print("Crediti finiti. Fine partita.")

if __name__ == "__main__":
    main()
