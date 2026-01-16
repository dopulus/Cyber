import roulette
import poker
import blackjack

def main():
    print("Benvenuto al Casinò di San Cyber!")
    scelta = input("Cosa vuoi giocare: (roulette-poker-blackjack)").lower()
    crediti = int(input("Quanti crediti vuoi? "))
    if scelta == "roulette":
        roulette.main(crediti)
    elif scelta == "poker":
        poker.main(crediti)
    elif scelta == "blackjack":
        blackjack.main(crediti)
    else:
        print("Scelta non valida.")

if __name__ == "__main__":
    main()