import numpy as np
import matplotlib.pyplot as plt

def correlate(M):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if i != j:
                if M[i][j] * M[i][j] > 0:
                    M[i][j] -= 1

def plot_eigenvalues(N, D_values):
    for D in D_values:
        muo = 0
        sigma_square = 1
        M = np.random.normal(muo, sigma_square, (N, N))
        correlate(M)
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