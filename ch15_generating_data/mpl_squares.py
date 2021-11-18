# import the pyplot module and alias it
import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
# create a list to hold the data to plot
squares = [1, 4, 9, 16, 25]

# built-in style
plt.style.use('seaborn')

# subplots() can generate one or more plots in the same figure
# fig represents the entire figure or collection of plots that are generated
# ax represents a single plot in the figure and is the variable we'll use most of the time
fig, ax = plt.subplots()
# the plot() method will try to plot the data it's given in a meaningful way. linewidth controls the thickness of the plot line.
ax.plot(input_values, squares, linewidth=3)

# set chart title and label names
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# this function opens Matplotlib's viewer and displays the plot
plt.show()