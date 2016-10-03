class Fraccionario:
    def __init__(self, frac):
        self.frac = frac # Expresion fraccionaria (str)
        f = list(self.frac)
        self.num = int(''.join(f[0:f.index('/')])) # Numerador (int)
        self.den = int(''.join(f[f.index('/')+1:len(f)])) # Denominador (int)

    	if self.den == 0:
            raise ZeroDivisionError("NO SOLUTION: DEN=0")
    
    def __str__(self):
        return str(self.frac)         
      
    def simp(self): 
        # Ingresa expresion fraccionaria. (str)
        # Returna expresion fraccionaria simplificada. (str)
        def mcd(a, b):
            resto = 0
            while(b > 0):
                resto = b
                b = a % b
                a = resto
            return a
        
        if self.num==0:
            return str(self.num)+'/1'
        else:
            x = mcd(self.num, self.den)
            if x!=1:
                while (x!=1):
                    num = self.num/x
                    den = self.den/x
                    x = mcd(num,den) 
                return str(num)+'/'+str(den)
            else: 
                return str(self.num)+'/'+str(self.den)
