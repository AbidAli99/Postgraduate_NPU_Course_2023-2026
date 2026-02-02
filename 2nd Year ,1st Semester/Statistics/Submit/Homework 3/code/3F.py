import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform, norm, binom, expon

# Set the number of samples
n = 100

# Generate and plot for uniform distribution U(0, 2)
uniform_samples = np.random.uniform(0, 2, n)
sns.histplot(uniform_samples, kde=True, stat="density", bins=10, color="skyblue", label="Histogram")
x = np.linspace(0, 2, 1000)
plt.plot(x, uniform.pdf(x, loc=0, scale=2), 'r-', label="Uniform PDF")
plt.title("Uniform Distribution U(0, 2)")
plt.legend()
plt.show()

# Generate and plot for normal distribution N(4, 2^2)
normal_samples = np.random.normal(4, 2, n)
sns.histplot(normal_samples, kde=True, stat="density", bins=10, color="skyblue", label="Histogram")
x = np.linspace(-2, 10, 1000)
plt.plot(x, norm.pdf(x, loc=4, scale=2), 'r-', label="Normal PDF")
plt.title("Normal Distribution N(4, 2^2)")
plt.legend()
plt.show()

# Generate and plot for binomial distribution Binomial(10, 0.5)
binomial_samples = np.random.binomial(10, 0.5, n)
sns.histplot(binomial_samples, kde=False, stat="density", bins=10, color="skyblue", label="Histogram")
x = np.arange(0, 11)
plt.plot(x, binom.pmf(x, 10, 0.5), 'r-', marker="o", label="Binomial PMF")
plt.title("Binomial Distribution Binomial(10, 0.5)")
plt.legend()
plt.show()

# Generate and plot for exponential distribution Exp(1/1000)
exponential_samples = np.random.exponential(1000, n)
sns.histplot(exponential_samples, kde=True, stat="density", bins=10, color="skyblue", label="Histogram")
x = np.linspace(0, 5000, 1000)
plt.plot(x, expon.pdf(x, scale=1000), 'r-', label="Exponential PDF")
plt.title("Exponential Distribution Exp(1/1000)")
plt.legend()
plt.show()
