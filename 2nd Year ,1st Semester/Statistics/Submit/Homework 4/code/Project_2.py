import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters of the population
mu = 50  # Population mean
sigma2 = 25  # Population variance
sigma = np.sqrt(sigma2)  # Population standard deviation
sample_size = 15  # Sample size
num_samples = 10000  # Number of samples

# Generate 10,000 samples, each of size 15
sample_means = []
for _ in range(num_samples):
    sample = np.random.normal(mu, sigma, sample_size)
    sample_means.append(np.mean(sample))

# Convert sample means to a NumPy array
sample_means = np.array(sample_means)

# Compute the parameters of the sampling distribution of the sample mean
sampling_sigma = sigma / np.sqrt(sample_size)  # Standard deviation of the sampling distribution

# Plot histogram of sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='blue', label='Histogram of Sample Means')

# Plot theoretical normal distribution
x = np.linspace(mu - 4 * sampling_sigma, mu + 4 * sampling_sigma, 1000)
theoretical_pdf = norm.pdf(x, loc=mu, scale=sampling_sigma)
plt.plot(x, theoretical_pdf, 'r-', label='Theoretical PDF ($N(\\mu, \\sigma^2/15)$)')

# Add labels and legend
plt.title('Sampling Distribution of the Sample Mean (n=15)')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()
