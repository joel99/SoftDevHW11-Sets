
def union(a,b):
    return [x for x in a] + [x for x in b if x not in a]

def intersection(a, b):
    return [x for x in b if x in a]

def dif(u, a):
    return [x for x in u if x not in a]

def symDif(a,b):
    return dif(union(a,b), intersection(a,b))

def cartProd(a,b):
    return [(x, y) for x in a for y in b]
