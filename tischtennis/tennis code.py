import random
import time # Zeitverzögerung bei der Ausgabe (optional)


# Turnierergebnisse absteigend speichern
def speichern(file, woerterbuch):
    with open(file, "w", encoding="utf-8") as f:
        for name, points in sorted(woerterbuch.items(), key=lambda s: s[1], reverse=True):
            f.write(f"{name}, {points}\n")


eingabedaten = 2 # Eingabebestätigung (1 = korrekt)

# Spieleranzahl und Namen eingeben, bei Bestätigung Schleife beenden
while eingabedaten != 1:
    spieler_anzahl = None
    print("Bitte geben Sie eine ganze Zahl ein.")
    while type(spieler_anzahl) != int:
        try:
            spieler_anzahl = int(input())
        except ValueError:
            print("Falsche Eingabe")

    print("Danke!")
    print("\n-------------------\n")

    spielers_list = []

    for i in range(spieler_anzahl):
        print("Bitte geben Sie den Namen des Spielers ein")
        spielers_list.append(input())

    print("\n-------------------\n")

    print(f"Erledigt!\nInsgesamt {len(spielers_list)} Spieler\nNamen aller Spieler:")

    for x in spielers_list:
        time.sleep(0.2)
        print("-" + x)

    print("\n-------------------\n")
    print("Bitte prüfen Sie, ob alle Namen korrekt eingegeben wurden:")
    print("- 1 - Ja, alles ist korrekt")
    print("- 2 - Nein, müssen die Daten erneut eingeben")

    while True:
        try:
            eingabedaten = int(input("Eingabe:"))
            if eingabedaten == 1 or eingabedaten == 2:
                break
            print("Bitte fuhren Sie nur 1 oder 2 ein!")
        except ValueError:
            print("Bitte fuhren Sie nur 1 oder 2 ein!")

print("\n-------------------\n")
time.sleep(1)
print("Ausgezeichnet! Die Spielerliste wurde bestätigt.")
time.sleep(1)




pairs = [] # Alle Spielerpaare erstellen
for i in range(len(spielers_list)):
    for j in range(i+1, len(spielers_list)):
        pairs.append([spielers_list[i], spielers_list[j]])

random.shuffle(pairs) # Spielreihenfolge zufällig mischen

# Spielplan ausgeben
print ("Der Spielplan und die teilnehmenden Paare:\n")
for i in range(len(pairs)):
    time.sleep(0.5)
    print (f"Spiel {i+1}:")
    print (pairs[i][0], "und", pairs[i][1], "\n")

print("\n-------------------\n")

print("Das Turnier beginnt!")

print("\n-------------------\n")

results = {name: 0 for name in spielers_list} # Punktestand initialisieren (alle = 0)


# Spiele durchführen, Sieger bekommt 3 Punkte
for i in range(len(pairs)):
    print(f"Spiel {i+1}:")
    print("\nUnd gewinnt das Spiel...")
    print(f"    1 - {pairs[i][0]}")
    print(f"    2 - {pairs[i][1]}")
    auswahl = 0
    while True:
        try:
            auswahl = int(input("Eingabe:"))
            if auswahl == 1 or auswahl == 2:
                break
            print("Bitte fuhren Sie nur 1 oder 2 ein!")
        except ValueError:
            print("Bitte fuhren Sie nur 1 oder 2 ein!")
    results[pairs[i][auswahl-1]] += 3
    print("\n-------------------\n")

time.sleep(1)
print("Das Turnier ist beendet!\n")
time.sleep(2)
print("Turnierergebnisse:\n")
time.sleep(1)

# Ergebnisse absteigend ausgeben
nummer = 0 # Platznummer
last_result = 0 # Vergleich, gleiche Punktzahl = gleicher Platz
for key, value in sorted(results.items(), key = lambda s: s[1], reverse = True):
    if value != last_result:
        nummer += 1
    time.sleep(0.7)
    print (f"Platz {nummer}:")
    print (f"{key}: {value} Punkte\n")

    last_result = value

print("\n-------------------\n")

# Ergebnisse in Datei speichern, schreiben ohne .txt
print("Turnierergebnisse speichern:")
filename = str(input("Gib dem Turnier einen Namen: ")+".txt")
speichern(filename, results)
print (f"Turnierergebnisse wurde gespeichert als {filename}")
