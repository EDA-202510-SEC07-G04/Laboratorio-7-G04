
def new_map(num_elements, load_factor, prime=109345121):
    """
    Crea una nueva instancia del mapa
    """
    
    my_map = {
        'prime': prime,
        'load_factor': load_factor,
        'size': 0,
        'num_elements': num_elements,
        'keys': [None] * num_elements,
        'values': [None] * num_elements
    }
    
    return my_map
    

def put(my_map, key, value):
    """
    Inserta un nuevo elemento en el mapa
    """
    
    hash_key = hash(key) % my_map['num_elements']
    index = hash_key
    
    while my_map['keys'][index] is not None:
        index = (index + 1) % my_map['num_elements']
        if index == hash_key:
            return False
        
    my_map['keys'][index] = key
    my_map['values'][index] = value
    my_map['size'] += 1
    
    return True


def contains(my_map, key):
    """
    Verifica si un elemento se encuentra en el mapa
    """
    
    hash_key = hash(key) % my_map['num_elements']
    index = hash_key
    
    while my_map['keys'][index] is not None:
        if my_map['keys'][index] == key:
            return True
        index = (index + 1) % my_map['num_elements']
        if index == hash_key:
            return False
        
    return False


def get(my_map, key):
    """
    Obtiene un elemento del mapa
    """
    
    hash_key = hash(key) % my_map['num_elements']
    index = hash_key
    
    while my_map['keys'][index] is not None:
        if my_map['keys'][index] == key:
            return my_map['values'][index]
        index = (index + 1) % my_map['num_elements']
        if index == hash_key:
            return None
        
    return None


def remove(my_map, key):
    """
    Elimina un elemento del mapa
    """
    
    hash_key = hash(key) % my_map['num_elements']
    index = hash_key
    
    while my_map['keys'][index] is not None:
        if my_map['keys'][index] == key:
            my_map['keys'][index] = None
            my_map['values'][index] = None
            my_map['size'] -= 1
            return True
        index = (index + 1) % my_map['num_elements']
        if index == hash_key:
            return False
        
    return False


def size(my_map):
    """
    Retorna el tamaño del mapa
    """
    
    return my_map['size']

