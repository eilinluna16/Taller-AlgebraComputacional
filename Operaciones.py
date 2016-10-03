from Entero import Entero
from Fraccion import Fraccionario
from Decimal import Decimal
from FuncionesPrincipales import isQ, isZ, isF

################# CONVERSIONES #####################
def isEntero(expr):
    # Ingresa expresion decimal o fraccionaria.
    # Si es convertible a entero returna True, sino False.
    if isF(expr)==True:
        expr = Fraccionario(expr)
        if expr.num % expr.den == 0:
            return True
        else:
            return False
    if isQ(expr)==True:
            D = Decimal(expr)
            if D.dec == 0:
                return True
            else:
                return False 

def toDecimal(expr):
    # Ingresa expresion entera.
    # Returna expresion decimal.
        return expr+'.0'
          
def toEntero(expr):
    # Ingresa expresion decimal.
    # Returna expresion entera.
    if isEntero(expr) == True:
       D = Decimal(expr)
       return D.ent
    
def toFraccion(expr):
    # Ingresa expresion decimal o entera.
    # Returna expresion fraccionaria.
    if isQ(expr)==True:
        expr = Decimal(expr)
        num = int(expr.d*10**len(expr.P_d))
        den = 10**len(expr.P_d)
        return Fraccionario(str(num)+'/'+str(den)).simp()
    if isZ(expr)==True:
        return Fraccionario(expr+'/1').simp()

def convierte(expr):
    expr = Fraccionario(expr)
    if isEntero(expr) == True:
        return str(expr.num/expr.den)
    else:
        return str(expr.num/float(expr.den))                
############################################################# 
################# OPERACIONES MATEMATICAS ###################
#############################################################

   
######################### SUMA ##############################
# Entero mas entero
def ZmasZ(A, B):
    A = Entero(A)
    B = Entero(B)
    return A.e+B.e
# Decimal mas Decimal
def QmasQ(A, B):
    A = Decimal(A)
    B = Decimal(B)
    return Decimal(str(A.d+B.d)).simp()
# Fraccionario mas Fraccionario
def FmasF(A, B):
    A = Fraccionario(A)
    B = Fraccionario(B)
    num = A.num*B.den + A.den*B.num
    den = A.den*B.den
    return Fraccionario(str(num)+'/'+str(den)).simp() 
# Entero mas decimal
def ZmasQ(A, B):
    A = Decimal(toDecimal(A))
    B = Decimal(B)
    return QmasQ(A, B)
# Entero mas Fraccionario
def ZmasF(A, B):
    A = Fraccionario(toFraccion(A))
    B = Fraccionario(B)
    return FmasF(A, B)
# Decimal mas Fraccionario
def QmasF(A, B):
        A = Fraccionario(toFraccion(A))
        B = Fraccionario(B)
        return FmasF(A, B)
        
####################### MULTIPLICACION ################################
# Entero por entero
def ZporZ(A, B):
    A = Entero(A)
    B = Entero(B)
    return A.e*B.e
# Decimal por Decimal
def QporQ(A, B):
    A = Decimal(A)
    B = Decimal(B)
    resp = list(str(int(A.d*10**len(A.P_d)*int(B.d*10**len(B.P_d)))))
    while len(A.P_d)+len(A.P_d)>len(resp):
        resp.insert(0,'0')
    resp.insert(-(len(A.P_d)+len(B.P_d)),'.')
    resp.insert(0,'0')
    return Decimal(''.join(resp)).simp()
# Fraccionario por Fraccionario
def FporF(A, B):
    A = Fraccionario(A)
    B = Fraccionario(B)
    num = A.num*B.num
    den = A.den*B.den
    return Fraccionario(str(num)+'/'+str(den)).simp() 
# Entero por Decimal
def ZporQ(A, B):
    A = Decimal(toDecimal(A))
    B = Decimal(B)
    return QporQ(A,B)
# Entero por Fraccionario
def ZporF(A, B):
    A = Fraccionario(toFraccion(A))
    B = Fraccionario(B)
    return FporF(A, B)
