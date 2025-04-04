# NumPy for matrix operations and numerical computations
import numpy as np  

# Encoding matrix A for cipher encryption
A = np.array([
    [1, -1, -1, 1],  
    [2, -3, -5, 4],   
    [-2, -1, -2, 2],   
    [3, -3, -1, 2]    
])

# Read plaintext from 'input-A21-1.txt' file
with open("input-A21-1.txt", "r") as f:
    # Read and remove extra spaces from the plaintext
    plaintext = f.read().strip() 

# Convert each character of plaintext into respective ASCII value
ascii_vals = [ord(c) for c in plaintext]

# Add zeros to ASCII values list so length is multiple of 4
while len(ascii_vals) % 4 != 0:
    # Add zeros to make length multiple of 4
    ascii_vals.append(0)  

# Reshape ASCII values into matrix B with 4 rows,
    # transpose to fit encryption requirements
# Reshape and transpose to create matrix ( 4 * n )
B = np.array(ascii_vals).reshape(-1, 4).T  
print("Plaintext Matrix (B):\n", B)

# Perform encryption: C = A * B (matrix multiplication)
C = A @ B  # Matrix multiplication to encrypt plaintext
# Flatten result for storage
ciphertext = C.flatten(order='F')
print("\nEncrypted Message (Ciphertext):\n", ciphertext.tolist())

# Write encrypted ciphertext to a file ('input-A22-fixed.txt')
with open("input-A22-fixed.txt", "w") as f:
    # Write ciphertext as space-separated values
    f.write(" ".join(map(str, ciphertext)))

# Read the encrypted ciphertext back from 'input-A22-fixed.txt' file
with open("input-A22-fixed.txt", "r") as f:
    # Read and convert the ciphertext back to integers
    c_vals = list(map(int, f.read().strip().split()))

# Reshape ciphertext to matrix C (4 rows, "n" columns)
C = np.array(c_vals).reshape(4, -1, order='F')
print("\nCipher matrix (C):\n", C)

# Decrypt the message: B = A^-1 * C
# Use the inverse of A to decrypt
A_inv = np.linalg.inv(A)  # Compute inverse of matrix A
# Multiply inverse of A with C to get decoded matrix
B_decoded = A_inv @ C
# Round results and convert to integers
B_decoded = np.round(B_decoded).astype(int)
print("\nDecoded matrix (B) after rounding:\n", B_decoded)

# Transpose decoded matrix B to get characters in correct order
B_decoded = B_decoded.T  # Transpose to get original character order
# Convert ASCII values back to characters
decoded_chars = [chr(num) for row in B_decoded for num in row if 0 <= num <= 127]

# Join characters to form decrypted message
decoded_message = ''.join(decoded_chars)
# Display final decrypted message
print("\nDecrypted Message:\n", decoded_message)
