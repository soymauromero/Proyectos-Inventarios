import math

class EOQ_Model:
    def __init__(self, demanda=0, ordenes=0, costo=0, flotante=0, lider=0, escasez_esperada=False, costo_minimo=0):
        self.demanda = demanda
        self.ordenes = ordenes
        self.flotante = flotante
        self.lider = lider
        self.costo = costo
        self.escasez_esperada = escasez_esperada
        self.costo_minimo = costo_minimo
            
    
    def optimal_ordenes_quantity(self, d=None, K=None, h=None, p=None):
        '''Calcula la cantidad de ordenes

        :parametro K: costo de las ordenes
        :parametro d: total demanda
        :parametro h: costo de tenencia

        :return: retorna la cantidad de reorden
        '''
        if d is None:
            d = self.demanda
        if K is None:
            K = self.ordenes
        if h is None:
            h = self.flotante
        if p is None:
            p = self.costo_minimo
        
        if self.escasez_esperada:
            return math.sqrt((2*d*K)/h) * math.sqrt(self.costo_minimo/(self.costo_minimo + self.flotante))
        else:
            return math.sqrt((2*d*K)/h)

    def reordenes_point(self, d=None, L=None):
        '''Calcula las ordenes sin faltante.
        

        :parametro d: total demanda
        :parametro L: tiempo de espera 

        :return: retorna los puntos de reorden
        '''
        if d is None:
            d = self.demanda
        if L is None:
            L = self.lider
        return d * L
    
    def optimal_cycle_time(self, d=None, K=None, h=None, p=None):
        '''Calcula el ciclo optimo de tiempo.

        :parametro K: costo impuesto a las ordenes
        :parametro d: total demanda
        :parametro h: costo de tenencia
        
        :return: retorna los puntos de reorden 
        '''
        if d is None:
            d = self.demanda
        if K is None:
            K = self.ordenes
        if h is None:
            h = self.flotante
        if p is None:
            p = self.costo_minimo
        
        if self.escasez_esperada:
            return math.sqrt((2*K)/(h*d)) * math.sqrt((self.costo_minimo + self.flotante)/self.costo_minimo)
        else:
            return math.sqrt((2*K)/(h*d))
    
    def complete_calculations(self):
        '''Calcula los resultados de las dos metricas principales, la cantidad de ordenes y el ciclo de tiempo optimo.
        
        
        :return: retorna una tupla de metricas
        '''
        
        Q = self.optimal_ordenes_quantity()
        t = self.optimal_cycle_time()
        Q = round(Q)
        t = round(t, 3)
        print("Cantidad optima de ordenes (Q*): {} unidades".format(Q))
        print("Ciclo de tiempo optimo (t*): {}".format(t))

"""
Listado de ejemplos (Tutorial):
1. Busca el caso de uso
2. Quitale los comentarios a ese caso de uso
3. Puedes modificar a tu conveniencia los valores de las variables
4. Ejecuta el archivo
"""
# ========================================= Ejemplo sin faltante =========================================

# d=500
# K=100
# c=20
# h=2
# p=0.8

# model = EOQ_Model(demanda=d, ordenes=K, costo=c, flotante=h, escasez_esperada=False, costo_minimo=p)
# model.complete_calculations()

# Salida
# Cantidad optima de ordenes (Q*): 224 units
# Ciclo de tiempo optimo (t*): 0.447

# ========================================= Ejemplo con faltante =========================================

# d=500
# K=100
# c=20
# h=2
# p=0.8

# model = EOQ_Model(demanda=d, ordenes=K, costo=c, flotante=h, escasez_esperada=True, costo_minimo=p)
# model.complete_calculations()

# Salida
# Cantidad optima de ordenes (Q*): 120 unidades
# Ciclo de tiempo optimo (t*): 0.837

# ====================================== Analisis de sensibilidad ======================================

# 1. Incrementar "K" Y se espera que tanto Q como t aumenten (sin faltante)

# d=500
# c=20
# h=2
# p=0.8
# K = [80, 100, 150, 200]

# for k in K:
#     print("Valor de K: {}".format(k))
#     model = EOQ_Model(demanda=d, ordenes=k, costo=c, flotante=h, escasez_esperada=False, costo_minimo=p)
#     model.complete_calculations()
#     print('-----------------')

# Salida
# Valor de K: 80
# Cantidad optima de ordenes (Q*): 200 unidades
# Ciclo de tiempo optimo (t*): 0.4
# -----------------
# Valor de K: 100
# Cantidad optima de ordenes (Q*): 224 unidades
# Ciclo de tiempo optimo (t*): 0.447
# -----------------
# Valor de K: 150
# Cantidad optima de ordenes (Q*): 274 unidades
# Ciclo de tiempo optimo (t*): 0.548
# -----------------
# Valor de K: 200
# Cantidad optima de ordenes (Q*): 316 unidades
# Ciclo de tiempo optimo (t*): 0.632
# -----------------

# 2. Incrementar "h" Y se espera que tanto Q como t disminuyan (sin faltante)

# d=500
# K=100
# c=20
# p=0.8
# H = [2,4,6,8,10]

# for h in H:
#     print("Valor de h: {}".format(h))
#     model = EOQ_Model(demanda=d, ordenes=K, costo=c, flotante=h, escasez_esperada=False, costo_minimo=p)
#     model.complete_calculations()
#     print('-----------------')

# Salida
# Valor de h: 2
# Cantidad optima de ordenes (Q*): 224 unidades
# Ciclo de tiempo optimo (t*): 0.447
# -----------------
# Valor de h: 4
# Cantidad optima de ordenes (Q*): 158 unidades
# Ciclo de tiempo optimo (t*): 0.316
# -----------------
# Valor de h: 6
# Cantidad optima de ordenes (Q*): 129 unidades
# Ciclo de tiempo optimo (t*): 0.258
# -----------------
# Valor de h: 8
# Cantidad optima de ordenes (Q*): 112 unidades
# Ciclo de tiempo optimo (t*): 0.224
# -----------------
# Valor de h: 10
# Cantidad optima de ordenes (Q*): 100 unidades
# Ciclo de tiempo optimo (t*): 0.2
# -----------------

# 3. Incrementar "d" Y se espera que Q aumente y t disminuya (sin faltante)

# D=[200,400,600,800]
# K=100
# c=20
# p=0.8
# h=2


# for d in D:
#     print("Valor de d: {}".format(d))
#     model = EOQ_Model(demanda=d, ordenes=K, costo=c, flotante=h, escasez_esperada=False, costo_minimo=p)
#     model.complete_calculations()
#     print('-----------------')

# Salida
# Valor de d: 200
# Cantidad optima de ordenes (Q*): 141 unidades
# Ciclo de tiempo optimo (t*): 0.707
# -----------------
# Valor de d: 400
# Cantidad optima de ordenes (Q*): 200 unidades
# Ciclo de tiempo optimo (t*): 0.5
# -----------------
# Valor de d: 600
# Cantidad optima de ordenes (Q*): 245 unidades
# Ciclo de tiempo optimo (t*): 0.408
# -----------------
# Valor de d: 800
# Cantidad optima de ordenes (Q*): 283 unidades
# Ciclo de tiempo optimo (t*): 0.354
# -----------------