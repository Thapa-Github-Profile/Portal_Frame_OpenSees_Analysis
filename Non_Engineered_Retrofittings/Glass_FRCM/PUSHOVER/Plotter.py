import numpy as np
import matplotlib.pyplot as plt
import csv

reaction_file = 'ReactionsX.out'
disp_file = 'Displacement.out'

# Load reaction and displacement data from files
reactions_data = np.loadtxt(reaction_file)  
displacements_data = np.loadtxt(disp_file)  

# Extract data columns#4,8,12,16,32,28,24,20,
time_displacements = displacements_data[:, 0]
d500 = displacements_data[:, 1]


#1,5,9,13,17,21,25,29,33,36,39,42
time_reactions = reactions_data[:, 0]
r1 = reactions_data[:, 1]
r2 = reactions_data[:, 2]
r3 = reactions_data[:, 3]




# Calculate the sum of reactions for each time step
sum_reactions = -(r1+r2+r3) 
with open('output.txt', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(sum_reactions, d500))

# Plot the sum of reactions and average of displacements
plt.figure(figsize=(10, 6))
plt.plot(d500, sum_reactions)
plt.xlabel('Displacment ')
plt.ylabel('Base Shear (kN)')
plt.title('Pushover Curve for Engineered Building')
plt.grid(True)
plt.legend()
plt.show()
