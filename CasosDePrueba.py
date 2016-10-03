from FuncionesPrincipales import isZ, isQ, isF
from Operaciones import Operando

print isZ('-6') #True
print isZ('5') #True
print isZ('5.2') #False
print isZ('5/2') #False
print isF('5.2') #False
print isF('5') #False
print isF('5/2') #True
print isQ('5') #False
print isQ('-5.2') #True
print isQ('5/2') #False
print simplify('5+6') #'11'
print simplify('5/6') #'5/6'
print simplify('12/6') #'2'
print simplify('0.5*0.7') #'0.35'
print simplify('0.5/0.7') #'5/7'
print simplify('0.5**3') #'0.125'
print simplify('1.55+0.45') #'2'
print simplify('1/2 + 3/2') #'2'
print simplify('0.4+2/5') #'4/5'
print simplify('(2/3)**2') #'4/9'