# Decimal por Fraccionario
def QporF(A, B):
    A = Fraccionario(toFraccion(A))
    B = Fraccionario(B)
    return FporF(A, B)

####################### DIVISION #######################
# Decimal entre Decimal
def QentreQ(A, B):
    A = Decimal(A)
    B = Decimal(B)
    if len(A.P_d)>=len(B.P_d):
        num = int(A.d*10**len(A.P_d))
        den = int(B.d*10**len(A.P_d))
        return Fraccionario(str(num)+'/'+str(den)).simp()
    else:
        num = int(A.d*10**len(B.P_d))
        den = int(B.d*10**len(B.P_d))
        return Fraccionario(str(num)+'/'+str(den)).simp()
# Fraccionario entre Fraccionario
def FentreF(A, B):
    A = Fraccionario(A)
    B = Fraccionario(B)
    num = A.num*B.den
    den = B.den*A.den
    return Fraccionario(str(num)+'/'+str(den)).simp() 
# Entero entre Decimal
def ZentreQ(A, B):
    A = Decimal(toDecimal(A))
    B = Decimal(B)
    return QentreQ(A,B)
# Entero entre Fraccionario
def ZentreF(A, B):
    A = Fraccionario(toFraccion(A))
    B = Fraccionario(B)
    return FentreF(A, B)
# Decimal entre Entero
def QentreZ(A, B):
    A = Decimal(A)
    B = Decimal(toDecimal(A))
    return QentreQ(A,B)
# Decimal entre Fraccionario
def QentreF(A, B):
    A = Fraccionario(toFraccion(A))
    B = Fraccionario(B)
    return FentreF(A, B)
# Fraccionario entre entero
def FentreZ(A, B):
    A = Fraccionario(A)
    B = Fraccionario(toFraccion(B))
    return FentreF(A,B)
# Fraccionario entre decimal
def FentreQ(A, B):
    A = Fraccionario(A)
    B = Fraccionario(toFraccion(B))
    return FentreF(A,B)

####################### POTENCIACION #######################
# Entero a la entero
def ZalaZ(A, B):
    A = Entero(A)
    B = Entero(B)
    return A.e**B.e
# Entero a la decimal
def ZalaQ(A, B):
    A = Entero(A)
    B = Decimal(B)
    res = str(A.e**B.d)
    if isEntero(res)==True:
        return res.toEntero()
    else:
        return str(A)+'**'+str(B)
# Entero a la Fraccionario
def ZalaF(A, B):
    if isEntero(B)==True:
        return ZalaZ(A, convierte(B))
    else:
        return ZalaQ(A, convierte(B))
# Decimal a la decimal
def QalaQ(A, B):
    return A+'**'+B
# Decimal a la Entero.
def QalaZ(A, B):
    A = Decimal(A)
    return str(A.d**int(B))
# Decimal a la Fraccionario
def QalaF(A, B):
    if isEntero(B)==True:
        return QalaZ(A, convierte(B))
    else:
        return QalaQ(A, convierte(B))
#Fraccionario a la Entero
def FalaZ(A, B):
    A = Fraccionario(A)
    B = int(B)
    if B>0:
        num = A.num ** B
        den = A.den ** B
    else:
        num = A.den ** (B*-1)
        den = A.num ** (B*-1)
    return Fraccionario(str(num)+'/'+str(den)).simp()
#Fraccionario a la decimal
def FalaQ(A, B):
    A = Fraccionario(A)
    B = Decimal(B)
    if B.d>=0:
        num = A.num**B.d
        den = A.den**B.d
    else:
        num = A.den**(B.d*-1)
        den = A.num**(B.d*-1)
    return toFraccion(str(num/den))
    
# Fraccionario a la Fraccionario
def FalaF(A, B):
    if isEntero(B)==True:
        return FalaZ(convierte(B))
    else:
        return FalaQ(convierte(B))
    
