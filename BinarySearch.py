def binary_search_rec(lst: list, key: int, vlevo, vpravo, recursion_level=0):
    recursion_level+=1
    print("Úroveň rekurze: ", recursion_level)
    median = int(((vlevo + vpravo)) / 2)
    print("Hledaná hodnota:", key)
    print("Levý index: ", vlevo, "Index Mediánu:", median, "Pravý index:", vpravo)
    print("Hodnota mediánu:", lst[median], "\n")

    if (key == lst[median]):

        print("Prvek nalezen!")
        print("Index prvku: ", median)
        print("Hodnota prvku: ", lst[median])
        return True

    elif (vlevo == vpravo):
        print(key, " není v seznamu!")
        return False
    else:

        if key < lst[median]:
            binary_search_rec(lst, key, vlevo, median,recursion_level)

        elif key > lst[median]:
            binary_search_rec(lst, key, median+1, vpravo,recursion_level)



pole_cisel = []
for i in range(-999, 1000, 3):
    pole_cisel.append(i)
print(pole_cisel)
k=[-1000,-999,-996,-995,-4,-3,-2,-1,0,1,2,3,555,996,997,998,999,1000,1001]
for j in enumerate(k):
    print("-----------------------------------------")
    l,m=j
    n=binary_search_rec(pole_cisel, m, 0, len(pole_cisel) - 1)
    print(n)
