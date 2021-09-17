import numpy as np
from scipy.stats import iqr

# Taken from https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# This is meant to show the affect of outliers on mean, standard deviation, median, and interquartile range
np.random.seed(10)

mu, sigma = 0, 1  # mean and standard deviation
s = np.random.normal(mu, sigma, 100)

# print(s)
print("Data properties before adding an outlier: ")
print("Mean: " + str(np.mean(s)))
print("Standard Deviation: " + str(np.std(s)))
print("Median: " + str(np.median(s)))
print("Interquartile Range: " + str(iqr(s)))

s = np.append(s, [10000])

print("\n\n")

print("Data properties after adding an outlier: ")
print("Mean: " + str(np.mean(s)))
print("Standard Deviation: " + str(np.std(s)))
print("Median: " + str(np.median(s)))
print("Interquartile Range: " + str(iqr(s)))

exit(0)
