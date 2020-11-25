stipendi = []
while True:
    stipendio = int(input("Quant'è lo stipendio? "))
    if stipendio == -1:
        break
    else:
        stipendi.append(stipendio)
totalestipendio = len(stipendi)
sommastipendio = sum(stipendi)
media = sommastipendio/totalestipendio
print("Media stupendi: ", media, "euri.")
