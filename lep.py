""" Q cantidad de inventario D  es tasa de la demanda R tasa de produccioon """
import math
class Lepp:
#constructor de la clase del modelo lepp y inicializando las variavles 
#de tasa de produccion (Tp) y tassa de demanda (td) 
#
    def __init__(self):
        self.Tp=0
        self.td=0
        self.c=0
    def costo(self,costoP,costoOp,costoMi):
        q=self.cantidadInv(costoOp,costoMi)
        self.c=costoP*q+costoOp+costoMi*(pow(q,2)*(1-self.td/self.Tp))/self.td*2
        return self.c
    #tasa de produccion
    def setTp(self,Tp):
        self.Tp=Tp
    #tasa de demanda
    def settp(self,td):
        self.td=td
    def cantidadInv(self,costoOp,costoMi):
        try:
            return math.sqrt((2*self.td*costoOp)/(costoMi*(1-self.td/self.Tp)))
        except ValueError:
            print(f"Valores inválidos: td={self.td}, costoOp={costoOp}, costoMi={costoMi}, Tp={self.Tp}")
class LeppFal(Lepp):
    def __init__(self):
        super().__init__()
    def costof(self,costoP,costoOp,costoMi,cf):
        q=super().cantidadInv(costoOp,costoMi)*math.sqrt((costoMi+cf)/cf)
        s=math.sqrt(2*self.td*costoOp/cf)*math.sqrt(1-self.td/self.Tp)*math.sqrt(costoMi/(costoMi+cf))
        self.c=costoP*q+costoOp+(costoMi/2)*pow(q*(1-self.td/self.Tp)-s,2)*(1/(self.Tp-self.td)+1/self.td)+(cf*s*s/2)*(1/(self.Tp-self.td)+1/self.td)
        return self.c


