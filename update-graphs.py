"""
Initial idea, best estimates used for scatterplot values.
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





# Creating the scatter plot
plt.xscale('log')
plt.yscale('log')
#plt.scatter(x_values, y_values, c=z_values, cmap='hot')
#plt.scatter(x, z, c=y)
#identity = [10**i for i in range(-7, 0)]
#plt.grid()
#plt.scatter(x, y, c=z, cmap='plasma', s=100)
plt.imshow(np.hstack(x,y), cmap='plasma', interpolation='nearest')
#plt.scatter(x2,x2,c=z2, marker="star")

# Adding a color bar
plt.colorbar(label='Performance gap recovered (%)')

# Adding labels and title
plt.xlabel('Strong Student Compute (fraction of GPT4)')
plt.ylabel('Weak Supervisor Compute (fraction of GPT4)')
plt.title('Chess Puzzles (Figure 3e)')

# Display the plot
plt.show()
