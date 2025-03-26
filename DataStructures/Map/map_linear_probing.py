
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random as r
from DataStructures.List import array_list as lt


def new_map(num_elements, load_factor, prime = 109345121):
    
    capacity = mf.next_prime(num_elements// load_factor)
    my_map={"prime":prime,
           "capacity": capacity,
           "scale":r.randint(1,prime-1),
           "shift":r.randint(0, prime-1),
           "table":lt.new_list(),
           "current_factor": 0 ,
           "limit_factor": load_factor,
           "size": 0
             }
    
    for i in range(capacity):
        entry = me.new_map_entry(None, None)
        lt.add_last(my_map["table"], entry)
    return my_map


def is_available(table, pos):
   entry = lt.get_element(table, pos)
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
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def put(my_map,key,value):
    hash_value = mf.hash_value(my_map, key)
    ocupied, first_avail = find_slot(my_map, key, hash_value)
    
    if ocupied == True:
        existing_entry = lt.get_element(my_map["table"], first_avail)
        my_map["table"]["elements"][first_avail]["value"]= value
        my_map["table"]["elements"][first_avail]["key"]= key
    else:
        my_map["table"]["elements"][first_avail]["value"]= value
        my_map["table"]["elements"][first_avail]["key"]= key
   
        my_map["size"] += 1
        load_factor = my_map["size"]/ my_map["capacity"]
        my_map["current_factor"] = load_factor

        if  my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    return my_map






def contains (my_map, key):
    hash_value = mf.hash_value(my_map, key)
    pos = find_slot(my_map,key,hash_value)
    return pos[0]



def get(my_map, key):
    
    hash_value = mf.hash_value(my_map,key)
    pos = find_slot(my_map,key,hash_value)
    if pos[0]:
        entry = lt.get_element(my_map["table"],pos[1])
        return me.get_value(entry)
    return None
    
    
    
        
def remove(my_map, key):
    
    hash_value= mf.hash_value(my_map,key)
    pos = find_slot(my_map,key, hash_value)

    if pos[0]:
        entry = lt.get_element(my_map["table"],pos[1])
        me.set_value(entry, None)
        me.set_key(entry,"_EMPTY_")
        my_map["size"] -= 1
    return my_map


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    if my_map["size"] == 0:
        return True
    else:
        return False


def key_set(my_map):
    respuesta = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "_EMPTY_":
            lt.add_first(respuesta, key)
    
    return respuesta

def value_set(my_map):
    respuesta = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"], i)
        value = me.get_value(entry)
        if value is not None and value != "_EMPTY_":
            lt.add_last(respuesta, value)
     
    return respuesta

def rehash(my_map):
    
    new_capacity = mf.next_prime(my_map["capacity"]*2)
    new_table = {"size":new_capacity,"elements":[]}
    
    for i in range(new_capacity):
        new_entry = me.new_map_entry(None,None)
        lt.add_last(new_table,new_entry)

    for entry in my_map["table"]["elements"]:
        if me.get_key(entry) is not None and me.get_key(entry) != "_EMPTY_":
            hash_value = mf.hash_value(my_map,me.get_key(entry))
            pos = find_slot(my_map,me.get_key(entry),hash_value)
            new_table["elements"][pos[1]] = entry

    my_map["table"] = new_table
    my_map["capacity"] = new_capacity

    return my_map