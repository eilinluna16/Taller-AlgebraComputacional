from Fraccion import Fraccionario
from Decimal import Decimal
from FuncionesPrincipales import isQ, isZ, isF

################# CONVERSIONES #####################    
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
        
def isEntero(expr):
    # Si Fraccion es convertible a entero returna True, sino False.
    if isF(expr)==True:
        expr = Fraccionario(expr)
        if expr.num % expr.den == 0:
            return True
        else:
            return False

##########################################################
################### OPERACIONES ENTRE FRACCIONES #########
# Fraccionario mas Fraccionario
def FmasF(A, B):
    A = Fraccionario(A)
    B = Fraccionario(B)
    num = A.num*B.den + A.den*B.num
    den = A.den*B.den
    return Fraccionario(str(num)+'/'+str(den)).simp() 
# Fraccionario por Fraccionario
def FporF(A, B):
    A = Fraccionario(A)
    B = Fraccionario(B)
    num = A.num*B.num
    den = A.den*B.den
    return Fraccionario(str(num)+'/'+str(den)).simp() 
# Fraccionario entre Fraccionario
def FentreF(A, B):
    A = Fraccionario(A)
    B = Fraccionario(B)
    num = A.num*B.den
    den = A.den*B.num
    return Fraccionario(str(num)+'/'+str(den)).simp() 
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
    A = Fraccionario(A)
    B = Fraccionario(B).simp()
    if isEntero(B)==True:
        B = Fraccionario(B)
        return FalaZ(A, int(B.num)/int(B.den))
    # Se tiene en cuenta si hay raiz cuadrada
    elif B == '1/2':        
        num = A.num ** 0.5
        den = A.den ** 0.5
        if isZ(str(num))==True and isZ(str(den))==True:
            return str(num)+'/'+str(den)
        else:
            A = A.simp()
            return A+'**'+B
    else:
        A = A.simp()
        return A+'**'+B

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
        if isF(self.expr)==False:
            self.expr = toFraccion(self.expr)
        if isF(other)==False:
            other = toFraccion(other)
        return FmasF(self.expr, other)
        
   def __sub__(self, other):
        if isF(self.expr)==False:
            self.expr = toFraccion(self.expr)
        if isF(other)==False:
            other = toFraccion(other)
        return FmasF(self.expr, '-'+other)
    
   def __mul__(self, other):
        if isF(self.expr)==False:
            self.expr = toFraccion(self.expr)
        if isF(other)==False:
            other = toFraccion(other)
        return FporF(self.expr, other)
                
   def __div__(self, other):
        if isF(self.expr)==False:
            self.expr = toFraccion(self.expr)
        if isF(other)==False:
            other = toFraccion(other)
        return FentreF(self.expr, other)
    
   def __pow__(self, other):
        if isF(self.expr)==False:
            self.expr = toFraccion(self.expr)
        # Si el exponente es entero
        if isZ(other)==True:
            return FalaZ(self.expr, other)
        # Si el exponente es decimal
        if isQ(other)==True:
            res = FalaQ(self.expr, other)
            if isEntero(res):
                return res
            else:
                Fraccionario(self.expr).simp()
                Decimal(other).simp()
                return '('+self.expr+')**'+other
        # Si el exponente es fraccionario
        if isF(other)==True:
            return FalaF(self.expr, other)