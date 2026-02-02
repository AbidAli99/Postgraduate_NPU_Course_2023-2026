import matplotlib.pyplot as plt

# Data for the graph from the table
sources = ['Coal', 'Natural gas', 'Nuclear electric ', 'Petroleum', 'Renewable energy']
percentages = [22, 23, 8, 40, 7]

# Part (a): Construct a bar graph
plt.figure(figsize=(8, 5))
plt.bar(sources, percentages, color='skyblue')
plt.title('Energy Consumption by Source in 2007')
plt.ylabel('Percentage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Part (b): Construct a Pareto chart (Bar and cumulative line)
sorted_percentages = sorted(percentages, reverse=True)
sorted_sources = [x for _, x in sorted(zip(percentages, sources), reverse=True)]
cumulative = [sum(sorted_percentages[:i+1]) for i in range(len(sorted_percentages))]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(sorted_sources, sorted_percentages, color='skyblue')
ax.set_ylabel('Percentage')

# Add cumulative line
ax2 = ax.twinx()
ax2.plot(sorted_sources, cumulative, color='red', marker='o', linestyle='dashed')
ax2.set_ylabel('Cumulative Percentage')

plt.title('Pareto Chart of Energy Consumption by Source')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Part (c): Construct a pie chart
plt.figure(figsize=(6, 6))
plt.pie(percentages, labels=sources, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Energy Consumption by Source (Pie Chart)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
