import numpy as np

# Macierz współczynników A
A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 2, 4]])

# Wektor wyników B
B = np.array([1, 2, 3])

# Rozwiązanie układu równań za pomocą funkcji linalg.solve
x = np.linalg.solve(A, B)

print("Rozwiązanie układu równań (x, y, z):", x)

# Weryfikacja: mnożenie macierzy A i wektora x powinno dać B
B_check = np.dot(A, x)
print("Weryfikacja (A * x):", B_check)
