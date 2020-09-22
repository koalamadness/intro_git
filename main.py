"""
garcia_luquin_8.py

script en Python que muestre un menú con las siguientes opciones
1) Canción favorita
2) Película favorita
3) Libro / videojuego favorito
4) Red social favorita
El usuario deberá seleccionar alguna de las opciones y el script abrirá una página web con contenido relacionado a la opción seleccionada
"""

import webbrowser

print("""           Opciones
1) Canción favorita
2) Película favorita
3) Libro / videojuego favorito
4) Red social favorita
""")

opc = int(input("Escoge una opción: "))

if opc == 1:
    webbrowser.open("https://www.youtube.com/watch?v=btPJPFnesV4")
elif opc == 2:
    webbrowser.open("https://www.youtube.com/watch?v=lc0UehYemQA")
elif opc == 3:
    webbrowser.open("https://playhearthstone.com/es-es/")
elif opc == 4:
    webbrowser.open("https://www.reddit.com/")