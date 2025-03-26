
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random as random
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime = 109345121):
    
    cap = mf.next_prime(num_elements / load_factor)
    my_map = {
        "prime":prime,
        "capacity": cap,
        "scale":random.randint(1 , prime - 1),
        "shift":random.randint(0, prime - 1),
        "table":al.new_list(),
        "current_factor": 0 ,
        "limit_factor": load_factor,
        "size": 0
        }
    
    for i in range(cap):
        entry = me.new_map_entry(None, None)
        al.add_last(my_map["table"], entry)
    return my_map


def is_available(table, pos):
    
    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "_EMPTY_":
        return True
    return False

def default_compare(key, entry):

    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1


def find_slot(my_map, key, hash_value):
    
    first_avail = None
    found = False
    ocupied = False
    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
        hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail


def put(my_map,key,value):
    hash_value = mf.hash_value(my_map, key)
    ocupied, pos = find_slot(my_map, key, hash_value)
    
    if ocupied == True:
        al.change_info(my_map["table"], pos, me.new_map_entry(key, value))
    else:
        al.change_info(my_map["table"], pos, me.new_map_entry(key, value))
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"]/ my_map["capacity"]

    if  my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)
    return my_map


def contains (my_map, key):
    hash_value = mf.hash_value(my_map , key)
    occupied, pos = find_slot(my_map , key , hash_value)
    return occupied

def get(my_map, key):
    
    hash_value = mf.hash_value(my_map , key)
    occupied, pos = find_slot(my_map , key , hash_value)
    if occupied:
        entry = al.get_element(my_map["table"],pos)
        return me.get_value(entry)
    return None
    
def remove(my_map, key):
    
    hash_value= mf.hash_value(my_map,key)
    occupied, pos = find_slot(my_map,key, hash_value)

    if occupied:
        entry = al.get_element(my_map["table"],pos)
        me.set_value(entry, None)
        me.set_key(entry,"_EMPTY_")
        my_map["size"] -= 1
    return my_map


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    
    return my_map["size"] == 0

def key_set(my_map):
    
    lista = al.new_list()
    for i in range(al.size(my_map["table"])):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "_EMPTY_":
            al.add_first(lista, key)
    
    return lista

def value_set(my_map):
    
    lista = al.new_list()
    for i in range(al.size(my_map["table"])):
        entry = al.get_element(my_map["table"], i)
        value = me.get_value(entry)
        if value is not None and value != "_EMPTY_":
            al.add_last(lista, value)
     
    return lista

def rehash(my_map):
    
    new_capacity = mf.next_prime(my_map["capacity"]*2)
    new_table = {"size":new_capacity,"elements":[]}
    
    for i in range(new_capacity):
        new_entry = me.new_map_entry(None,None)
        al.add_last(new_table,new_entry)

    for entry in my_map["table"]["elements"]:
        if me.get_key(entry) is not None and me.get_key(entry) != "_EMPTY_":
            hash_value = mf.hash_value(my_map, me.get_key(entry))
            occupied, pos = find_slot(my_map, me.get_key(entry), hash_value)
            new_table["elements"][pos] = entry

    my_map["table"] = new_table
    my_map["capacity"] = new_capacity

    return my_map