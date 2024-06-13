# Sistema de Gestión de Equipos y Partidos

Este es un sistema simple para gestionar equipos de fútbol y sus partidos. Permite agregar equipos, registrar partidos con sus resultados y ver la clasificación de equipos basada en los puntos y diferencia de goles.

## Requisitos

- Python 3.11 instalado
- Archivos CSV de datos de equipos y partidos (`teams.csv` y `matches.csv`) en la carpeta `data`.

## Instalación

1. **Clonar el repositorio:**
   git clone https://github.com/SantFLY/SistemadeGestion

## Ejecucion

1.  **Ejecutar el programa:**

    Desde la carpeta raíz del proyecto, ejecuta:

        - python app.py

    Esto iniciará la aplicación en la consola.

2.  **Interactuar con la aplicación:**

    Una vez iniciada la aplicación, seguir las instrucciones en pantalla:

        - Para agregar un nuevo equipo, selecciona la opción 1 del menú principal.
        - Para ver la clasificación, selecciona la opción 2.
        - Para agregar un nuevo partido, selecciona la opción 3.
        - Para ver los partidos por fecha, selecciona la opción 4.
        - Para salir de la aplicación, selecciona la opción 5.

## Funcionalidades

- Agregar equipo: Permite registrar un nuevo equipo con su nombre.
- Ver clasificación: Muestra la tabla de posiciones de los equipos ordenados por puntos y diferencia de goles.
- Agregar partido: Permite registrar un nuevo partido entre dos equipos con sus respectivos resultados y fecha.
- Ver partidos por fecha: Muestra la lista de partidos registrados ordenados por fecha.
- Guardar datos: Los datos de equipos y partidos se guardan automáticamente en los archivos CSV después de cada operación de modificación.

## Recordatorio

- Cada vez que se reinicie la aplicacion se reiniciara la tabla de clasificacion sin embargo no se borraran los equipo y partidos registrados.

## Ultimos cambios

- Cambio de nombre del archivo `readme` al nombre `README.md`.
- Adición de archivo `.gitignore` para mejor rendimiento del repositorio.
- Correccion en el archivo `views/console_view.py` para validar que el campo ingresado sea tipo `number` para evitar errores.

  ```python
   def get_match_input(self):
      ### Otro codigo ###

      # Validar que el input ingresado sea de tipo numerico
      while True:
          try:
              score1 = int(input("Ingrese el resultado del equipo 1: "))
              score2 = int(input("Ingrese el resultado del equipo 2: "))
              break
          except ValueError:
              print("Error: Debe ingresar un valor numérico.")

      ### Otro codigo ###
  ```

## Recomendaciones de buenas practicas

- Comentar las funciones del script.



---

Aplicacion desarrollada por Santiago Polanco

Editado por [Felipe Silva](https://github.com/AND3SIL4/)

Ultima modificación | Junio 13, 2024
