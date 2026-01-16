import random

def main():
    tentativi = 0
    n = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Prova a vincere, inserisci un numero tra 1 e 10: "))
        except ValueError:
            print("Devi inserire un numero!")
            continue

        if guess < 1 or guess > 10:
            print("Numero non valido. Riprova.")
            continue

        tentativi += 1 

        if guess == n:
            print("Hai indovinato!")
            print(f"Hai impiegato {tentativi} tentativi.")
            break
        else:
            print("Hai sbagliato.")
            if guess < n:
                print("Consiglio: il numero è più grande.")
            else:
                print("Consiglio: il numero è più piccolo.")

if __name__ == "__main__":
    main()
