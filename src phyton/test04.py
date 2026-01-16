def main():
    costo_totale = 0.0

    domanda = input("Hai dei prodotti da aggiungere? (si/no): ").lower()

    if domanda != "si":
        print("Hai sbagliato a lanciare il programma. Ti consiglierei di farti visitare da qualcuno, te lo dico seriamente.")
        return

    while domanda == "si":
        n = int(input("Quanti prodotti dello stesso tipo vuoi aggiungere? "))
        if n <= 0:
            print("Numero di prodotti non valido. Riprova.")
            continue
        elif n == 1:
            print("Attenzione: stai aggiungendo un solo prodotto.")

        costo = float(input("Inserisci il costo del prodotto: "))
        
        if costo < 0:
            print("Costo non valido. Riprova.")
            continue

        costo_totale += costo * n

        domanda = input("Vuoi aggiungere altri prodotti? (si/no): ").lower()

    print(f"Costo totale: {costo_totale:.2f} €")


if __name__ == "__main__":
    main()
