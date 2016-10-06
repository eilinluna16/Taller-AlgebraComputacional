# FUNCIONES PRINCIPALES
# Si es entero returna True, si no False.
def isZ(expresion):
    elem = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']
    expr = list(expresion)
    num = 0
    for i in range(len(expr)):
        if expr[i] in elem:
            num += 1
    # Si hay mas de un '-', return False.
    if expr.count('-')>1:
        return False
    # Si no hay elementos diferentes a la lista elem, return True.
    elif len(expr)==num:
        # Si hay un '-', nos aseguramos de que este antes del num. 
        if expr.count('-')==1 and expr.index('-')!=0:
                return False
        return True
    # Si hay elementos diferentes a la lista elem, return True.
    else:
        return False

# Si es decimal returna True, si no False.
def isQ(expresion):
    elem = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.']
    expr = list(expresion)
    num = 0
    for i in range(len(expr)):
        if expr[i] in elem:
                num += 1
    # Si '.' se encuentra al principio o al final, return False.
    if expr[0]=='.'or expr[len(expr)-1]=='.' :
            return False    
    # Si hay mas o ningun '.', return False.
    elif expr.count('.')!=1:
            return False
    elif len(expr)==num:
        # Si hay un '-', nos aseguramos de que esta antes del numero.
        if expr.count('-')==1 and expr.index('-')!=0:
                return False
        return True
    else:
        return False
        
# Si es fraccionario returna True, si no False.
def isF(expresion):
        expr = list(expresion)
        elem = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']
        num = 0
        for i in range(len(expr)):
            if expr[i] in elem:
                num += 1
        # Si '/' se encuentra al principio o al final, return False.
        if expr[0]=='/' or expr[len(expr)-1]=='/' :
            return False
        # Si hay mas o ningun '/', return False.
        elif expr.count('/')!=1:
            return False
        # Si no hay elementos diferentes a la lista elem, return True.
        elif len(expr)==num:
            return True
        # Si hay elementos diferentes a la lista elem, return False.
        else:
            return False