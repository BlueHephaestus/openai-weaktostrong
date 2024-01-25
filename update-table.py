"""
Updated idea, using tables with colorcoding to indicate values, since x and ys seemed to be following a
triangular pattern.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1e-6,   8e-6, 8e-5, 8e-4, 7e-3, 2e-2, 1,
              8e-6, 8e-5, 8e-4, 7e-3, 2e-2, 1,
              8e-5, 8e-4, 7e-3, 2e-2, 1,
              8e-4, 7e-3, 2e-2, 1,
              7e-3, 2e-2, 1,
              2e-2, 1,
              1])

y = np.array([1e-6]*7 + [1e-5]*6 + [1e-4]*5 + [1e-3]*4 + [1e-2]*3 + [1e-1]*2 + [1])
z = np.array([-20, 0, 8, 4, 5, 2, 2,
              0, 23, 12, 12, 8, 8,
              40, 25, 25, 20, 12,
              45, 42, 37, 22,
              60, 50, 30,
              72, 34,
              41])

#xtx = [1e-6,   8e-6, 8e-5, 8e-4, 7e-3, 2e-2, 1]
xtx = ["1e-6", "8e-6", "8e-5", "8e-4", "7e-3", "2e-2", "1"]
#ytx = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
ytx = ["1e-6", "1e-5", "1e-4", "1e-3", "1e-2", "1e-1", "1"]

n = len(x)

# Create the table with color mapping
fig, ax = plt.subplots()

# Create the 2D array of values
XY = np.full((7,7), np.nan)

# this will only be upper triangular so we stop inserting values after we exhaust them, and leave as nans.
triu = np.triu_indices(7)

XY[triu] = z
for (i,j) in zip(triu[0], triu[1]):
    ax.text(j, i, f'{XY[i,j]}', ha='center', va='center', color='black', fontsize=12)

cax = ax.matshow(XY, cmap='viridis', origin='lower')
ax.xaxis.set_ticks_position('bottom')
plt.xticks(np.arange(7), xtx)
plt.yticks(np.arange(7), ytx)

# Add a colorbar to indicate accuracies
cbar = fig.colorbar(cax)
# label colorbar
cbar.ax.set_ylabel('Accuracy(%)', rotation=-90, va="bottom")

# Set labels and title
plt.xlabel('Strong Student Compute (fraction of GPT4)')
plt.ylabel('Weak Supervisor Compute (fraction of GPT4)')
plt.title('Chess Puzzles (Figure 3e)')

# Show the plot
plt.show()
