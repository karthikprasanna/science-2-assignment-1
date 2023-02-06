import numpy as np
import matplotlib.pyplot as plt

t = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
y = np.array([1.1, 0.5, 0.0, 0.5, 2.0])

# Find the coefficients of the polynomial p(t) = a3 + a2t + a1t^2 = y
# Also plot the least-squares curve for the data

coefficients = np.polyfit(t, y, 2)

print("The given polynomial is: p(t) = a1t^2 + a2t + a3")
print(f'The coefficients of the polynomial are: a1={coefficients[0]}, a2={coefficients[1]}, a3={coefficients[2]}')

polynomial = np.poly1d(coefficients)
t_left = -1.0
t_right = 1.0
t_new = np.linspace(t_left, t_right, num=100)
y_new = polynomial(t_new)

plt.plot(t, y, '.', t_new, y_new)
plt.xlabel('t')
plt.ylabel('y')
plt.show()
