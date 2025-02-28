# Importing Numpy: numerical operations, array manipulations
import numpy as np
# Importing Sympy functions: symbolic math
from sympy import Matrix, symbols, Eq, solve

# Define variables for system of equations
x1, x2, x3, x4, x5, x6 = symbols("x1 x2 x3 x4 x5 x6")

# Define system of linear equations w/ expressions
equations = [
    Eq(x1 - x2, 100),  # x1 - x2 = 100
    Eq(x2 - x3, -50),  # x2 - x3 = -50
    Eq(x3 - x4, 120),  # x3 - x4 = 120
    Eq(x4 - x5, 150),  # x4 - x5 = 150
    Eq(x5 - x6, 80),   # x5 - x6 = 80
]

# Display system of linear equations
print("System of Linear Equations:")
for eq in equations:
    print(eq)

# Create coefficient matrix A w/ system of linear equations
A = np.array([
    [1, -1,  0,  0,  0,  0],  # Coefficients for x1 - x2 = 100
    [0,  1, -1,  0,  0,  0],  # x2 - x3 = -50
    [0,  0,  1, -1,  0,  0],  # x3 - x4 = 120
    [0,  0,  0,  1, -1,  0],  # x4 - x5 = 150
    [0,  0,  0,  0,  1, -1],  # x5 - x6 = 80
], dtype=float)

# Create vector B constants w/ other side of the equations
B = np.array([100, -50, 120, 150, 80], dtype=float)

# Construct augmented matrix by combining matrix A coefficent w/ vector B constants
augmented_matrix = Matrix(np.column_stack((A, B)))

# Find  Row-Reduced Echelon Form of augmented matrix and get pivot positions
rref_matrix, pivots = augmented_matrix.rref()

# Display RREF of augmented matrix
print("\nRow-Reduced Echelon Form of Augmented Matrix:")
print(rref_matrix)

# Solve system of linear equations using the Sympy solver
solution = solve(equations, (x1, x2, x3, x4, x5, x6))

# Display general solution
print("\nGeneral Solution for Traffic Flow:")
print(solution)

# Adjust x6 w/ condition x5 = 1000 and compute specific value for x6
x6_value = 1000 - 80  # Basically: x6 = x5 - 80

# Substitute x6 specific value in general solution
solution_specific = {var: expr.subs(x6, x6_value) for var, expr in solution.items()}

# Display specific solution when x5 = 1000 and x6 = 0
print("\nSpecific Solution when x5 = 1000 and x6 = 0:")
print(solution_specific)