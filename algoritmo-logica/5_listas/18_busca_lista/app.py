l = ["sofa","televisao","radio","ac","poltrona"]

i = 0

item_procurado = input("o que deseja buscar na casa ?")
achou = False

while i < len(l):
    if l[i] == item_procurado:
        print("encontramos um %s "%item_procurado)
        achou = True
    i = i + 1

if achou == False:
    print("nao encontramos um %s "%item_procurado)
