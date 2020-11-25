auto = []
while True:
    transito = int(input("Quante auto sono passate oggi? "))
    if transito == 0:
        break
    else:
        auto.append(transito)
somma_auto = sum(auto)
print("Auto transitate: ", somma_auto)
