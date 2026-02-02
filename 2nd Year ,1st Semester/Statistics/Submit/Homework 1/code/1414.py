import matplotlib.pyplot as plt
import numpy as np

# Given data from the image
data = [2.9, 7.9, 15.9, 6.2, 0.6, 0.5, 8.8, 6.9, 13.5, 13.7, 9.8, 12.8, 17.1, 11.5, 11.5, 13.7,
        2.8, 2.9, 12.3, 2.7, 3.8, 3.6, 3.7, 3.5, 16.0, 6.1, 8.9, 8.3, 2.1, 8.8, 13.0, 15.9,
        6.4, 2.2, 7.9, 5.1, 17.2, 9.4, 11.7, 6.0]

# Part (a): Stem-and-leaf display
data_sorted = sorted(data)
stem_leaf = {}

for num in data_sorted:
    stem, leaf = divmod(int(num * 10), 10)
    if stem not in stem_leaf:
        stem_leaf[stem] = []
    stem_leaf[stem].append(leaf)

# Print stem-and-leaf display
print("Stem-and-Leaf Display:")
for stem, leaves in stem_leaf.items():
    leaves_str = ' '.join(map(str, leaves))
    print(f"{stem} | {leaves_str}")

# Part (b): Frequency Histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, color='lightblue', edgecolor='black')
plt.title('Frequency Histogram of Radon Concentrations')
plt.xlabel('Radon Concentration (pCi/L)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Part (c): Pie Chart
counts, bins = np.histogram(data, bins=6)
labels = [f"{round(bins[i], 1)}-{round(bins[i+1], 1)}" for i in range(len(bins)-1)]

plt.figure(figsize=(7, 7))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Pie Chart of Radon Concentration Ranges')
plt.show()
