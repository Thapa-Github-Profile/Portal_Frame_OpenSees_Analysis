import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image



os.chdir(r"E:\4th year project\opensees\Pushover all typology\portal frame fragility curve all")

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'portal frame pushover.xlsx'

# Create an instance of PdfPages
pdf_pages = PdfPages('Pushovergraph.pdf')

# Read Excel file
data = pd.read_excel(file_path)

# Initialize empty lists to store data from each column
Displacement = []
eng = []
noneng = []
preeng = []
Rcret = []
Steelret = []
GFRCMret = []
HEMPret = []
FRPret=[]

PRCret = []
PSteelret = []
PGFRCMret = []
PHEMPret= []
PFRPret = []

# Define the range you want to include in the lists
num_rows= 3000

# Iterate over each column and store the values in the respective lists
for column in data.columns:
    if column == 'Displacement ':
        Displacement = data[column].head(num_rows).tolist()
    elif column == 'Engineered':
        eng = data[column].head(num_rows).tolist()
    elif column == 'Non-Engineered':
        noneng = data[column].head(num_rows).tolist()
    elif column == 'Pre-Engineered':
        preeng = data[column].head(num_rows).tolist() 
    elif column == 'RCNon':
        Rcret = data[column].head(num_rows).tolist()
    elif column == 'steelnon':
        Steelret = data[column].head(num_rows).tolist()
    elif column == 'GFRCMNon':
        GFRCMret = data[column].head(num_rows).tolist()
    elif column == 'HEMP non':
       HEMPret = data[column].head(num_rows).tolist()
    elif column == 'FRP Non':
       FRPret = data[column].head(num_rows).tolist()
    elif column == 'Pre Rc':
       PRCret = data[column].head(num_rows).tolist()
    elif column == 'Pre steel':
       PSteelret = data[column].head(num_rows).tolist()
    elif column == 'Pre HEMP':
       PHEMPret = data[column].head(num_rows).tolist()
    elif column == 'Pre GFRCM':
       PGFRCMret = data[column].head(num_rows).tolist()
    elif column == 'pre FRP':
       PFRPret = data[column].head(num_rows).tolist()
       
print(f'length of rc={len(Displacement)}')
print(f'length of rc={len(eng)}')
print(f'length of rc={len(noneng)}')
print(f'length of rc={len(preeng)}')
print(f'length of rc={len(Rcret)}')
print(f'length of rc={len(Steelret)}')
print(f'length of rc={len(GFRCMret)}')
print(f'length of rc={len(HEMPret)}')
print(f'length of rc={len(FRPret)}')
print(f'length of rc={len(PRCret)}')
print(f'length of rc={len(PSteelret)}')
print(f'length of rc={len(PHEMPret)}')
print(f'length of rc={len(PGFRCMret)}')
print(f'length of rc={len(PFRPret)}')



##########Comparing pushover of all three typology###########
fig = plt.figure()
plt.plot(Displacement, eng, 'b', label='Engineered')
plt.plot(Displacement, preeng, 'brown', label='Pre-Engineered')
plt.plot(Displacement, noneng, 'r', label='Non-Engineered')
plt.xlabel('Displacement (m)')  
plt.ylabel('Base Shear (kN)')
plt.legend()
plt.grid(True)
# Create a twin y-axis to plot Base Shear Coefficient without plotting
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.set_ylabel('Base Shear Coefficient (%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
y_min= 0
y_max =200
ax1.set_ylim(y_min,y_max)
ax2.set_ylim(y_min, y_max)
# Customize the x-axis for Drift
yticks = np.linspace(y_min, y_max, num=9)
# yticks = ax1.get_yticks()
ax2.set_yticks(yticks)
ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
ax3 = ax1.twiny()
ax3.set_xlabel('Drift(%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
x_min= 0
x_max =0.3
ax1.set_xlim(x_min,x_max)
ax3.set_xlim(x_min, x_max)
# Customize the y-axis for base shear coefficient
xticks = np.linspace(x_min, x_max, num=7)
# yticks = ax1.get_yticks()
ax1.set_xticks(xticks)
ax3.set_xticks(xticks)
ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])

plt.title('Pushover Curve')

# Load the image
image_path = 'modal.png'
image = Image.open(image_path)

# Convert the image to an OffsetImage
imagebox = OffsetImage(image, zoom=0.2)  # Adjust zoom as needed

# Set the position of the image
xy = (0.18, 0.85)  # Position in data coordinates
ab = AnnotationBbox(imagebox, xy, xycoords='axes fraction', frameon=False)

# Add the image to the plot
ax1.add_artist(ab)



# pdf_pages.savefig()  # Save the current figure to the PDF
# plt.close()
plt.show()