#########################################################
#########################################################
#########################################################
class Operando:
    def __init__(self, expr):
        self.expr = expr
        
    def __str__(self, expr):
        return str(self.expr)
           
    # SUMA       
    def __add__(self, other):
        if isZ(self.expr)==True:
            if isZ(other)==True:
                return ZmasZ(self.expr, other)
            if isQ(other)==True:
                return ZmasQ(self.expr, other)
            if isF(other)==True:
                return ZmasF(self.expr, other)
        if isQ(self.expr)==True:
            if isZ(other)==True:
                return other.ZmasQ(self.expr)
            if isQ(other)==True:
                return QmasQ(self.expr, other)
            if isF(other)==True:
                return QmasF(self.expr, other)
        if isF(self.expr)==True:
            if isZ(other)==True:
                return ZmasF(other, self.expr)
            if isQ(other)==True:
                return QmasF(other, self.expr)
            if isF(other)==True:
                return FmasF(self.expr, other)
                
    def __sub__(self, other):
        if isZ(self.expr)==True:
            if isZ(other)==True:
                return ZmasZ(self.expr, '-'+other)
            if isQ(other)==True:
                return ZmasQ(self.expr, '-'+other)
            if isF(other)==True:
                return ZmasF(self.expr, '-'+other)
        if isQ(self.expr)==True:
            if isZ(other)==True:
                return ZmasQ(other, '-'+self.expr)
            if isQ(other)==True:
                return QmasQ(self.expr, '-'+other)
            if isF(other)==True:
                return QmasF(self.expr, '-'+other)
        if isF(self.expr)==True:
            if isZ(other)==True:
                return ZmasF(other, '-'+self.expr)
            if isQ(other)==True:
                return QmasF(other, '-'+self.expr)
            if isF(other)==True:
                return FmasF(self.expr, '-'+other)
    
    def __mul__(self, other):
        if isZ(self.expr)==True:
            if isZ(other)==True:
                return ZporZ(self.expr, other)
            if isQ(other)==True:
                return ZporQ(self.expr, other)
            if isF(other)==True:
                return ZporF(self.expr, other)
        if isQ(self.expr)==True:
            if isZ(other)==True:
                return ZporQ(other, self.expr)
            if isQ(other)==True:
                return QporQ(self.expr, other)
            if isF(other)==True:
                return QporF(self.expr, other)
        if isF(self.expr)==True:
            if isZ(other)==True:
                return ZporF(other, self.expr)
            if isQ(other)==True:
                return QporF(other, self.expr)
            if isF(other)==True:
                return FporF(self.expr, other)
                
    def __div__(self, other):
        if isZ(self.expr)==True:
            if isQ(other)==True:
                return ZentreQ(self.expr, other)
            if isF(other)==True:
                return ZentreF(self.expr, other)
        if isQ(self.expr)==True:
            if isZ(other)==True:
                return QentreZ(self.expr, other)
            if isQ(other)==True:
                return QentreQ(self.expr, other)
            if isF(other)==True:
                return QentreF(self.expr, other)
        if isF(self.expr)==True:
            if isZ(other)==True:
                return FentreZ(self.expr, other)
            if isQ(other)==True:
                return FentreQ(self.expr, other)
            if isF(other)==True:
                return FentreF(self.expr, other)
    
    def __pow__(self, other):
        if isZ(self.expr)==True:
            if isZ(other)==True:
                return ZalaZ(self.expr, other)
            if isQ(other)==True:
                return ZalaQ(self.expr, other)
            if isF(other)==True:
                return ZalaF(self.expr, other)
        if isQ(self.expr)==True:
            if isZ(other)==True:
                return QalaZ(self.expr, other)
            if isQ(other)==True:
                return QalaQ(self.expr, other)
            if isF(other)==True:
                return QalaF(self.expr, other)
        if isF(self.expr)==True:
            if isZ(other)==True:
                return FalaZ(self.expr, other)
            if isQ(other)==True:
                return FalaQ(self.expr, other)
            if isF(other)==True:
                return FalaF(self.expr, other)