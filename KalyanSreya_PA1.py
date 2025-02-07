# Import Numpy for all the matrix calculations
import numpy as np

def get_matrix(rows, cols):
    # Function to get matrix input from user
    print(f"Enter the elements of a {rows}x{cols} matrix row by row, with a space in"
          f" between each number, use the Enter key to continue entering until you "
          f"have reached the specified limit:")
    matrix = [] # Empty matrix to store user input
    for i in range(rows):
        # Read + convert input into a list
        row = list(map(int, input().split()))
        # Ensure that user enters the correct number of elements for each row
        while len(row) != cols:
            print(f"Invalid row length. Please enter {cols} numbers.")
            row = list(map(int, input().split()))
        # Append inputted row into matrix
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    # Display a matrix
    for row in matrix:
        # WIll print each row as a string with spaces in between
        print(" ".join(map(str, row)))
    print()

def main():
    while True:
        # Printing the menu options
        print("\nMatrix Operations Menu:")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Scalar Multiplication")
        print("4. Exit")
        # Read user input choice
        choice = input("Select an operation to do (1-4): ")

        # If the user chooses Addition or Subtraction
        if choice == '1' or choice == '2':
            # Ask user for matrix dimensions
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            # Ask user for matrix values and store them
            print("Enter first matrix:")
            A = get_matrix(rows, cols)
            print("Enter second matrix:")
            B = get_matrix(rows, cols)

            # Do the specified operation
            if choice == '1':
                print("NumPy Addition Result:")
                # Use the Numpy addition function
                display_matrix(np.add(A, B))
            else:
                print("NumPy Subtraction Result:")
                # Use the Numpy subtraction function
                display_matrix(np.subtract(A, B))

        # If the user chooses Multiplication
        elif choice == '3':
            # Get matrix dimensions
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            # Store the entire matrix after getting user input for values
            A = get_matrix(rows, cols)
            # Ask the user for the scalar value they want to user for multiplication
            scalar = int(input("Enter scalar value: "))
            print("NumPy Scalar Multiplication Result:")
            # Use Numpy, perform calulations, and display it
            display_matrix(np.multiply(A, scalar))

        # If user choose to Exit
        elif choice == '4':
            print("Exiting program.")
            # Break the loop, end the programme
            break
        else:
            # If invalid choice given, loop repeats question
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()