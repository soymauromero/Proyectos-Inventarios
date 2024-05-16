import numpy as np

# Se define la funcion LEP
def LEP(D, P, K, H):
    
    """
    Lote Economico de Produccion

    Argumentos:
    D: cantidad demandada anual
    K: costo de producción
    H: costo de tenencia por unidad
    P: tasa de producción

    Devuelve:
    ["Q (tamaño del lote):", 
    "Duracion del ciclo", 
    "Numero de ejecuciones de produccion", 
    "Duracion de la ejecucion de produccion", 
    "Duracion del periodo de demanda", 
    "Costo de produccion", 
    "Costo de tenencia anual", 
    "Maximo nivel de inventario", 
    "Costo total anual"]
    """

    if(D>0 and P>0 and K>0 and H>0):

        Q = (np.sqrt((2*D*K)/(H*(1-(D/P)))))
        T = round(Q/D*12,2)
        numero_de_ejecuciones_produccion = D/Q
        Tp = round(Q/P*12,2)
        Td = round((Q/D-Q/P)*12,2)
        APC = numero_de_ejecuciones_produccion*K
        AHC = Q/2*(1-(D/P))*H
        Imax = Q*(1-(D/P))
        ATC = APC+AHC

        print("Q:", Q , 
              "\nDuracion del ciclo:", T, 
              "\nNumero de ejecuciones de produccion:", numero_de_ejecuciones_produccion, 
              "\nDuracion de la ejecucion de produccion:", Tp, 
              "\nDuracion del periodo de demanda:", Td, 
              "\nCosto de produccion:", APC, 
              "\nCosto de tenencia anual:", AHC, 
              "\nMaximo nivel de inventario:", Imax, 
              "\nCosto total anual:", ATC)
        
        return[Q , T, numero_de_ejecuciones_produccion, Tp, Td, APC, AHC, Imax, ATC]

    else:
        print("Error. Todos los argumentos de la función no deben ser negativos.")
        
# ================================================== Casos de Uso ==================================================

# ======================================= Ejemplo sencillo de la ejecucion =======================================

# D = 500
# P = 1000
# K = 100
# H = 2

# LEP(D, P, K, H)

# Salida
# Q: 316.22776601683796 
# Duracion del ciclo: 7.59 
# Numero de ejecuciones de produccion: 1.5811388300841895 
# Duracion de la ejecucion de produccion: 3.79 
# Duracion del periodo de demanda: 3.79 
# Costo de produccion: 158.11388300841895 
# Costo de tenencia anual: 158.11388300841898 
# Maximo nivel de inventario: 158.11388300841898 
# Costo total anual: 316.2277660168379

# ================================================ Incrementar "K" ================================================

# D = 500
# P = 1000
# K = [80, 100, 150, 200]
# H = 2

# for k in K:
#     print("Valor de K: {}".format(k))
#     LEP(D, P, k, H)
#     print('-----------------------------------------------------------')

# Salida
# Valor de K: 80
# Q: 282.842712474619 
# Duracion del ciclo: 6.79 
# Numero de ejecuciones de produccion: 1.7677669529663687 
# Duracion de la ejecucion de produccion: 3.39 
# Duracion del periodo de demanda: 3.39 
# Costo de produccion: 141.42135623730948 
# Costo de tenencia anual: 141.4213562373095 
# Maximo nivel de inventario: 141.4213562373095 
# Costo total anual: 282.842712474619
# -----------------------------------------------------------
# Valor de K: 100
# Q: 316.22776601683796 
# Duracion del ciclo: 7.59 
# Numero de ejecuciones de produccion: 1.5811388300841895 
# Duracion de la ejecucion de produccion: 3.79 
# Duracion del periodo de demanda: 3.79 
# Costo de produccion: 158.11388300841895 
# Costo de tenencia anual: 158.11388300841898 
# Maximo nivel de inventario: 158.11388300841898 
# Costo total anual: 316.2277660168379
# -----------------------------------------------------------
# Valor de K: 150
# Q: 387.2983346207417 
# Duracion del ciclo: 9.3 
# Numero de ejecuciones de produccion: 1.2909944487358056 
# Duracion de la ejecucion de produccion: 4.65 
# Duracion del periodo de demanda: 4.65 
# Costo de produccion: 193.64916731037084 
# Costo de tenencia anual: 193.64916731037084 
# Maximo nivel de inventario: 193.64916731037084 
# Costo total anual: 387.2983346207417
# -----------------------------------------------------------
# Valor de K: 200
# Q: 447.21359549995793 
# Duracion del ciclo: 10.73 
# Numero de ejecuciones de produccion: 1.118033988749895 
# Duracion de la ejecucion de produccion: 5.37 
# Duracion del periodo de demanda: 5.37 
# Costo de produccion: 223.60679774997897 
# Costo de tenencia anual: 223.60679774997897 
# Maximo nivel de inventario: 223.60679774997897 
# Costo total anual: 447.21359549995793
# -----------------------------------------------------------

