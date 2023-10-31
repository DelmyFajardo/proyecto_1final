import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

def find_inverse():
    try:
        matrix_text = inverse_entry.get()
        matrix = np.array(eval(matrix_text))
        inverse = np.linalg.inv(matrix)
        inverse_result.set(str(inverse))
    except Exception as e:
        inverse_result.set("Error")

def multiply_matrices():
    try:
        matrix_a_text = matrix_a_entry.get()
        matrix_b_text = matrix_b_entry.get()
        matrix_a = np.array(eval(matrix_a_text))
        matrix_b = np.array(eval(matrix_b_text))
        result = np.dot(matrix_a, matrix_b)
        multiplication_result.set(str(result))
    except Exception as e:
        multiplication_result.set("Error")


        
def solve_equations():
    try:
        coefficients_text = coefficients_entry.get()
        constants_text = constants_entry.get()
        coefficients = np.array(eval(coefficients_text))
        constants = np.array(eval(constants_text))
        method = method_var.get()
        
        if len(coefficients) == 4 and len(constants) == 2:
            A = coefficients.reshape(2, 2)
            if method == "Gauss-Jordan":
                solution = np.linalg.solve(A, constants)
            else:
                det_A = np.linalg.det(A)
                A1 = A.copy()
                A2 = A.copy()
                A1[:, 0] = constants
                A2[:, 1] = constants
                solution = np.array([np.linalg.det(A1) / det_A, np.linalg.det(A2) / det_A])
        elif len(coefficients) == 9 and len(constants) == 3:
            A = coefficients.reshape(3, 3)
            solution = np.linalg.solve(A, constants)
        else:
            solution = "Error"
        
        equations_result.set(str(solution))
    except Exception as e:
        equations_result.set("Error")

def plot_equation():
    try:
        equation = equation_entry.get()
        x = np.linspace(-10, 10, 100)
        y = eval(equation)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica de la ecuación')
        plt.grid(True)
        plt.show()
    except Exception as e:
        plt.close()
        equation_result.set("Error")

app = tk.Tk()
app.title("Calculadora de Matrices y Ecuaciones")
app.geometry("800x600")  # Aumenté la altura para acomodar mejor los elementos

# Estilo para los widgets
style = ttk.Style()
style.configure('TButton', padding=(10, 5), width=20)
style.configure('TLabel', padding=(5, 5))

# Crear un notebook para las dos pestañas
notebook = ttk.Notebook(app)

# Pestaña de Instrucciones
instructions_frame = ttk.Frame(notebook)
notebook.add(instructions_frame, text="Instrucciones")
instructions_label = tk.Label(
    instructions_frame,
    text="Instrucciones:\n\n"
    "Inversa de una matriz:\n"
    "1. Introduce la matriz de la que deseas calcular la inversa en la casilla de texto.\n"
    "2. Asegúrate de que la matriz esté en el formato adecuado, por ejemplo [[1, 2], [3, 4]].\n"
    "3. Haz clic en el botón 'Calcular Inversa'.\n\n"
    "Multiplicación de matrices:\n"
    "1. Introduce las matrices A y B en las casillas de texto correspondientes.\n"
    "2. Asegúrate de que las matrices estén en el formato adecuado, por ejemplo, [[1, 2], [3, 4]].\n"
    "3. Haz clic en el botón 'Multiplicar Matrices'.\n\n"
    "Ecuaciones de resolución:\n"
    "1. Introduce los coeficientes de las ecuaciones y las constantes en las casillas de texto.\n"
    "2. Los coeficientes y constantes deben estar separados por comas, por ejemplo, 1, 2, 4, -1 para un sistema de dos ecuaciones.\n"
    "3. Selecciona el método de resolución ('Gauss-Jordan' o 'Regla de Cramer') en el menú desplegable.\n"
    "4. Haz clic en el botón 'Resolver Ecuaciones'.\n\n"
    "Ejemplo (Regla de Cramer):\n"
    "Supongamos que tenemos el siguiente sistema de ecuaciones:\n"
    "1. 2x + 3y = 12\n"
    "2. 4x - y = 8\n"
    "Ingresa los coeficientes 1, 2, 4, -1 (en ese orden) y las constantes 12, 8 (en ese orden) en las casillas de texto correspondientes.\n"
"Selecciona el método 'Regla de Cramer' en el menú desplegable.\n"
    "Haz clic en el botón 'Resolver Ecuaciones'.\n"
    "El código calculará la solución utilizando la Regla de Cramer y mostrará el resultado en la ventana de la aplicación.\n"
    "Nota: Este es solo un ejemplo; puedes ingresar tus propios sistemas de ecuaciones en el formato adecuado para resolverlos utilizando este código.\n\n"
    "Gráfico de ecuación:\n"
    "1. Introduce una ecuación válida en la casilla de texto.\n"
    "2. Por ejemplo, puedes escribir una ecuación en términos de x, como 2 * x**2 + 3 * x - 5.\n"
    "3. Haz clic en el botón 'Graficar Ecuación'.\n"
    "Se abrirá una ventana con la gráfica de la ecuación. Si hay un error, se mostrará 'Error'.",
    justify="left"
)
instructions_label.pack(fill="both", expand=True, padx=20, pady=20)


