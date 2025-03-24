
def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def insert_element(my_list, element, pos):
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    nodo = my_list["first"]
    for i in range(pos - 2):
        nodo = nodo["next"]
        nodo["next"] = {
            "info": element,
            "next": nodo["next"]
        }
    return my_list
    
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    
    node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        node["next"] = my_list["first"]
        my_list["first"] = node
    my_list["size"] += 1
    
def add_last(my_list, element):
    
    node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
    my_list["size"] += 1
    
def is_empty(my_list):
    
    return my_list["size"] == 0

def size(my_list):
    
    return my_list["size"]

def first_element(my_list):
    
    return my_list["first"]["info"]

def last_element(my_list):
    
    return my_list["last"]["info"]

def remove_first(my_list):
    
    if my_list["size"] == 0:
        return None
    element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return element

def remove_last(my_list):
    
    if my_list["size"] == 0:
        return None
    element = my_list["last"]["info"]
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        temp = my_list["first"]
        while temp["next"] != my_list["last"]:
            temp = temp["next"]
        temp["next"] = None
        my_list["last"] = temp
    my_list["size"] -= 1
    return element

  

def clear(my_list):
    
    my_list["first"] = None
    my_list["last"] = None
    my_list["size"] = 0


def delete_element(my_list, pos):

    if pos == 0:
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
            
    else:
        node = my_list['first']
        for i in range(pos - 1):
            node = node['next']
        node['next'] = node['next']['next']
        if pos == my_list['size'] - 1:
            my_list['last'] = node
    my_list['size'] -= 1
    
    return my_list


def change_info(my_list, pos, new_info):
    
    first = my_list["first"]
    i = 0
    
    while i < pos:
        first = first["next"]
        i += 1
    first["info"] = new_info
    
    return my_list


def exchange(my_list, pos1, pos2):
    
    if pos1 == pos2:
        return my_list
    n1 = my_list["first"]
    n2 = my_list["first"]
    i = 0
    
    while i < pos1:
        n1 = n1["next"]
        i += 1
    i = 0
    
    while i < pos2:
        n2 = n2["next"]
        i += 1
    info = n1["info"]
    n1["info"] = n2["info"]
    n2["info"] = info
    
    return my_list


def sub_list(my_list, pos, num_elem):
    
    sublst = new_list()
    cont = 0
    while cont < num_elem:
        elem = get_element(my_list, pos)
        add_last(sublst, elem)
        pos += 1
        cont += 1
    return sublst



def default_sort_criteria(element1, element2):
    
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    
    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            minimum = pos1
            pos2 = pos1 + 1
            while (pos2 < n):
                if (sort_crit(get_element(my_list, pos2),(get_element(my_list, minimum)))):
                    minimum = pos2
                pos2 += 1
            if minimum != pos1:
                exchange(my_list, pos1, minimum)
            pos1 += 1
    return my_list
    
def insertion_sort(my_list, sort_crit):

    n = size(my_list)
    if n == 0:
        return my_list

    i = 1
    
    while i < n:
        j = i
        while j > 0 and sort_crit(get_element(my_list, j - 1), get_element(my_list, j)) == 1:
            exchange(my_list, j - 1, j)
            j -= 1
        i += 1
        
    return my_list

def shell_sort(my_list, sort_criteria):

    inc = size(my_list) // 2
    while inc:
        for i in range(inc, size(my_list)):
            temp = get_element(my_list, i)
            j = i
            while j >= inc and sort_criteria(temp, get_element(my_list, j - inc)):
                change_info(my_list, j, get_element(my_list, j - inc))
                j -= inc
            change_info(my_list, j, temp)
        inc = 1 if inc == 2 else inc * 5 // 11


def quick_sort(my_list, sort_crit):
    
    if size(my_list) <= 1:
        return my_list

    pivot = get_element(my_list, 0)
    less, equal, greater = new_list(), new_list(), new_list()
    
    i = 0
    
    while i < size(my_list):
        elem = get_element(my_list, i)
        if sort_crit(elem, pivot) == -1:
            add_last(less, elem)
        elif sort_crit(elem, pivot) == 0:
            add_last(equal, elem)
        else:
            add_last(greater, elem)
        i += 1

    less = quick_sort(less, sort_crit)
    greater = quick_sort(greater, sort_crit)

    result = new_list()
    
    while size(less) > 0:
        add_last(result, remove_first(less))
    while size(equal) > 0:
        add_last(result, remove_first(equal))
    while size(greater) > 0:
        add_last(result, remove_first(greater))

    return result

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