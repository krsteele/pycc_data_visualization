import matplotlib.pyplot as plt


x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)

# set chart title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# range for each axis
ax.axis([0, 5000, 0, 1.25e11])

# plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')