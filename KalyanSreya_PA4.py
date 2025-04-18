# Import NumPy for matrix operations
import numpy as np

# To read input-output matrix D and external demand matrix E from input file
def read_file(filename):
    with open(filename, 'r') as f:
        # Read all lines from file, remove extra blank lines/spaces
        lines = [line.strip() for line in f.readlines() if line.strip()]
        # To store 3x3 input-output matrix
        D = []
        for i in range(3):
            # Each of first 3 lines contains one row of D
            D.append(list(map(float, lines[i].split())))
        # To store 3x1 external demand matrix
        E = []
        for i in range(3, 6):
            # Each of the next 3 lines contains one number from E
            E.append([float(lines[i])])

        # Return both matrices as NumPy arrays
        return np.array(D), np.array(E)

# To calculate output matrix X using formula X = (I - D)^(-1) * E
def compute_output(D, E):
    # Create 3x3 identity matrix
    I = np.identity(3)
    try:
        # Subtract D from I, and then find inverse of  result
        inverse = np.linalg.inv(I - D)
        # Multiply inverse matrix by E to get X
        X = np.dot(inverse, E)
        # Round result to one decimal place
        return np.round(X, 1)
    except np.linalg.LinAlgError:
        # This will happen if matrix (I - D) can't be inverted (not valid for solving)
        print("Matrix (I - D) is singular and cannot be inverted.")
        return None

# To run program
if __name__ == "__main__":
    # Name of input file that contains matrices
    input_file = "input.txt"
    # Read D and E matrices from file
    D, E = read_file(input_file)
    # Calculate output matrix X
    X = compute_output(D, E)
    # If X calculation was successful, print result
    if X is not None:
        print("Output matrix X (rounded to the nearest tenth):")
        print(X)