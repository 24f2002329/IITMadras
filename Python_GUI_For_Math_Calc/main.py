import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Eq, sympify, solve, Matrix
import math

class MathCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Calculator")
        self.root.geometry("500x600")
        self.root.config(bg="#e0e0e0")

        self.main_menu()

    def clear_frame(self):
        """Clear the window frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        """Display the main menu."""
        self.clear_frame()

        tk.Label(self.root, text="Math Calculator", font=("Helvetica", 18, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Menu buttons
        tk.Button(self.root, text="Permutation & Combination", command=self.perm_comb_menu, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=1, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Linear Equations Solver", command=self.linear_equation_menu, font=("Helvetica", 12), bg="#2196F3", fg="white").grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Factorial Calculator", command=self.factorial_menu, font=("Helvetica", 12), bg="#FF9800", fg="white").grid(row=3, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Prime Number Checker", command=self.prime_menu, font=("Helvetica", 12), bg="#FFC107", fg="white").grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Quadratic Equation Solver", command=self.quadratic_menu, font=("Helvetica", 12), bg="#9C27B0", fg="white").grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Determinant Calculator", command=self.determinant_menu, font=("Helvetica", 12), bg="#673AB7", fg="white").grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="GCD & LCM Calculator", command=self.gcd_lcm_menu, font=("Helvetica", 12), bg="#3F51B5", fg="white").grid(row=7, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Matrix Multiplication", command=self.matrix_multiplication_menu, font=("Helvetica", 12), bg="#9C27B0", fg="white").grid(row=8, column=0, columnspan=2, pady=10, padx=10)

    def perm_comb_menu(self):
        """Display the Permutation & Combination menu."""
        self.clear_frame()

        tk.Label(self.root, text="Permutation & Combination", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter n:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.n_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.n_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter r:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
        self.r_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.r_entry.grid(row=2, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Calculate Permutation P(n,r)", command=self.calculate_permutation, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Calculate Combination C(n,r)", command=self.calculate_combination, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def linear_equation_menu(self):
        """Display the Linear Equations Solver menu."""
        self.clear_frame()

        tk.Label(self.root, text="Linear Equations Solver", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        tk.Label(self.root, text="Solve 2x2 System", font=("Helvetica", 14), bg="#e0e0e0").grid(row=1, column=0, columnspan=3, pady=5, padx=10)
        self.eq1_2x2_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq1_2x2_entry.grid(row=2, column=0, columnspan=3, pady=5, padx=10)
        self.eq2_2x2_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq2_2x2_entry.grid(row=3, column=0, columnspan=3, pady=5, padx=10)

        tk.Button(self.root, text="Solve 2 Equations", command=self.solve_linear_2eq, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

        tk.Label(self.root, text="Solve 3x3 System", font=("Helvetica", 14), bg="#e0e0e0").grid(row=5, column=0, columnspan=3, pady=5, padx=10)
        self.eq1_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq1_3x3_entry.grid(row=6, column=0, columnspan=3, pady=5, padx=10)
        self.eq2_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq2_3x3_entry.grid(row=7, column=0, columnspan=3, pady=5, padx=10)
        self.eq3_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq3_3x3_entry.grid(row=8, column=0, columnspan=3, pady=5, padx=10)

        tk.Button(self.root, text="Solve 3 Equations", command=self.solve_linear_3eq, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=9, column=0, columnspan=3, pady=5, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=10, column=0, columnspan=3, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=11, column=0, columnspan=3, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=12, column=0, columnspan=3, pady=10, padx=10)

    def factorial_menu(self):
        """Display the Factorial Calculator menu."""
        self.clear_frame()

        tk.Label(self.root, text="Factorial Calculator", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter a non-negative integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.factorial_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.factorial_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Calculate Factorial", command=self.calculate_factorial, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def prime_menu(self):
        """Display the Prime Number Checker menu."""
        self.clear_frame()

        tk.Label(self.root, text="Prime Number Checker", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter an integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.prime_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.prime_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Check if Prime", command=self.check_prime, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def quadratic_menu(self):
        """Display the Quadratic Equation Solver menu."""
        self.clear_frame()

        tk.Label(self.root, text="Quadratic Equation Solver", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        tk.Label(self.root, text="Enter a:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.a_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.a_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter b:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
        self.b_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.b_entry.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter c:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=3, column=0, pady=5, padx=10)
        self.c_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.c_entry.grid(row=3, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Solve Quadratic", command=self.solve_quadratic, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def determinant_menu(self):
        """Display the 3x3 Determinant Calculator menu."""
        self.clear_frame()

        tk.Label(self.root, text="Determinant Calculator (3x3)", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        # Create a grid for the 3x3 matrix
        self.matrix_entries_3x3 = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(self.root, font=("Helvetica", 12), width=5)
                entry.grid(row=i + 1, column=j, pady=5, padx=5)
                row_entries.append(entry)
            self.matrix_entries_3x3.append(row_entries)

        tk.Button(self.root, text="Calculate Determinant", command=self.calculate_determinant_3x3, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=3, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=3, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=3, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=3, pady=10, padx=10)


    def gcd_lcm_menu(self):
        """Display the GCD & LCM Calculator menu."""
        self.clear_frame()

        tk.Label(self.root, text="GCD & LCM Calculator", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter first integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.gcd_lcm_entry1 = tk.Entry(self.root, font=("Helvetica", 12))
        self.gcd_lcm_entry1.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter second integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
        self.gcd_lcm_entry2 = tk.Entry(self.root, font=("Helvetica", 12))
        self.gcd_lcm_entry2.grid(row=2, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Calculate GCD", command=self.calculate_gcd, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, pady=5, padx=10)
        tk.Button(self.root, text="Calculate LCM", command=self.calculate_lcm, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    def matrix_multiplication_menu(self):
        """Display the matrix multiplication menu."""
        self.clear_frame()

        tk.Label(self.root, text="Matrix Multiplication", font=("Helvetica", 18, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        tk.Label(self.root, text="Enter number of rows for Matrix A:", bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=5)
        self.rows_a_entry = tk.Entry(self.root, width=5)
        self.rows_a_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(self.root, text="Enter number of columns for Matrix A:", bg="#e0e0e0").grid(row=1, column=2, pady=5, padx=5)
        self.cols_a_entry = tk.Entry(self.root, width=5)
        self.cols_a_entry.grid(row=1, column=3, pady=5, padx=5)

        tk.Label(self.root, text="Enter number of rows for Matrix B:", bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=5)
        self.rows_b_entry = tk.Entry(self.root, width=5)
        self.rows_b_entry.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(self.root, text="Enter number of columns for Matrix B:", bg="#e0e0e0").grid(row=2, column=2, pady=5, padx=5)
        self.cols_b_entry = tk.Entry(self.root, width=5)
        self.cols_b_entry.grid(row=2, column=3, pady=5, padx=5)

        tk.Button(self.root, text="Set Matrices", command=self.set_matrices, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=4, pady=10, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5, padx=10)

    def reset_inputs(self):
        """Clear all input fields and result labels."""
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            if isinstance(widget, tk.Label) and "result" in widget.cget("text"):
                widget.config(text="")

    def calculate_permutation(self):
        """Calculate permutation P(n, r)."""
        n = int(self.n_entry.get())
        r = int(self.r_entry.get())
        result = math.perm(n, r)
        self.result_label.config(text=f"P({n},{r}) = {result}")

    def calculate_combination(self):
        """Calculate combination C(n, r)."""
        n = int(self.n_entry.get())
        r = int(self.r_entry.get())
        result = math.comb(n, r)
        self.result_label.config(text=f"C({n},{r}) = {result}")

    def solve_linear_2eq(self):
        """Solve a system of 2 linear equations."""
        eq1 = self.eq1_2x2_entry.get()
        eq2 = self.eq2_2x2_entry.get()
        try:
            x, y = symbols('x y')
            equations = [sympify(eq1.replace('=', '-(') + ')'), sympify(eq2.replace('=', '-(') + ')')]
            solutions = solve(equations, (x, y))
            self.result_label.config(text=f"Solutions: x = {solutions[x]}, y = {solutions[y]}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid equation format.")

    def solve_linear_3eq(self):
        """Solve a system of 3 linear equations."""
        eq1 = self.eq1_3x3_entry.get()
        eq2 = self.eq2_3x3_entry.get()
        eq3 = self.eq3_3x3_entry.get()
        try:
            x, y, z = symbols('x y z')
            equations = [sympify(eq1.replace('=', '-(') + ')'), sympify(eq2.replace('=', '-(') + ')'), sympify(eq3.replace('=', '-(') + ')')]
            solutions = solve(equations, (x, y, z))
            self.result_label.config(text=f"Solutions: x = {solutions[x]}, y = {solutions[y]}, z = {solutions[z]}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid equation format.")

    def calculate_factorial(self):
        """Calculate factorial of a number."""
        try:
            number = int(self.factorial_entry.get())
            if number < 0:
                raise ValueError("Negative value")
            result = math.factorial(number)
            self.result_label.config(text=f"{number}! = {result}")
        except Exception:
            messagebox.showerror("Error", "Please enter a non-negative integer.")

    def check_prime(self):
        """Check if a number is prime."""
        try:
            number = int(self.prime_entry.get())
            if number <= 1:
                result = "Not Prime"
            else:
                result = "Prime" if all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)) else "Not Prime"
            self.result_label.config(text=f"{number} is {result}.")
        except Exception:
            messagebox.showerror("Error", "Please enter an integer.")

    def solve_quadratic(self):
        """Solve a quadratic equation."""
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                self.result_label.config(text="No real roots.")
            elif discriminant == 0:
                root = -b / (2*a)
                self.result_label.config(text=f"One root: {root}")
            else:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                self.result_label.config(text=f"Roots: {root1}, {root2}")
        except Exception:
            messagebox.showerror("Error", "Invalid input values.")


    def calculate_determinant_3x3(self):
        """Calculate determinant of a 3x3 matrix."""
        try:
            a11 = float(self.matrix_entries_3x3[0][0].get())
            a12 = float(self.matrix_entries_3x3[0][1].get())
            a13 = float(self.matrix_entries_3x3[0][2].get())
            a21 = float(self.matrix_entries_3x3[1][0].get())
            a22 = float(self.matrix_entries_3x3[1][1].get())
            a23 = float(self.matrix_entries_3x3[1][2].get())
            a31 = float(self.matrix_entries_3x3[2][0].get())
            a32 = float(self.matrix_entries_3x3[2][1].get())
            a33 = float(self.matrix_entries_3x3[2][2].get())

            # Calculate the determinant of the 3x3 matrix
            determinant = (a11 * (a22 * a33 - a23 * a32) -
                        a12 * (a21 * a33 - a23 * a31) +
                        a13 * (a21 * a32 - a22 * a31))
            
            self.result_label.config(text=f"Determinant = {determinant}")
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix format.")


    def calculate_gcd(self):
        """Calculate GCD of two numbers."""
        try:
            num1 = int(self.gcd_lcm_entry1.get())
            num2 = int(self.gcd_lcm_entry2.get())
            result = math.gcd(num1, num2)
            self.result_label.config(text=f"GCD({num1}, {num2}) = {result}")
        except Exception:
            messagebox.showerror("Error", "Please enter valid integers.")

    def calculate_lcm(self):
        """Calculate LCM of two numbers."""
        try:
            num1 = int(self.gcd_lcm_entry1.get())
            num2 = int(self.gcd_lcm_entry2.get())
            result = abs(num1 * num2) // math.gcd(num1, num2)
            self.result_label.config(text=f"LCM({num1}, {num2}) = {result}")
        except Exception:
            messagebox.showerror("Error", "Please enter valid integers.")


    def set_matrices(self):
        """Set the input grids for matrices based on the specified order."""
        try:
            rows_a = int(self.rows_a_entry.get())
            cols_a = int(self.cols_a_entry.get())
            rows_b = int(self.rows_b_entry.get())
            cols_b = int(self.cols_b_entry.get())

            if cols_a != rows_b:
                raise ValueError("Number of columns in Matrix A must be equal to number of rows in Matrix B for multiplication.")

            self.clear_frame()

            tk.Label(self.root, text="Matrix A:", bg="#e0e0e0").grid(row=0, column=0, pady=5, padx=5)
            self.matrix_a_entries = [[tk.Entry(self.root, width=5) for _ in range(cols_a)] for _ in range(rows_a)]
            for i in range(rows_a):
                for j in range(cols_a):
                    self.matrix_a_entries[i][j].grid(row=i+1, column=j, pady=5, padx=5)

            tk.Label(self.root, text="Matrix B:", bg="#e0e0e0").grid(row=0, column=cols_a+1, pady=5, padx=5)
            self.matrix_b_entries = [[tk.Entry(self.root, width=5) for _ in range(cols_b)] for _ in range(rows_b)]
            for i in range(rows_b):
                for j in range(cols_b):
                    self.matrix_b_entries[i][j].grid(row=i+1, column=j+cols_a+1, pady=5, padx=5)

            tk.Button(self.root, text="Calculate", command=self.perform_matrix_multiplication, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=max(rows_a, rows_b)+1, column=0, columnspan=cols_a+cols_b+1, pady=10, padx=10)

            tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
            tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=5, column=1, columnspan=2, pady=5, padx=25)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def perform_matrix_multiplication(self):
        """Perform matrix multiplication and display the result."""
        try:
            matrix_a = Matrix([[int(self.matrix_a_entries[i][j].get()) for j in range(len(self.matrix_a_entries[0]))] for i in range(len(self.matrix_a_entries))])
            matrix_b = Matrix([[int(self.matrix_b_entries[i][j].get()) for j in range(len(self.matrix_b_entries[0]))] for i in range(len(self.matrix_b_entries))])

            result = matrix_a * matrix_b

            # Clear previous result grid if any
            if hasattr(self, 'result_labels'):
                for row in self.result_labels:
                    for label in row:
                        label.destroy()

            # Display "Matrix AB ="
            result_start_row = max(len(self.matrix_a_entries), len(self.matrix_b_entries)) + 10
            tk.Label(self.root, text="Matrix AB =", bg="#e0e0e0").grid(row=result_start_row, column=0, pady=5, padx=5)

            # Display result as a grid
            self.result_labels = []
            for i in range(result.rows):
                row_labels = []
                for j in range(result.cols):
                    label = tk.Label(self.root, text=str(result[i, j]), bg="#e0e0e0", relief="solid", width=5)
                    label.grid(row=i+result_start_row+1, column=j, pady=5, padx=5)
                    row_labels.append(label)
                self.result_labels.append(row_labels)

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input or multiplication error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MathCalculatorApp(root)
    root.mainloop()
