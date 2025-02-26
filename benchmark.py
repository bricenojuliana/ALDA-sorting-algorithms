import time
import random
import matplotlib.pyplot as plt
from sorting import bubble_sort, merge_sort, quick_sort, insertion_sort, selection_sort

# Algoritmos a evaluar
algorithms = {
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
}


# Generar listas de prueba
def generate_lists(size=1000):
    random_list = [random.randint(0, 10000) for _ in range(size)]
    sorted_list = sorted(random_list)
    reversed_list = sorted_list[::-1]
    duplicate_list = [random.choice(sorted_list) for _ in range(size)]
    empty_list = []
    return {
        "Random": random_list,
        "Sorted": sorted_list,
        "Reversed": reversed_list,
        "Duplicates": duplicate_list,
        "Empty": empty_list,
    }


# Medir tiempos de ejecución
def benchmark_algorithms(sizes=[100, 500, 1000, 5000]):
    results = {alg: {} for alg in algorithms}

    for size in sizes:
        test_cases = generate_lists(size)
        for case_name, test_list in test_cases.items():
            for name, algorithm in algorithms.items():
                arr_copy = test_list[:]  # Copia para evitar modificar el original
                start = time.time()
                algorithm(arr_copy)
                end = time.time()
                results[name].setdefault(case_name, []).append(end - start)

    return results, sizes


# Graficar resultados
def plot_results(results, sizes):
    for case_name in ["Random", "Sorted", "Reversed", "Duplicates", "Empty"]:
        plt.figure(figsize=(8, 5))
        for name, times in results.items():
            plt.plot(sizes, times[case_name], label=name)
        plt.xlabel("Tamaño del arreglo")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.title(f"Comparación de Algoritmos - {case_name} List")
        plt.legend()
        plt.savefig(f"images/{case_name.lower()}_lists.png")
        plt.show()


# Ejecutar benchmark y graficar
if __name__ == "__main__":
    results, sizes = benchmark_algorithms()
    plot_results(results, sizes)
