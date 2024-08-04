import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(r':E:\4th year project\opensees\Pushover all typology\Non engineered buildings\Engineered portal framr\Engineered')
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
######Saving in Excel ##############
import pandas as pd
# Your code to load data and calculate sum_reactions
# Create a DataFrame
data = {
    
    'Displacement': d500,
    'Base Shear': sum_reactions
}
df = pd.DataFrame(data)
# Define the output Excel file path
output_excel_file = 'outt.xlsx'
# Export the DataFrame to Excel
df.to_excel(output_excel_file, index=False)
