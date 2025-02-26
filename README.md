# Sorting Algorithms

Este proyecto contiene la implementación y prueba de varios algoritmos de ordenamiento en Python. Incluye Bubble Sort, Merge Sort, Quick Sort, Insertion Sort y Selection Sort, junto con sus respectivas pruebas unitarias y análisis de rendimiento.

## Problema
El objetivo de este proyecto es analizar y comparar el rendimiento de diferentes algoritmos de ordenamiento aplicados a distintos tipos de listas. Se busca identificar cuál algoritmo es más eficiente dependiendo del caso de uso.

## Requisitos
- Python 3.x
- Librerías necesarias especificadas en `requirements.txt`
- Entorno virtual recomendado (opcional)

## Estructura del Proyecto

```
 sorting-project
    ├── benchmark.py                # Benchmark de los algoritmos
    ├── htmlcov/                    # Reporte HTML de cobertura (se genera después de correr coverage)
    ├── images/                     # Carpeta con gráficas generadas
    ├── README.md                   # Documentación del proyecto
    ├── requirements.txt            # Dependencias del proyecto
    ├── sorting-algorithms.ipynb    # Notebook con análisis de los algoritmos
    ├── sorting.py                  # Implementación de algoritmos de ordenamiento
    └── test_sorting.py             # Pruebas unitarias
```

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/bricenojuliana/ALDA-sorting-algorithms.git
   cd sorting-algorithms
   ```
2. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Puedes ejecutar el notebook `sorting-algorithms.ipynb` para visualizar la ejecución de los algoritmos y sus tiempos de rendimiento. Si deseas probar los algoritmos en la terminal:

```sh
python sorting.py
```

Para ejecutar las pruebas unitarias:
```sh
pytest test_sorting.py
```

Para generar un reporte de cobertura:
```sh
coverage run -m pytest test_sorting.py
coverage report -m
```

Para generar un reporte en HTML:
```sh
coverage html
```
Los archivos generados estarán en la carpeta `htmlcov/`.

## Análisis de Rendimiento
Los gráficos de rendimiento comparan el tiempo de ejecución de cada algoritmo en diferentes casos:
- Listas aleatorias
- Listas ordenadas
- Listas en orden inverso
- Listas con elementos duplicados

Puedes visualizar estos gráficos ejecutando el notebook o revisando la carpeta `images/`.

## Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de usarlo y mejorarlo! 😃

