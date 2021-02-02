import timeit

class CustomException(Exception):
    def __init__(self,a=""):
        message = a
        super().__init__(message)

def binary_search_rec(lst: list, key: int, left_indent, right_indent, recursion_level :int):
    if recursion_level < 0 or not (isinstance(recursion_level, int)):
        raise CustomException("Úroveň rekurze musí být nezáporné, celé číslo!")

    recursion_level+=1
    print("Úroveň rekurze: ", recursion_level)

    if not isinstance(left_indent, int) or not isinstance(right_indent, int):
        raise CustomException("Vlevo a Vpravo musí  být celé číslo!")
    elif left_indent<0 or right_indent<0:
        raise CustomException("Vlevo a Vpravo musí  být nezáporné číslo!")
    elif right_indent<left_indent:
        raise CustomException("prohozené vlevo a vpravo")
    search_succesfull=False
    median = int(((left_indent + right_indent)) / 2)
    print("Hledaná hodnota:", key)
    print("Levý index: ", left_indent, "Index Mediánu:", median, "Pravý index:", right_indent)
    print("Hodnota mediánu:", lst[median], "\n")

    if (key == lst[median]):
        search_succesfull = True
        target_index=median
        print("Prvek nalezen!")
        print("Index prvku: ", median)
        print("Hodnota prvku: ", lst[median])

        return search_succesfull,target_index

    elif (left_indent == right_indent):
        search_succesfull=False
        print(key, " není v seznamu!")

        return search_succesfull, -1

    else:

        if key < lst[median]:
            search_succesfull2,target_index2= binary_search_rec(lst, key, left_indent, median,recursion_level)

        elif key > lst[median]:
            search_succesfull2,target_index2=search_succesfull,actual_index=binary_search_rec(lst, key, median+1, right_indent,recursion_level)

    return search_succesfull2,target_index2



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

