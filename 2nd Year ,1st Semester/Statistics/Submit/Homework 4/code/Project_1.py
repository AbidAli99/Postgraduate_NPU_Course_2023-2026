import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters of the population
mu = 50  # Population mean
sigma2 = 25  # Population variance
sigma = np.sqrt(sigma2)  # Population standard deviation

# Sample sizes
sample_sizes = [100, 500, 1000]

# To store results
results = []

# Generate samples and calculate statistics
for n in sample_sizes:
    # Generate a normal random sample
    sample = np.random.normal(mu, sigma, n)

    # Calculate statistics
    sample_mean = np.mean(sample)
    sample_median = np.median(sample)
    sample_variance = np.var(sample, ddof=1)  # Sample variance (unbiased)

    # Append results
    results.append({
        "Sample Size": n,
        "Sample Mean": sample_mean,
        "Sample Median": sample_median,
        "Sample Variance": sample_variance
    })

# Convert results to a DataFrame
df_results = pd.DataFrame(results)

# Display the results in a table
print("Sample Statistics Comparison")
print(df_results)

# Plot the sample mean and variance compared to the population
plt.figure(figsize=(12, 6))

# Plot sample mean
plt.subplot(1, 2, 1)
plt.plot(sample_sizes, df_results["Sample Mean"], marker='o', label="Sample Mean")
plt.axhline(y=mu, color='r', linestyle='--', label="Population Mean")
plt.xlabel("Sample Size")
plt.ylabel("Mean")
plt.title("Sample Mean vs Population Mean")
plt.legend()

# Plot sample variance
plt.subplot(1, 2, 2)
plt.plot(sample_sizes, df_results["Sample Variance"], marker='o', label="Sample Variance")
plt.axhline(y=sigma2, color='r', linestyle='--', label="Population Variance")
plt.xlabel("Sample Size")
plt.ylabel("Variance")
plt.title("Sample Variance vs Population Variance")
plt.legend()

plt.tight_layout()
plt.show()