# Pestaña de Operaciones
operations_frame = ttk.Frame(notebook)
notebook.add(operations_frame, text="Operaciones")

# Interfaz de operación (agrega tus widgets para operaciones aquí)
inverse_label = ttk.Label(operations_frame, text="Inversa de una matriz:")
inverse_label.pack()
inverse_entry = ttk.Entry(operations_frame)
inverse_entry.pack()
inverse_result = tk.StringVar()
inverse_result_label = ttk.Label(operations_frame, textvariable=inverse_result)
inverse_result_label.pack()
inverse_button = ttk.Button(operations_frame, text="Calcular Inversa", command=find_inverse)
inverse_button.pack()

matrix_a_label = ttk.Label(operations_frame, text="Matriz A:")
matrix_a_label.pack()
matrix_a_entry = ttk.Entry(operations_frame)
matrix_a_entry.pack()

matrix_b_label = ttk.Label(operations_frame, text="Matriz B:")
matrix_b_label.pack()
matrix_b_entry = ttk.Entry(operations_frame)
matrix_b_entry.pack()
multiplication_result = tk.StringVar()
multiplication_result_label = ttk.Label(operations_frame, textvariable=multiplication_result)
multiplication_result_label.pack()
multiply_button = ttk.Button(operations_frame, text="Multiplicar Matrices", command=multiply_matrices)
multiply_button.pack()

equations_label = ttk.Label(operations_frame, text="Resolver ecuaciones:")
equations_label.pack()
coefficients_label = ttk.Label(operations_frame, text="Coeficientes (separados por comas):")
coefficients_label.pack()
coefficients_entry = ttk.Entry(operations_frame)
coefficients_entry.pack()
constants_label = ttk.Label(operations_frame, text="Constantes (separadas por comas):")
constants_label.pack()
constants_entry = ttk.Entry(operations_frame)
constants_entry.pack()

method_label = ttk.Label(operations_frame, text="Método:")
method_label.pack()
method_var = tk.StringVar()
method_combo = ttk.Combobox(operations_frame, textvariable=method_var, values=["Gauss-Jordan", "Regla de Cramer"])
method_combo.set("Gauss-Jordan")
method_combo.pack()
equations_result = tk.StringVar()
equations_result_label = ttk.Label(operations_frame, textvariable=equations_result)
equations_result_label.pack()
solve_button = ttk.Button(operations_frame, text="Resolver Ecuaciones", command=solve_equations)
solve_button.pack()
equation_label = ttk.Label(operations_frame, text="Gráfica de una ecuación:")
equation_label.pack()
equation_entry = ttk.Entry(operations_frame)
equation_entry.pack()
equation_result = tk.StringVar()
equation_result_label = ttk.Label(operations_frame, textvariable=equation_result)
equation_result_label.pack()
plot_button = ttk.Button(operations_frame, text="Graficar Ecuación", command=plot_equation)
plot_button.pack()

notebook.pack(fill="both", expand=True)

app.mainloop()
