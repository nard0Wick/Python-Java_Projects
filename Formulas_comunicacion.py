import sympy as sp

class Generar():  
    def __init__(self, **args): 
        self.unidades = { 
                'Y':1E24, 'Z':1E21, 'E':1E18, 'P':1E15, 'T':1E12,
                'G':1E9, 'M':1E6, 'k':1E3, 'h':1E2, 'da':1E1, '1': 1E0,'d':1E-1,
                'c':1E-2, 'm':1E-3, 'µ': 1E-6, 'n':1E-9, 'p':1E-12,
                'f':1E-15, 'a':1E-18, 'z':1E-21, 'y':1E-2  
                }   
        self.x = sp.symbols('x')
        self.conversiones = { 
           'c_k': self.x + 273.15, 
           'f_k': (self.x - 32) * 5/9 + 273.15, 
           'k_k': self.x,
           'k_c': self.x - 273.15, 
           'k_f': (self.x - 273.15) * 9/5 + 32
        }
        self.values = args
        self.hercios = 0.0 
        self.grados = 0.0

    def __str__(self) -> str:
      return f"hercios:" 
    
    def convertir_hz(self): 
       self.hercios = self.values['hercios'] * self.unidades[self.values['unidades_hercios']]

    def convertir_grados(self): 
      self.grados = self.conversiones[self.values['convertir_grados']].subs(self.x, self.values['temperatura'])
    
    def getGrados(self): 
        return self.grados 

    def getHercios(self): 
      return self.hercios   

    

#hercios = float(input("Frecuencia en hercios: ")) 
#unidades_hercios = input("Unidades de los hercios: ")  
temp = float(input("Temperatura: ")) 
convertir = input("Convertir: ") 
generar = Generar(**{'temperatura':temp, 'convertir_grados':convertir})  
#generar.convertir_hz()  
generar.convertir_grados()
print("{:,.4f}".format(generar.getGrados()))


class Calcular(Generar): 
  def __init__(self): 
    pass  
  
  def longitud_onda(self): 
    pass 
  
  def potencia_ruido_termico(self): 
    pass 
  
  def potencia_ruido_termico_dbm(self): 
    pass 
  
  def voltaje_ruido(self): 
    pass 
  
  def temperatura_ruido_equivalente(self): 
    pass 
  
