"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():

    import os
    import matplotlib.pyplot as plt

    # Crear la carpeta 'plots' si no existe
    if not os.path.exists('./files/plots'):
        os.makedirs('./files/plots/')

    # Crear un gráfico simple
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.title('Gráfico de ejemplo')

    # Guardar el gráfico en la carpeta 'plots' como 'grafico.png'
    plt.savefig('./files/plots/news.png')

    print("El archivo 'grafico.png' ha sido creado en la carpeta 'plots'.")


    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
pregunta_01()