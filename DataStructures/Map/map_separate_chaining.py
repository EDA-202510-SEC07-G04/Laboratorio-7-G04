from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
import random

def new_map(num_elements, load_factor, prime=109345121):
    
    cap = mf.next_prime(int(num_elements / load_factor))
    
    map = {
        "prime" : prime,
        "capacity" : cap,
        "scale" : 1, #random.randint(1, prime - 1) ,
        "shift": 0, #random.randint(0, prime-1),
        "table": al.new_list(),
        "current_factor" : 0,
        "limit_factor" : load_factor,
        "size" : 0
           }

    for i in range(num_elements):
        al.add_last(map["table"], sl.new_list())
    
    return map
def put(my_map, key, value):
    hash_key = mf.hash_value(my_map, key)
    occupied, pos = find_slot(my_map, key, hash_key)
    bucket = al.get_element(my_map["table"], pos)

    if occupied:
        node = bucket["first"]
        while node is not None:
            if node["info"]["key"] == key:
                node["info"]["value"] = value
                return my_map
            node = node["next"]
    else:
        sl.add_last(bucket, me.new_map_entry(key, value))
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    if my_map["current_factor"] >= my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map

def contains(my_map, key):

    index = mf.hash_value(my_map, key)
    ocuppied, pos = find_slot(my_map, key, index)
    return ocuppied

def get(my_map, key):
    index = mf.hash_value(my_map, key)
    ocuppied, pos = find_slot(my_map, key, index)
    bucket = al.get_element(my_map["table"], pos)
    
    if ocuppied:
        node = bucket["first"]
        while node is not None:
            if node["info"]["key"] == key:
                return me.get_value(node["info"])
            node = node["next"]
    else:
        return None

def remove(my_map, key):
    index = mf.hash_value(my_map, key)
    occupied, pos = find_slot(my_map, key, index)
    bucket = al.get_element(my_map["table"], pos)

    if occupied:
        node = bucket["first"]
        i = 0
        while node is not None:
            if node["info"]["key"] == key:
                sl.delete_element(bucket, i)
                my_map["size"] -= 1
                return my_map
            i += 1

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0
    
def find_slot(map, key, index):
    for i in range(map["capacity"]):
        pos = (index + i) % map["capacity"]
        bucket = al.get_element(map["table"], pos)
        
        if bucket["first"] is None:
            return (False, pos)

        node = bucket["first"]
        while node is not None:
            if node["info"]["key"] == key:
                return (True, pos)
            node = node["next"]

    return (False, -1)

def key_set(my_map):
    
    keys = al.new_list()
    for i in range(my_map["capacity"]):
        bucket = al.get_element(my_map["table"], i)
        node = bucket["first"]
        while node is not None:
            al.add_last(keys, node["info"]["key"])
            node = node["next"]
    return keys

def value_set(my_map):
    
    values = al.new_list()
    for i in range(my_map["capacity"]):
        bucket = al.get_element(my_map["table"], i)
        node = bucket["first"]
        while node is not None:
            al.add_last(values, node["info"]["value"])
            node = node["next"]
    return values

def rehash(my_map):
    
    old_table = my_map["table"]
    new_capacity = mf.next_prime(my_map["capacity"] * 2)
    new_mapp = new_map(new_capacity, my_map["limit_factor"], my_map["prime"])
    
    
    for i in range(my_map["capacity"]):
        bucket = al.get_element(old_table, i)
        node = bucket["first"]
        while node is not None:
            key = me.get_key(node["info"])
            value = me.get_value(node["info"])
            put(new_mapp, key, value)
            node = node["next"]

    return new_mapp
               
def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1



