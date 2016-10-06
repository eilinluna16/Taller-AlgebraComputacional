from Operaciones import Operando
from Fraccion import Fraccionario
from FuncionesPrincipales import isQ, isF

class Expresion:
    def __init__(self, expr):
        self.expr = expr
  
    def __str__(self):
        return str(self.expr)
        
    # Eliminando vacios
    def ElimVacios(self, lista):
        # Eliminando ' '
        x = lista.count(' ')
        while x>0:
            lista.pop(lista.index(' '))
            x = lista.count(' ') 
        # Eliminando []
        y = lista.count([])
        while y>0:
            lista.pop(lista.index([]))
            y = lista.count([]) 
        # Eliminando ''
        z = lista.count('')
        while z>0:
            lista.pop(lista.index(''))
            z = lista.count('')
        return lista
        
    # Funcion que identifica los numeros de una expresion.
    def Numero(self):
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if type(self.expr)==list:
            expr = self.expr
            self.expr.append(' ')
            self.expr.insert(0, ' ')  
        else:
            expr = list(self.expr)
            expr.append(' ')
            expr.insert(0, ' ')        
        lista = []
        pos = 0
        for i in range(len(expr)):
            if expr[i] not in num:
                lista += [expr[pos+1:i],expr[i]]
                pos = i 
        # Convirtiendoo lista de numeros a string.
        for j in range(len(lista)):
            if type(lista[j])==list:
                lista[j]= ''.join(lista[j])
        self.ElimVacios(lista)
        return lista
        
    # Si hay decimales return True, sino False.
    def HayDecimal(self):
        lista = self.Numero()
        for i in range(len(lista)):
            if lista[i]=='.':
                return isQ(''.join(lista[i-1:i+2]))
        if '.' not in lista: return False
    
    # Funcion que identifica los decimales de una expresion            
    def Decimal(self):
        lista = self.Numero()
        for i in range(len(lista)):
            if lista[i]=='.' and isQ(''.join(lista[i-1:i+2]))==True:
                lista[i] = ''.join(lista[i-1:i+2])
                lista[i-1], lista[i+1] = '', ''
        self.ElimVacios(lista)
        
        # Si hay puntos, que no expresan un decimal, returna Error.
        if '.' in lista: raise TypeError("Error decimal")
        else: return lista
    
    # Si hay fraccionarios return True, sino False.
    def HayFraccion(self):
        lista = self.Numero()
        for i in range(len(lista)):
            if lista[i]=='/':
                return isF(''.join(lista[i-1:i+2]))
        if '/' not in lista: return False
            
    # Funcion que identifica los fraccionarios de una expresion            
    def Fraccion(self):
        lista = self.Numero()
        for i in range(len(lista)):
            if lista[i]=='/' and isF(''.join(lista[i-1:i+2]))==True:
                lista[i] = ''.join(lista[i-1:i+2])
                lista[i-1], lista[i+1] = '', ''
        self.ElimVacios(lista)
        
        return lista
        
    # Si hay '**' returna True, sino, False
    def HayPotencia(self):
        lista = self.Numero()
        for i in range(len(lista)):
            if lista[i]=='*' and lista[i+1]=='*':
                return True
        if '*' not in lista: return False
    
    # Resuelve las potencias.
    def Potencia(self):
        lista = self.Numero()
        for i in range(len(lista)):
            if lista[i]=='*' and lista[i+1]=='*':
                if lista[i+2]=='-':
                    lista[i+2]=''.join(lista[i+2:i+4])
                    lista[i+3]=''    
                lista[i] = str(Operando(lista[i-1])**lista[i+2])
                lista[i-1] = ''
                lista[i+1] = ''
                lista[i+2] = ''
        self.ElimVacios(lista)   
        return lista
        
    # Si hay '*' returna True
    def HayMultiplicacion(self):
        lista = self.Numero()
        if '*' in lista:           
            return True
        else:
            return False
    
    # Resuelve multiplicacion
    def Mult(self):
        lista = self.Numero()
        for i in range(lista.count('*')):
            j = lista.index('*')
            if lista[j+1]=='-':
                lista[j+1]=''.join(lista[i+1:i+3])
                lista[j+2]=''
            lista[j] = str(Operando(lista[j-1])*lista[j+1])
            lista[j-1]=''
            lista[j+1]=''
            self.ElimVacios(lista)   
        return lista
        
    # Si hay '+' returna True
    def HaySuma(self):
        lista = self.Numero()
        if '+' in lista:           
            return True
        else:
            return False
    # Resuelve suma
    def Suma(self):
        lista = self.Numero()
        for i in range(lista.count('+')):
            j = lista.index('+')
            if lista[j+1]=='-':
                lista[j+1]=''.join(lista[i+1:i+3])
                lista[j+2]=''
            lista[j] = str(Operando(lista[j-1])+lista[j+1])
            lista[j-1]=''
            lista[j+1]=''
            self.ElimVacios(lista)
        return lista
        
    def HayResta(self):
        lista = self.Numero()
        if '-' in lista:           
            return True
        else:
            return False
    # Resuelve suma
    def Resta(self):
        lista = self.Numero()
        for i in range(lista.count('-')):
            j = lista.index('-')
            if j!=0:
                if lista[j-1]=='-':
                    lista[j+1]=''.join(lista[i+1:i+3])
                    lista[j+2]=''
                lista[j] = str(Operando(lista[j-1])+lista[j+1])
                lista[j-1]=''
                lista[j+1]=''
            self.ElimVacios(lista)
        return lista
    
    # Si hay '/' returna True
    def HayDivision(self):
        lista = self.Numero()
        if '/' in lista:           
            return True
        else:
            return False
            
    def Division(self):
        lista = self.Numero()
        for i in range(lista.count('/')):
            j = lista.index('/')
            if j!=0:
                if lista[j-1]=='-':
                    lista[j+1]=''.join(lista[i+1:i+3])
                    lista[j+2]=''
                lista[j] = str(Operando(lista[j-1])/lista[j+1])
                lista[j-1]=''
                lista[j+1]=''
            self.ElimVacios(lista)
        return lista
        
    def simplify(self):
        lista = Expresion(self.Numero())
        if lista.HayDecimal() == True:
            lista = Expresion(lista.Decimal())
        if lista.HayFraccion() == True:
            lista = Expresion(lista.Fraccion())
        if lista.HayPotencia() == True:
            lista = Expresion(lista.Potencia())
        if lista.HayMultiplicacion() == True:
            lista = Expresion(lista.Mult())
        if lista.HaySuma() == True:
            lista = Expresion(lista.Suma())
        if lista.HayResta() == True:
            lista = Expresion(lista.Resta())  
        if lista.HayDivision() == True:
            lista = Expresion(lista.Division())  
        return lista
            
def simplify(Expr): 
   def ElimVac(Expr):
       Expr=list(Expr)
       lista = ['[', "'", ' ', ',', ']']
       for i in range(5):
           A = lista[i] in Expr
           while A == True:
               Expr.remove(lista[i])
               A = lista[i] in Expr
       return ''.join(Expr)
   
   A = list(Expr)
   if '(' in A:
        if A.count('(')!=A.count(')'):
            raise TypeError("Falta Parentesis")
        
        A_P = A.index('(')
        A[A_P]=str(Expresion(A[A_P+1:A.index(')')]).simplify())
        B = A[A_P+1:A.index(')')]
        for i in range(len(B)+1):
            A.pop(A_P+1)
        A[A_P]=ElimVac(A[A_P])
        Expr = ''.join(A)
   A = str(Expresion(Expr).simplify())
   R = ElimVac(A)
   
   if isF(R)==True:
       R = Fraccionario(Fraccionario(R).simp())
       if R.den==1:
           return R.num
       else:
           return str(R)+' = '+str(R.num/float(R.den))
   else:
        return R