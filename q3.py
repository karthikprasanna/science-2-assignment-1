import numpy as np
import matplotlib.pyplot as plt

N = 500
D_values = [0, 1, 5, 10]

for D in D_values:
    M = np.random.normal(0, 1, (N, N))
    np.fill_diagonal(M, -D)
    eigenvalues = np.linalg.eigvals(M)
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues), label=f'D={D}')

plt.xlabel('Real(λ)')
plt.ylabel('Imag(λ)')
plt.legend()
plt.show()
