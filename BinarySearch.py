import timeit

class CustomException(Exception):
    def __init__(self,a=""):
        message = a
        super().__init__(message)

def binary_search_rec(lst: list, key: int, vlevo, vpravo, recursion_level :int):
    if recursion_level < 0 or not (isinstance(recursion_level, int)):
        raise CustomException("Úroveň rekurze musí být nezáporné, celé číslo!")

    recursion_level+=1
    print("Úroveň rekurze: ", recursion_level)

    if not isinstance(vlevo, int) or not isinstance(vpravo, int):
        raise CustomException("Vlevo a Vpravo musí  být celé číslo!")
    elif vlevo<0 or vpravo<0:
        raise CustomException("Vlevo a Vpravo musí  být nezáporné číslo!")
    elif vpravo<vlevo:
        raise CustomException("prohozené vlevo a vpravo")
    search_succesfull=False
    median = int(((vlevo + vpravo)) / 2)
    print("Hledaná hodnota:", key)
    print("Levý index: ", vlevo, "Index Mediánu:", median, "Pravý index:", vpravo)
    print("Hodnota mediánu:", lst[median], "\n")

    if (key == lst[median]):
        search_succesfull = True
        print("Prvek nalezen!")
        print("Index prvku: ", median)
        print("Hodnota prvku: ", lst[median])

    elif (vlevo == vpravo):
        search_succesfull=False
        print(key, " není v seznamu!")

    else:

        if key < lst[median]:
            search_succesfull,actual_index= binary_search_rec(lst, key, vlevo, median,recursion_level)

        elif key > lst[median]:
            search_succesfull,actual_index=binary_search_rec(lst, key, median+1, vpravo,recursion_level)

    if search_succesfull:
        return search_succesfull, median
    else:
        return search_succesfull, -1



pole_cisel = []
for i in range(-999, 1000, 3):
    pole_cisel.append(i)
print(pole_cisel)
k=[-1000,-999,-996,-995,-4,-3,-2,-1,0,1,2,3,555,996,997,998,999,1000,1001]

for j in enumerate(k):
    print("-----------------------------------------")
    l,m=j
    start = timeit.timeit()
    element_found,final_index=binary_search_rec(pole_cisel, m, 0, len(pole_cisel) - 1,0)
    end = timeit.timeit()
    print("Doba trvani hledaní: ",end-start)
    if element_found:
        print("Číslo ",m ," je na prvek s indexem:", final_index)
    else:
        print("Číslo ",m ," není v poli čísel!", final_index)

