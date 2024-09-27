import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Your dataset
data = [7, 10, 12, 4, 8, 7, 3, 8, 5, 12, 11, 3, 8, 1, 1, 13, 10, 4, 4, 5, 5, 8, 7, 7, 3, 2, 3, 8, 13, 1, 7, 17, 3, 4, 5, 5, 3, 1, 17, 10, 4, 7, 7, 11, 8]

# Calculate sample mean and standard deviation
sample_mean = np.mean(data)
sample_std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
population_std_dev = np.std(data)  # ddof=0 (default) for population standard deviation

# Plot histogram
plt.hist(data, bins=10, density=True, alpha=0.6, color='g')

# Plot the sample mean and sample standard deviation as a normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, sample_mean, sample_std_dev)
plt.plot(x, p, 'k', linewidth=2, label='Sample Mean & Std Dev')

# Plot the population standard deviation as a normal distribution curve
p_pop = norm.pdf(x, sample_mean, population_std_dev)
plt.plot(x, p_pop, 'r--', linewidth=2, label='Population Std Dev')

title = f"Fit results:\nSample Mean = {sample_mean:.2f}, Sample Std Dev = {sample_std_dev:.2f}\nPopulation Std Dev = {population_std_dev:.2f}"
plt.title(title)
plt.xlabel('Hours of sleep after anesthesia')
plt.ylabel('Density')
plt.legend()

# Show plot
plt.show()
