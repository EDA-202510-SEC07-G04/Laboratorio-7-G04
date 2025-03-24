import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as lt


def new_map(capacity, load_factor, prime=109345121):
    capacity = mf.next_prime(max(capacity, 11))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    
    return {
        "table": [None] * capacity,
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
        map["table"][pos] = me.new_map_entry(key, value)
    else:
        map["table"][pos] = me.new_map_entry(key, value)
        map["size"] += 1
        map["current_factor"] = map["size"] / map["capacity"]
    
    return map


def find_slot(map, key, index):
    for i in range(map["capacity"]):
        pos = (index + i) % map["capacity"]
        entry = map["table"][pos]
        if entry is None or me.get_key(entry) == key:
            return (entry is not None, pos)
    return (False, -1)


def is_available(table, pos):
    return table[pos] is None


def default_compare(key1, key2):
    return key1 == key2


def contains(map, key):
    index = mf.hash_value(map, key)
    occupied, _ = find_slot(map, key, index)
    return occupied


def remove(map, key):
    index = mf.hash_value(map, key)
    occupied, pos = find_slot(map, key, index)
    if occupied:
        map["table"][pos] = None
        map["size"] -= 1
        map["current_factor"] = map["size"] / map["capacity"]


def get(map, key):
    index = mf.hash_value(map, key)
    occupied, pos = find_slot(map, key, index)
    if occupied:
        return me.get_value(map["table"][pos])
    return None


def size(map):
    return map["size"]


def is_empty(map):
    return map["size"] == 0


def key_set(map):
    keys = lt.new_list()
    for entry in map["table"]:
        if entry is not None:
            lt.add_last(keys, me.get_key(entry))
    return keys


def value_set(map):
    values = lt.new_list()
    for entry in map["table"]:
        if entry is not None:
            lt.add_last(values, me.get_value(entry))
    return values


def rehash(map):
    old_table = map["table"]
    new_capacity = mf.next_prime(max(map["capacity"] * 2, 11)) 
    new_map_instance = new_map(new_capacity, map["limit_factor"], map["prime"])
    
    for entry in old_table:
        if entry is not None:
            put(new_map_instance, me.get_key(entry), me.get_value(entry))
    
    return new_map_instance
