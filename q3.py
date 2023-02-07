import numpy as np
import matplotlib.pyplot as plt

def plot_eigenvalues(N, D_values):
    for D in D_values:
        muo = 0
        sigma_square = 1
        M = np.random.normal(muo, sigma_square, (N, N))
        D = -D
        np.fill_diagonal(M, D)
        eigenvalues = np.linalg.eigvals(M)
        real_eigenvalues = np.real(eigenvalues)
        imag_eigenvalues = np.imag(eigenvalues)
        plt.scatter(real_eigenvalues, imag_eigenvalues, label=f'D={D}')

N = 500
D_values = [0, 1, 5, 10]
plot_eigenvalues(N, D_values)

plt.xlabel('Real(λ)')
plt.ylabel('Imag(λ)')
plt.legend()
plt.show()