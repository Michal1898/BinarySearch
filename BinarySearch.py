def binary_search_rec(lst: list, key: int, vlevo, vpravo):
    median = int(((vlevo + vpravo)) / 2)
    print("Hledaná hodnota:", key)
    print("Levý index: ", vlevo, "Index Mediánu:", median, "Pravý index:", vpravo)
    print("Hodnota mediánu:", lst[median], "\n")

    if (key == lst[median]):

        print("Prvek nalezen!")
        print("Index prvku: ", median)
        print("Hodnota prvku: ", lst[median])
        return median, lst[median]

    elif (vlevo == vpravo):
        print(key, " není v seznamu")
        return False
    else:

        if key < lst[median]:
            binary_search_rec(lst, key, vlevo, median)

        elif key > lst[median]:
            if vlevo == (vpravo - 1):
                vlevo = vpravo
                binary_search_rec(lst, key, vlevo, vpravo)
            else:
                levy = median
                pravy = vpravo
                binary_search_rec(lst, key, levy, pravy)


pole_cisel = []
for i in range(-6, 19, 3):
    pole_cisel.append(i)
print(pole_cisel)

for j in range(-7, 20):
    print("-----------------------------------------")
    print(j)
    binary_search_rec(pole_cisel, j, 0, len(pole_cisel) - 1)
