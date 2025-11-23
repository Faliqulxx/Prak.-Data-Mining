import numpy as np  # type: ignore
nim_digits = [0, 3, 1, 1, 1, 8]
matrix_2d = np.array(nim_digits).reshape(2, 3)
print("Matriks 2D:")
print(matrix_2d)

matrix_addition = matrix_2d + 5  
matrix_subtraction = matrix_2d - 2  
matrix_multiplication = matrix_2d * 3  
print("\nHasil Pertambahan:")
print(matrix_addition)
print("\nHasil Pengurangan:")
print(matrix_subtraction)
print("\nHasil Perkalian:")
print(matrix_multiplication)

matrix_1d = matrix_2d.flatten()
print("\nMatriks dalam bentuk 1D:")
print(matrix_1d)

sliced_matrix = matrix_2d[0, :] 
print("\nHasil Slicing:")
print(sliced_matrix)
