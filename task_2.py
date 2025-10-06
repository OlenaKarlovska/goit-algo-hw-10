import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2
a, b = 0, 2

# --- Метод Монте-Карло ---
def monte_carlo_integral(f, a, b, n=1000000):
    x_rand = np.random.uniform(a, b, n)
    y_rand = f(x_rand)
    mean_value = np.mean(y_rand)
    return (b - a) * mean_value

# --- Аналітичний результат ---
analytic_result = (b**3 - a**3) / 3
quad_result, quad_error = spi.quad(f, a, b)
mc_result = monte_carlo_integral(f, a, b, n=1000000)
print(f"Метод Монте-Карло: {mc_result:.6f}")
print(f"Аналітичний результат: {analytic_result:.6f}")
print(f"SciPy quad: {quad_result:.6f}, похибка {quad_error:.2e}")

# --- Візуалізація ---
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Інтеграл f(x) = x^2 методом Монте-Карло')
plt.grid()
plt.show()