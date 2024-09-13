import time

class Caminos:
    def __init__(self, N, M):
        self.N = N - 1  # num de filas para insertar correctamente en los for
        self.M = M - 1  # num de columnas para insertar correctamente en los for
        self.tiempos_ejecucion = {}  # diccionario para almacenar los tiempos en la instancia

    def medir_tiempo(func):
        def decorador(self):
            inicio = time.time()  # comienza a medir el tiempo
            resultado = func(self)  # llama a la función original
            fin = time.time()  # termina de medir el tiempo
            tiempo = fin - inicio
            # se guarda el tiempo de ejecución en el diccionario de la instancia
            self.tiempos_ejecucion[func.__name__] = tiempo
            print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.6f} segundos")
            return resultado
        return decorador
    
    @medir_tiempo
    def contar_caminos_comb(self):
        # Aca lo cambie para verificar si habia algun cambio si ocupaba una funcion auxiliar,
        #pero no hubo ningun cambio en el conteo del tiempo
        # Conteo directo del factorial dado distintos resultados factoriales, donde
        #este resultado se creo en base a lapiz y papel (estuve harto rato intentando entender)
        N = self.N
        M = self.M
        resultado_factorial_NM = 1
        resultado_factorial_N = 1
        resultado_factorial_M = 1
        for i in range(2, N + M + 1): 
            resultado_factorial_NM *= i
        for i in range(2, N + 1): 
            resultado_factorial_N *= i
        for i in range(2, M + 1): 
            resultado_factorial_M *= i

        return resultado_factorial_NM // (resultado_factorial_N * resultado_factorial_M)

    @medir_tiempo
    def contar_caminos_dinamic(self):
        # Se crea la matriz de ceros dado tamaño de filas y columnas
        grilla = [[0] * (self.M + 1) for i in range(self.N + 1)]  
        grilla[0][0] = 1
        # Se iteran en loops for dado tamaños de filas  y despues columnas (podia ser al reves),
        #donde se van sumando segun indices anteriores, avanzando siempre a lo largo de un indice positivo
        #en la matriz
        for i in range(self.N + 1):
            for j in range(self.M + 1):
                if i > 0:
                    grilla[i][j] += grilla[i - 1][j]
                if j > 0:
                    grilla[i][j] += grilla[i][j - 1]

        return grilla[self.N][self.M] 


