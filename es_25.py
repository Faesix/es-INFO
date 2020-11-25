nomi = []
punti = []
candidato1 = input("Nome del primo candidato: ").upper()
punteggio1 = int(input("Punteggio del primo candidato: "))
nomi.append(candidato1)
punti.append(punteggio1)
candidato2 = input("Nome del secondo candidato: ").upper()
punteggio2 = int(input("Punteggio del secondo candidato: "))
nomi.append(candidato2)
punti.append(punteggio2)
print("Ordine alfacandidato2etico: ")
nomi.sort()
print(nomi)
input("ENTER X l'ordine decrescente")
print("Ordine decrescente: ")
if punteggio1>punteggio2:
    print(punteggio2, punteggio1)
else:
    print(punteggio1, punteggio2)
