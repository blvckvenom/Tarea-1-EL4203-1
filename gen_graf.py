from P4 import Caminos
import matplotlib.pyplot as plt

#fun() para generar graficos, ocuparemos la clase del item P4 dado que es el mas avanzado
def generar_graficos():
    matrices = [(i, i) for i in range(5, 1001, 5)] 
    tiempos_combinatorio = []
    tiempos_dinamico = []

    for matriz in matrices:
        caminos = Caminos(matriz[0], matriz[1])
        caminos.contar_caminos_comb()  
        tiempos_combinatorio.append(caminos.tiempos_ejecucion['contar_caminos_comb'])

        caminos.contar_caminos_dinamic()  
        tiempos_dinamico.append(caminos.tiempos_ejecucion['contar_caminos_dinamic'])

    plt.figure()
    plt.plot([f"{s[0]}x{s[1]}" for s in matrices], tiempos_combinatorio, label='Combinatorio', marker='o')
    plt.plot([f"{s[0]}x{s[1]}" for s in matrices], tiempos_dinamico, label='Dinamico', marker='o')
    plt.title('Tiempo de Ejecucion por Metodo')
    plt.xlabel('Tamaño de Entrada')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.legend()
    plt.grid(True)

   
    plt.savefig('tiempos_ejecucion.svg') 
    plt.show() 

generar_graficos()
