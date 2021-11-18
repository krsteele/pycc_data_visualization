# Calculating Data Automatically
import matplotlib.pyplot as plt


x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14 )

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
# Saving Your Plots Automatically 
# replace plt.show() with plt.savefig()
# the first arg is the filename, the second trims the extra whitespace from the plot and is optional
# plt.savefig('squares_plot.png', bbox_inches='tight')


# Plotting a Series of Points with scatter()
# import matplotlib.pyplot as plt


# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)

# # set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14 )

# # Set size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()