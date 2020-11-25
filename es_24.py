Candidato1 = int(input("Voti candidato 1 : "))
Candinato2 = int(input("voti candidato 2 : "))
NomeCandidato1 = str(input("Nome candidato 1 : "))
NomeCandidato2 = str(input("Nome candidato 2 : "))
VotiTOT = Candidato1 + Candinato2
PercentualeVotiCandidato1 = int((Candidato1 * 100) / VotiTOT)
PercentualeVotiCandidato2 = int((Candinato2 * 100) / VotiTOT)
print(NomeCandidato1 + str(" " + str(PercentualeVotiCandidato1)) + str("%"))
print(NomeCandidato2 + str(" " + str(PercentualeVotiCandidato2)) + str("%"))
if PercentualeVotiCandidato1 > PercentualeVotiCandidato2:
    print(NomeCandidato1 + str(" ha vinto!"))
else:
    print(NomeCandidato2 + str(" ha vinto!"))
