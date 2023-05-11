import matplotlib.pyplot as plt
import numpy as np

print("Please input your equation(k*x+d but you will define x in the next step!)")

equation = input()

# 100 linearly spaced numbers
print("Please specify x! If you don´t want to specify it, press enter!")
x = input()

if x == "":
    x = np.linspace(-5,5,100)

# the function, which is y = x^2 here
y = -6/2*x+3

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()