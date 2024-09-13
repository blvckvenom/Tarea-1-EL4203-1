#P1 Enunciado:

'''
1. Primero, puede crear un nuevo método por cada solución programada, que entregue el tiempo
de ejecución de dicha solución para un input determinado.
'''
import time

class Caminos:
    def __init__(self, N, M):
        self.N = N - 1  # num de filas para insertar correctamente en los for
        self.M = M - 1  # num de columnas para insertar correctamente en los for

    def factorial(self, num):
        # inicializamos en 1 
        resultado = 1
        # recorremos y multiplicamos segun el num en el for para despues imprimir el resultado
        for i in range(2, num + 1): 
            resultado *= i
        return resultado

    def contar_caminos_combinatorio(self):
        # conteo directo dado factorial() definido anteriormente, donde
        # esta funcion se creo en base a lapiz y papel (estuve harto rato intentando entender)
        return self.factorial(self.N + self.M) // (self.factorial(self.N) * self.factorial(self.M))

    def contar_caminos_dinamico(self):
        # se crea la matriz de ceros dado tamano de filas y columnas
        grilla = [[0] * (self.M + 1) for i in range(self.N + 1)]  
        grilla[0][0] = 1
        # se iteran en loops for dado tamano de filas y despues columnas (podia ser al reves),
        # donde se van sumando segun indices anteriores, avanzando siempre a lo largo de un indice positivo
        # en la matriz
        for i in range(self.N + 1):
            for j in range(self.M + 1):
                if i > 0:
                    grilla[i][j] += grilla[i - 1][j]
                if j > 0:
                    grilla[i][j] += grilla[i][j - 1]

        return grilla[self.N][self.M] 

    # se definen las funciones de conteo para las distintas funciones
    def tiempo_ejecucion_combinatorio(self):
        start_time = time.time()
        resultado = self.contar_caminos_combinatorio()
        end_time = time.time()
        return resultado, end_time - start_time

    def tiempo_ejecucion_dinamico(self):
        start_time = time.time()
        resultado = self.contar_caminos_dinamico()
        end_time = time.time()
        return resultado, end_time - start_time

