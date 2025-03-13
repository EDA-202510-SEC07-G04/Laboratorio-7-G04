
def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def add_first(my_list, element):
    
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else: 
        return False
    
def size(my_list):
    return my_list["size"]
    
def first_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["elements"][0]

def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["elements"][my_list["size"] - 1]


def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def remove_first(my_list):
    if my_list["size"] !=0:
        elemento_borrado = my_list["elements"].pop(0)
        my_list["size"] = my_list["size"] - 1
        return elemento_borrado
    else:
        return None
    
def remove_last(my_list):
    if my_list["size"] !=0:
        elemento_borrado = my_list["elements"].pop(-1)
        my_list["size"] = my_list["size"] - 1
        return elemento_borrado
    else:
        return None
    
def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos ,element)
    my_list["size"] = len(my_list["elements"])
    return my_list

def delete_element(my_list, pos):
    if my_list["size"] !=0:
        if pos >=0 and pos <= len(my_list["elements"]):
            elemento_borrado = my_list["elements"].pop(pos) 
            my_list["size"] = my_list["size"] - 1
            return my_list
    else:
        return None
    
def change_info(my_list, pos, new_info):
    my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos1,pos2):
    my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
    return my_list


def sub_list(my_list, pos, numelem):
    posicion = pos
    contador = 0
    new_list = {"elements":[],"size":0,"type": "ARRAY_LIST"}

    while posicion < len(my_list["elements"]) and contador < numelem:
        new_list["elements"].append(my_list["elements"][posicion])
        posicion +=1
        contador +=1
    
    new_list["size"] = len(new_list["elements"])
    return new_list


def default_sort_criteria(element1, element2):
    
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted
    

def insertion_sort(my_list, sort_crit):
    
    elements = my_list["elements"]
    
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        
        while j >= 0 and sort_crit(key, elements[j]) == True:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
        
    return my_list


def selection_sort(my_list, sort_crit):
    elements = my_list["elements"]
    
    for i in range(len(elements)):
        indice = i
        for j in range(i + 1, len(elements)):
            if sort_crit(elements[j], elements[i]) == -1:
                indice = j
        min_value = delete_element(my_list, indice)
        insert_element(my_list, min_value, i)

    return my_list

def shell_sort(list, sort_crit):
    inc = size(list) // 2
    while inc:
        for i, e in enumerate(sub_list(list,0,size(list))["elements"]):  
            while i >= inc and sort_crit(list[i - inc], e):
                list[i] = list[i - inc]
                i -= inc
            list[i] = e
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list

def quick_sort(my_list, sort_crit):
    
    elements = my_list["elements"]
    
    if len(elements) <= 1:
        return my_list
    
    pivot = elements[0]
    less = [x for x in elements[1:] if sort_crit(x, pivot) == -1]
    equal = [pivot]
    greater = [x for x in elements[1:] if sort_crit(x, pivot) == 1]
    
    sorted_less = quick_sort({"elements": less, "size": len(less)}, sort_crit)
    sorted_greater = quick_sort({"elements": greater, "size": len(greater)}, sort_crit)
    
    sorted_elements = sorted_less["elements"] + equal + sorted_greater["elements"]
    
    return {"elements": sorted_elements, "size": len(sorted_elements)}

def merge_sort(my_list, sort_crit):
    
    n = size(my_list)
    if n > 1:
        mid = (n // 2)
        izq_list = sub_list(my_list, 0, mid)
        der_list = sub_list(my_list, mid, n - mid)

        merge_sort(izq_list, sort_crit)
        merge_sort(der_list, sort_crit)

        i = j = k = 0

        izq_elements = size(izq_list)
        der_elements = size(der_list)

        while (i < izq_elements) and (j < der_elements):
            elem_i = get_element(izq_list, i)
            elem_j = get_element(der_list, j)

            if sort_crit(elem_j, elem_i):   
                change_info(my_list, k, elem_j)
                j += 1
            else:                            
                change_info(my_list, k, elem_i)
                i += 1
            k += 1

        while i < izq_elements:
            change_info(my_list, k, get_element(izq_list, i))
            i += 1
            k += 1

        while j < der_elements:
            change_info(my_list, k, get_element(der_list, j))
            j += 1
            k += 1
    return my_list