# ================================================ Incrementar "H" ================================================

# D = 500
# P = 1000
# K = 100
# H = [2,4,6,8,10]

# for h in H:
#     print("Valor de H: {}".format(h))
#     LEP(D, P, K, h)
#     print('-----------------------------------------------------------')

# Salida
# Valor de H: 2
# Q: 316.22776601683796 
# Duracion del ciclo: 7.59 
# Numero de ejecuciones de produccion: 1.5811388300841895 
# Duracion de la ejecucion de produccion: 3.79 
# Duracion del periodo de demanda: 3.79 
# Costo de produccion: 158.11388300841895 
# Costo de tenencia anual: 158.11388300841898 
# Maximo nivel de inventario: 158.11388300841898 
# Costo total anual: 316.2277660168379
# -----------------------------------------------------------
# Valor de H: 4
# Q: 223.60679774997897 
# Duracion del ciclo: 5.37 
# Numero de ejecuciones de produccion: 2.23606797749979 
# Duracion de la ejecucion de produccion: 2.68 
# Duracion del periodo de demanda: 2.68 
# Costo de produccion: 223.60679774997897 
# Costo de tenencia anual: 223.60679774997897 
# Maximo nivel de inventario: 111.80339887498948 
# Costo total anual: 447.21359549995793
# -----------------------------------------------------------
# Valor de H: 6
# Q: 182.57418583505537 
# Duracion del ciclo: 4.38 
# Numero de ejecuciones de produccion: 2.7386127875258306 
# Duracion de la ejecucion de produccion: 2.19 
# Duracion del periodo de demanda: 2.19 
# Costo de produccion: 273.8612787525831 
# Costo de tenencia anual: 273.8612787525831 
# Maximo nivel de inventario: 91.28709291752769 
# Costo total anual: 547.7225575051662
# -----------------------------------------------------------
# Valor de H: 8
# Q: 158.11388300841898 
# Duracion del ciclo: 3.79 
# Numero de ejecuciones de produccion: 3.162277660168379 
# Duracion de la ejecucion de produccion: 1.9 
# Duracion del periodo de demanda: 1.9 
# Costo de produccion: 316.2277660168379 
# Costo de tenencia anual: 316.22776601683796 
# Maximo nivel de inventario: 79.05694150420949 
# Costo total anual: 632.4555320336758
# -----------------------------------------------------------
# Valor de H: 10
# Q: 141.4213562373095 
# Duracion del ciclo: 3.39 
# Numero de ejecuciones de produccion: 3.5355339059327373 
# Duracion de la ejecucion de produccion: 1.7 
# Duracion del periodo de demanda: 1.7 
# Costo de produccion: 353.5533905932737 
# Costo de tenencia anual: 353.5533905932738 
# Maximo nivel de inventario: 70.71067811865476 
# Costo total anual: 707.1067811865476
# -----------------------------------------------------------

# ================================================ Incrementar "D" ================================================

# D = [200,400,600,800]
# P = 1000
# K = 100
# H = 2

# for d in D:
#     print("Valor de D: {}".format(d))
#     LEP(d, P, K, H)
#     print('-----------------------------------------------------------')

