list_elements = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_of_list_elements(lst):
    elem_list_int = list(map(int, lst.split(',')))
    return sum(elem_list_int)

result_list = []
for element in list_elements:
    try:
        result = sum_of_list_elements(element)
        result_list.append(result)
    except ValueError:
        result_list.append("Не можу це зробити")

print('Сума елементів списку:')
print(*result_list, sep=', ')