# # Plotting RC Jacketing

# plt.figure()
# plt.plot(Displacement, eng, 'b', label='Engineered')
# plt.plot(Displacement, noneng, 'r', label='Non-Engineered')
# plt.plot(Displacement, Rcret, 'g', label='RC Jacketing')
# plt.xlabel('Displacement (m)')  
# plt.ylabel('Base Shear (kN)')
# plt.legend()
# plt.grid(True)
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.set_ylabel('Base Shear Coefficient (%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# y_min= 0
# y_max =200
# ax1.set_ylim(y_min,y_max)
# ax2.set_ylim(y_min, y_max)
# # Customize the x-axis for Drift
# yticks = np.linspace(y_min, y_max, num=9)
# # yticks = ax1.get_yticks()
# ax2.set_yticks(yticks)
# ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# # ax1 = plt.gca()
# ax3 = ax1.twiny()
# ax3.set_xlabel('Drift(%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# x_min= 0
# x_max =0.3
# ax1.set_xlim(x_min,x_max)
# ax3.set_xlim(x_min, x_max)
# # Customize the y-axis for base shear coefficient
# xticks = np.linspace(x_min, x_max, num=7)
# # yticks = ax1.get_yticks()
# ax1.set_xticks(xticks)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
# plt.title('Pushover Curve')

# # pdf_pages.savefig()  # Save the current figure to the PDF
# # plt.close()
# plt.show()

# # Plotting steel jacketing
# plt.figure()
# plt.plot(Displacement, eng, 'b', label='Engineered')
# plt.plot(Displacement, noneng, 'r', label='Non-Engineered')
# plt.plot(Displacement, Steelret, 'g', label='Steel Jacketing')
# plt.xlabel('Displacement (m)')
# plt.ylabel('Base Shear (kN)')
# plt.legend()
# plt.grid(True)
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.set_ylabel('Base Shear Coefficient (%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# y_min= 0
# y_max =200
# ax1.set_ylim(y_min,y_max)
# ax2.set_ylim(y_min, y_max)
# # Customize the x-axis for Drift
# yticks = np.linspace(y_min, y_max, num=9)
# # yticks = ax1.get_yticks()
# ax2.set_yticks(yticks)
# ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# # ax1 = plt.gca()
# ax3 = ax1.twiny()
# ax3.set_xlabel('Drift(%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# x_min= 0
# x_max =0.3
# ax1.set_xlim(x_min,x_max)
# ax3.set_xlim(x_min, x_max)
# # Customize the y-axis for base shear coefficient
# xticks = np.linspace(x_min, x_max, num=7)
# # yticks = ax1.get_yticks()
# ax1.set_xticks(xticks)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
# plt.title('Pushover Curve')
# plt.show()


# ############ GFRCM ############
# # #Plotting
    

# plt.figure()
# plt.plot(Displacement, eng, 'b', label='Engineered')
# plt.plot(Displacement, noneng, 'r', label='Non-Engineered')
# plt.plot(Displacement, GFRCMret ,'g', label='GFRCM Jacketing')
# plt.xlabel('Displacement (m)')  
# plt.ylabel('Base Shear (kN)')
# plt.legend()
# plt.grid(True)
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.set_ylabel('Base Shear Coefficient (%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# y_min= 0
# y_max =200
# ax1.set_ylim(y_min,y_max)
# ax2.set_ylim(y_min, y_max)
# # Customize the x-axis for Drift
# yticks = np.linspace(y_min, y_max, num=9)
# # yticks = ax1.get_yticks()
# ax2.set_yticks(yticks)
# ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# # ax1 = plt.gca()
# ax3 = ax1.twiny()
# ax3.set_xlabel('Drift(%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# x_min= 0
# x_max =0.3
# ax1.set_xlim(x_min,x_max)
# ax3.set_xlim(x_min, x_max)
# # Customize the y-axis for base shear coefficient
# xticks = np.linspace(x_min, x_max, num=7)
# # yticks = ax1.get_yticks()
# ax1.set_xticks(xticks)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
# plt.title('Pushover Curve')
# plt.show()
# # Potting HEMP Jaketing


# plt.figure()
# plt.plot(Displacement, eng, 'b', label='Engineered')
# plt.plot(Displacement, noneng, 'r', label='Non-Engineered')
# plt.plot(Displacement, HEMPret, 'g', label='HEMP Jacketing')
# plt.xlabel('Displacement (m)')  
# plt.ylabel('Base Shear (kN)')
# plt.legend()
# plt.grid(True)
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.set_ylabel('Base Shear Coefficient (%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# y_min= 0
# y_max =200
# ax1.set_ylim(y_min,y_max)
# ax2.set_ylim(y_min, y_max)
# # Customize the x-axis for Drift
# yticks = np.linspace(y_min, y_max, num=9)
# # yticks = ax1.get_yticks()
# ax2.set_yticks(yticks)
# ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# # ax1 = plt.gca()
# ax3 = ax1.twiny()
# ax3.set_xlabel('Drift(%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# x_min= 0
# x_max =0.3
# ax1.set_xlim(x_min,x_max)
# ax3.set_xlim(x_min, x_max)
# # Customize the y-axis for base shear coefficient
# xticks = np.linspace(x_min, x_max, num=7)
# # yticks = ax1.get_yticks()
# ax1.set_xticks(xticks)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
# plt.title('Pushover Curve')
# plt.show()


# # Potting FRP retrofitting for non enginneered


# plt.figure()
# plt.plot(Displacement, eng, 'b', label='Engineered')
# plt.plot(Displacement, noneng, 'r', label='Non-Engineered')
# plt.plot(Displacement, FRPret, 'g', label='FRP Jacketing')
# plt.xlabel('Displacement (m)')  
# plt.ylabel('Base Shear (kN)')
# plt.legend()
# plt.grid(True)
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.set_ylabel('Base Shear Coefficient (%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# y_min= 0
# y_max =200
# ax1.set_ylim(y_min,y_max)
# ax2.set_ylim(y_min, y_max)
# # Customize the x-axis for Drift
# yticks = np.linspace(y_min, y_max, num=9)
# # yticks = ax1.get_yticks()
# ax2.set_yticks(yticks)
# ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# # ax1 = plt.gca()
# ax3 = ax1.twiny()
# ax3.set_xlabel('Drift(%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# x_min= 0
# x_max =0.3
# ax1.set_xlim(x_min,x_max)
# ax3.set_xlim(x_min, x_max)
# # Customize the y-axis for base shear coefficient
# xticks = np.linspace(x_min, x_max, num=7)
# # yticks = ax1.get_yticks()
# ax1.set_xticks(xticks)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
# plt.title('Pushover Curve')
# plt.show()
# ##############Pre engineered########

# # Potting RC Jacketing
# plt.figure()
# plt.plot(Displacement, eng, 'b', label='Engineered')
# plt.plot(Displacement, preeng, 'r', label='Pre-Engineered')
# plt.plot(Displacement, PRCret, 'g', label='RC Jacketing')
# plt.xlabel('Displacement (m)')  
# plt.ylabel('Base Shear (kN)')
# plt.legend()
# plt.grid(True)
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.set_ylabel('Base Shear Coefficient (%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# y_min= 0
# y_max =200
# ax1.set_ylim(y_min,y_max)
# ax2.set_ylim(y_min, y_max)
# # Customize the x-axis for Drift
# yticks = np.linspace(y_min, y_max, num=9)
# # yticks = ax1.get_yticks()
# ax2.set_yticks(yticks)
# ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# # Create a twin y-axis to plot Base Shear Coefficient without plotting
# # ax1 = plt.gca()
# ax3 = ax1.twiny()
# ax3.set_xlabel('Drift(%)')
# # Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
# x_min= 0
# x_max =0.3
# ax1.set_xlim(x_min,x_max)
# ax3.set_xlim(x_min, x_max)
# # Customize the y-axis for base shear coefficient
# xticks = np.linspace(x_min, x_max, num=7)
# # yticks = ax1.get_yticks()
# ax1.set_xticks(xticks)
# ax3.set_xticks(xticks)
# ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
# plt.title('Pushover Curve')
# plt.show()


# Potting steel jacketing
plt.figure()
plt.plot(Displacement, eng, 'b', label='Engineered')
plt.plot(Displacement, preeng, 'r', label='Pre-Engineered')
plt.plot(Displacement, PSteelret, 'g', label='Steel Jacketing')
plt.xlabel('Displacement (m)')
plt.ylabel('Base Shear (kN)')
plt.legend()
plt.grid(True)
# Create a twin y-axis to plot Base Shear Coefficient without plotting
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.set_ylabel('Base Shear Coefficient (%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
y_min= 0
y_max =200
ax1.set_ylim(y_min,y_max)
# Customize the x-axis for Drift
yticks = np.linspace(y_min, y_max, num=9)
ax1.set_yticks(yticks)
ax1.set_yticklabels([f'{yt:.0f}' for yt in yticks])
ax2.set_ylim(y_min, y_max)

# yticks = ax1.get_yticks()
ax2.set_yticks(yticks)
ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
ax3 = ax1.twiny()
ax3.set_xlabel('Drift(%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
x_min= 0
x_max =0.3
ax1.set_xlim(x_min,x_max)
ax3.set_xlim(x_min, x_max)
# Customize the y-axis for base shear coefficient
xticks = np.linspace(x_min, x_max, num=7)
# yticks = ax1.get_yticks()
ax1.set_xticks(xticks)
ax3.set_xticks(xticks)
ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
plt.title('Pushover Curve')
plt.show()

############ GFRCM ############

# Potting
plt.figure()
plt.plot(Displacement, eng, 'b', label='Engineered')
plt.plot(Displacement, preeng, 'r', label='Pre-Engineered')
plt.plot(Displacement, PGFRCMret ,'g', label='GFRCM Jacketing')
plt.xlabel('Displacement (m)')  
plt.ylabel('Base Shear (kN)')
plt.legend()
plt.grid(True)
# Create a twin y-axis to plot Base Shear Coefficient without plotting
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.set_ylabel('Base Shear Coefficient (%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
y_min= 0
y_max =200
ax1.set_ylim(y_min,y_max)
ax2.set_ylim(y_min, y_max)
# Customize the x-axis for Drift
yticks = np.linspace(y_min, y_max, num=9)
# yticks = ax1.get_yticks()
ax2.set_yticks(yticks)
ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
ax3 = ax1.twiny()
ax3.set_xlabel('Drift(%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
x_min= 0
x_max =0.3
ax1.set_xlim(x_min,x_max)
ax3.set_xlim(x_min, x_max)
# Customize the y-axis for base shear coefficient
xticks = np.linspace(x_min, x_max, num=7)
# yticks = ax1.get_yticks()
ax1.set_xticks(xticks)
ax3.set_xticks(xticks)
ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
plt.title('Pushover Curve')
plt.show()

# Potting HEMP Jaketing

plt.figure()
plt.plot(Displacement, eng, 'b', label='Engineered')
plt.plot(Displacement, preeng, 'r', label='Pre-Engineered')
plt.plot(Displacement, PHEMPret, 'g', label='HEMP Jacketing')
plt.xlabel('Displacement (m)')  
plt.ylabel('Base Shear (kN)')
plt.legend()
plt.grid(True)
# Create a twin y-axis to plot Base Shear Coefficient without plotting
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.set_ylabel('Base Shear Coefficient (%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
y_min= 0
y_max =200
ax1.set_ylim(y_min,y_max)
ax2.set_ylim(y_min, y_max)
# Customize the x-axis for Drift
yticks = np.linspace(y_min, y_max, num=9)
# yticks = ax1.get_yticks()
ax2.set_yticks(yticks)
ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
ax3 = ax1.twiny()
ax3.set_xlabel('Drift(%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
x_min= 0
x_max =0.3
ax1.set_xlim(x_min,x_max)
ax3.set_xlim(x_min, x_max)
# Customize the y-axis for base shear coefficient
xticks = np.linspace(x_min, x_max, num=7)
# yticks = ax1.get_yticks()
ax1.set_xticks(xticks)
ax3.set_xticks(xticks)
ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
plt.title('Pushover Curve')
plt.show()


# Plotting FRP retrofitting for pre enginneered
plt.figure()
plt.plot(Displacement, eng, 'b', label='Engineered')
plt.plot(Displacement, preeng, 'r', label='Pre-Engineered')
plt.plot(Displacement, PFRPret, 'g', label='FRP Jacketing')
plt.xlabel('Displacement (m)')  
plt.ylabel('Base Shear (kN)')
plt.legend()
plt.grid(True)
# Create a twin y-axis to plot Base Shear Coefficient without plotting
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.set_ylabel('Base Shear Coefficient (%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
y_min= 0
y_max =200
ax1.set_ylim(y_min,y_max)
ax2.set_ylim(y_min, y_max)
# Customize the x-axis for Drift
yticks = np.linspace(y_min, y_max, num=9)
# yticks = ax1.get_yticks()
ax2.set_yticks(yticks)
ax2.set_yticklabels([f'{yt / 600:.2f}' for yt in yticks])
# Create a twin y-axis to plot Base Shear Coefficient without plotting
# ax1 = plt.gca()
ax3 = ax1.twiny()
ax3.set_xlabel('Drift(%)')
# Calculate and set the same y-limits and y-ticks for both axes to ensure alignment
x_min= 0
x_max =0.3
ax1.set_xlim(x_min,x_max)
ax3.set_xlim(x_min, x_max)
# Customize the y-axis for base shear coefficient
xticks = np.linspace(x_min, x_max, num=7)
# yticks = ax1.get_yticks()
ax1.set_xticks(xticks)
ax3.set_xticks(xticks)
ax3.set_xticklabels([f'{xt*12:.2f}' for xt in xticks])
plt.title('Pushover Curve')
plt.show()