# # Salida
# Valor de D: 200
# Q: 158.11388300841898 
# Duracion del ciclo: 9.49 
# Numero de ejecuciones de produccion: 1.2649110640673515 
# Duracion de la ejecucion de produccion: 1.9 
# Duracion del periodo de demanda: 7.59 
# Costo de produccion: 126.49110640673516 
# Costo de tenencia anual: 126.49110640673518 
# Maximo nivel de inventario: 126.49110640673518 
# Costo total anual: 252.98221281347034
# -----------------------------------------------------------
# Valor de D: 400
# Q: 258.19888974716116 
# Duracion del ciclo: 7.75 
# Numero de ejecuciones de produccion: 1.5491933384829666 
# Duracion de la ejecucion de produccion: 3.1 
# Duracion del periodo de demanda: 4.65 
# Costo de produccion: 154.91933384829665 
# Costo de tenencia anual: 154.9193338482967 
# Maximo nivel de inventario: 154.9193338482967 
# Costo total anual: 309.83866769659335
# -----------------------------------------------------------
# Valor de D: 600
# Q: 387.2983346207417 
# Duracion del ciclo: 7.75 
# Numero de ejecuciones de produccion: 1.5491933384829668 
# Duracion de la ejecucion de produccion: 4.65 
# Duracion del periodo de demanda: 3.1 
# Costo de produccion: 154.91933384829667 
# Costo de tenencia anual: 154.91933384829667 
# Maximo nivel de inventario: 154.91933384829667 
# Costo total anual: 309.83866769659335
# -----------------------------------------------------------
# Valor de D: 800
# Q: 632.4555320336759 
# Duracion del ciclo: 9.49 
# Numero de ejecuciones de produccion: 1.2649110640673515 
# Duracion de la ejecucion de produccion: 7.59 
# Duracion del periodo de demanda: 1.9 
# Costo de produccion: 126.49110640673516 
# Costo de tenencia anual: 126.49110640673516 
# Maximo nivel de inventario: 126.49110640673516 
# Costo total anual: 252.9822128134703
# -----------------------------------------------------------

# ================================================ Incrementar "P" ================================================

D = 500
P = [1000, 2000, 3000, 4000]
K = 100
H = 2

for p in P:
    print("Valor de P: {}".format(p))
    LEP(D, p, K, H)
    print('-----------------------------------------------------------')

# Salida
# Valor de P: 1000
# Q: 316.22776601683796 
# Duracion del ciclo: 7.59 
# Numero de ejecuciones de produccion: 1.5811388300841895 
# Duracion de la ejecucion de produccion: 3.79 
# Duracion del periodo de demanda: 3.79 
# Costo de produccion: 158.11388300841895 
# Costo de tenencia anual: 158.11388300841898 
# Maximo nivel de inventario: 158.11388300841898 
# Costo total anual: 316.2277660168379
# -----------------------------------------------------------
# Valor de P: 2000
# Q: 258.19888974716116 
# Duracion del ciclo: 6.2 
# Numero de ejecuciones de produccion: 1.9364916731037083 
# Duracion de la ejecucion de produccion: 1.55 
# Duracion del periodo de demanda: 4.65 
# Costo de produccion: 193.64916731037084 
# Costo de tenencia anual: 193.64916731037087 
# Maximo nivel de inventario: 193.64916731037087 
# Costo total anual: 387.2983346207417
# -----------------------------------------------------------
# Valor de P: 3000
# Q: 244.94897427831782 
# Duracion del ciclo: 5.88 
# Numero de ejecuciones de produccion: 2.041241452319315 
# Duracion de la ejecucion de produccion: 0.98 
# Duracion del periodo de demanda: 4.9 
# Costo de produccion: 204.12414523193152 
# Costo de tenencia anual: 204.12414523193152 
# Maximo nivel de inventario: 204.12414523193152 
# Costo total anual: 408.24829046386304
# -----------------------------------------------------------
# Valor de P: 4000
# Q: 239.04572186687872 
# Duracion del ciclo: 5.74 
# Numero de ejecuciones de produccion: 2.091650066335189 
# Duracion de la ejecucion de produccion: 0.72 
# Duracion del periodo de demanda: 5.02 
# Costo de produccion: 209.16500663351889 
# Costo de tenencia anual: 209.16500663351889 
# Maximo nivel de inventario: 209.16500663351889 
# Costo total anual: 418.33001326703777
# -----------------------------------------------------------