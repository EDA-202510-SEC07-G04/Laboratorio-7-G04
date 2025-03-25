
import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as lt


def new_map(num_elements, load_factor, prime=109345121, test_mode=False):
    """
    Crea una nueva tabla de hash con direccionamiento abierto usando Linear Probing.
    La capacidad es el siguiente número primo a num_elements / load_factor.
    """
    calculated_capacity = int(num_elements / load_factor)
    capacity = 11 if calculated_capacity <= 11 else mf.next_prime(calculated_capacity)
    
    if test_mode:
        scale, shift = 1, 0
    else:
        scale = random.randint(1, prime - 1)
        shift = random.randint(0, prime - 1)
    
    table = lt.new_list()
    for _ in range(capacity):
        lt.add_last(table, None)
    
    return {
        "table": table,
        "capacity": capacity,
        "prime": prime,
        "scale": scale,
        "shift": shift,
        "size": 0,
        "limit_factor": load_factor,
        "current_factor": 0
    }


def put(map, key, value):
    
    if map["current_factor"] >= map["limit_factor"]:
        map = rehash(map)
    
    index = mf.hash_value(map, key)
    occupied, pos = find_slot(map, key, index)
    
    if occupied:
        lt.change_info(map["table"], pos, me.new_map_entry(key, value))
    else:
        lt.change_info(map["table"], pos, me.new_map_entry(key, value))
        map["size"] += 1
        map["current_factor"] = map["size"] / map["capacity"]
    
    return map


def find_slot(map, key, index):
    
    for i in range(map["capacity"]):
        pos = (index + i) % map["capacity"]
        entry = lt.get_element(map["table"], pos)
        if entry is None or me.get_key(entry) == key:
            return (entry is not None, pos)
    return (False, -1)


def contains(map, key):
    
    index = mf.hash_value(map, key)
    occupied, _ = find_slot(map, key, index)
    return occupied


def remove(map, key):
    
    index = mf.hash_value(map, key)
    occupied, pos = find_slot(map, key, index)
    if occupied:
        lt.change_info(map["table"], pos, None)
        map["size"] -= 1
        map["current_factor"] = map["size"] / map["capacity"]


def get(map, key):
    
    index = mf.hash_value(map, key)
    occupied, pos = find_slot(map, key, index)
    if occupied:
        return me.get_value(lt.get_element(map["table"], pos))
    return None


def size(map):
    
    return map["size"]


def is_empty(map):
    
    return map["size"] == 0


def is_available(table, pos):
    
    return lt.get_element(table, pos) is None


def key_set(map):
    
    keys = lt.new_list()
    for i in range(map["capacity"]):
        entry = lt.get_element(map["table"], i)
        if entry is not None:
            lt.add_last(keys, me.get_key(entry))
    return keys


def value_set(map):
    
    values = lt.new_list()
    for i in range(map["capacity"]):
        entry = lt.get_element(map["table"], i)
        if entry is not None:
            lt.add_last(values, me.get_value(entry))
    return values


def rehash(map):
    
    old_table = map["table"]
    new_capacity = mf.next_prime(map["capacity"] * 2)
    new_map_instance = new_map(new_capacity, map["limit_factor"], map["prime"])
    
    for i in range(map["capacity"]):
        entry = lt.get_element(old_table, i)
        if entry is not None:
            put(new_map_instance, me.get_key(entry), me.get_value(entry))
    
    return new_map_instance
