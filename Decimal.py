class Decimal:
    def __init__(self, dec):
        self.d = float(dec) # Numero decimal (float)
        self.decimal = dec # Expresion decimal (str)
        D = list(self.decimal)
        self.P_e = D[0:D.index('.')]
        self.P_d = D[D.index('.')+1:len(D)]
        self.ent = int(''.join(self.P_e)) # Parte entera (int)
        self.dec = int(''.join(self.P_d)) # Parte decimal (int)
         
    def __str__(self):
        return str(self.decimal)
       
    def simp(self):
        # Ingresa expresion decimal
        # Returna expresiond decimal reducida
        while len(self.P_e)>1 and self.P_e[0]=='0':
            self.P_e.pop(0)
        self.ent = ''.join(self.P_e)
    
        while len(self.P_d)>1 and self.P_d[-1]=='0':
            self.P_d.pop(len(self.P_d)-1)
        self.dec = ''.join(self.P_d)

        return self.ent+'.'+self.dec