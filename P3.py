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
    
    def medir_tiempo(func):
        def decorador(self):
            inicio = time.time()  # Comienza a medir el tiempo
            resultado = func(self)  # llama a la funcion original
            fin = time.time()  # termina de medir el tiempo
            print(f"Tiempo de ejecucion de {func.__name__}: {fin - inicio:.6f} segundos")
            return resultado
        return decorador
    
    """Decoramos cada funcion"""

    @medir_tiempo
    def contar_caminos_combinatorio(self):
        # conteo directo dado factorial() definido anteriormente, donde
        #esta funcion se creo en base a lapiz y papel (estuve harto rato intentando entender)
        return self.factorial(self.N + self.M) // (self.factorial(self.N) * self.factorial(self.M))

    @medir_tiempo
    def contar_caminos_dinamic(self):
        # se crea la matriz de ceros dado tamaño de filas y columnas
        grilla = [[0] * (self.M + 1) for i in range(self.N + 1)]  
        grilla[0][0] = 1
        # se iteran en loops for dado tamaños de filas  y despues columnas (podia ser al reves),
        #donde se van sumando segun indices anteriores, avanzando siempre a lo largo de un indice positivo
        #en la matriz
        for i in range(self.N + 1):
            for j in range(self.M + 1):
                if i > 0:
                    grilla[i][j] += grilla[i - 1][j]
                if j > 0:
                    grilla[i][j] += grilla[i][j - 1]

        return grilla[self.N][self.M] 
