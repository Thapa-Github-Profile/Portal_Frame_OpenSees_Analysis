import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
import pandas as pd
os.chdir(r"E:\4th year project\opensees\Pushover all typology\portal frame fragility curve all\FRagility\CP")

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'pushover and fragility.xlsx'

# Read Excel file
data = pd.read_excel(file_path)

# Initialize empty lists to store data from each column
Pga = []
eng = []
noneng = []
preeng = []
Rcret = []
Steelret = []
FRPret=[]
GFRCMret = []
HEMPret= []
PRCret = []
PSteelret = []
PGFRCMret = []
PHEMPret = []
PFRPret= []

# Iterate over each column and store the values in the respective lists
for column in data.columns:
    if column == 'PGA':
        Pga = data[column].tolist()
    elif column == 'Engineered':
        eng = data[column].tolist()
    elif column == 'Non-Engineered':
        noneng = data[column].tolist()
    elif column == 'Pre-Engineered':
        preeng = data[column].tolist()    
    elif column == ' RC_Retrofitted':
        Rcret = data[column].tolist()
    elif column == 'Steel_Retrofitted':
        Steelret = data[column].tolist()
    elif column == 'PRC_Retrofitted':
       PRCret = data[column].tolist()
    elif column == 'PSteel_Retrofitted':
       PSteelret = data[column].tolist()
    elif column == 'GFRCM_Retrofitted':
       GFRCMret= data[column].tolist()
    elif column == 'HEMP_Retrofitted':
        HEMPret = data[column].tolist()
    elif column == 'PGFRCM_Retrofitted':
        PGFRCMret = data[column].tolist()
    elif column == 'PHEMP_Retrofitted':
        PHEMPret= data[column].tolist()
    elif column == 'FRP_Retrofitted':
        FRPret = data[column].tolist()
    elif column == 'PFRP_Retrofitted':
        PFRPret = data[column].tolist()   
    
    

print(f'length of rc2={len(noneng)}')
print(f'length of rc3={len(eng)}')
print(f'length of rc3={len(preeng)}')
print(f'length of rc4={len(Rcret)}')
print(f'length of rc5={len(PSteelret)}')
print(f'length of rc6={len(FRPret)}')
print(f'length of rc7={len(GFRCMret)}')
print(f'length of rc8={len(HEMPret)}')
print(f'length of rc9={len(PRCret)}')
print(f'length of rc11={len(PHEMPret)}')
print(f'length of rc12={len(PGFRCMret)}')


######### for Non engineered################
fig, axs= plt.subplots(2, 3, figsize=(15, 10))
######     RC retrofitted fragility################

axs[0,0].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[0,0].plot(Pga, noneng, '-', markersize=5, label='Non-Engineered - CP', color='Red')
axs[0,0].plot(Pga, Rcret, '-', markersize=5, label='RC-Retrofitted - CP', color='green')
axs[0,0].set_xlabel('PGA (g)', fontsize=1)
axs[0,0].set_ylabel('Probability of exceedence', fontsize=1)
axs[0,0].legend(loc='lower right')
axs[0,0].grid(True, linestyle='--', alpha=0.7)
axs[0,0].set_title('Collapse Prevention', fontsize=10)

############### Steel Jacketing #######

axs[0,1].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[0,1].plot(Pga, noneng, '-', markersize=5, label='Non-Engineered - CP', color='Red')
axs[0,1].plot(Pga, Steelret, '-', markersize=5, label='Steel-Retrofitted - CP', color='green')
axs[0,1].set_xlabel('PGA (g)', fontsize=10)
axs[0,1].set_ylabel('Probability of exceedence', fontsize=10)
axs[0,1].legend(loc='lower right')
axs[0,1].grid(True, linestyle='--', alpha=0.7)
axs[0,1].set_title('Collapse Prevention', fontsize=10)


############# GFRCM Jacketing ##########
axs[0,2].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[0,2].plot(Pga, noneng, '-', markersize=5, label='Non-Engineered - CP', color='Red')
axs[0,2].plot(Pga, GFRCMret, '-', markersize=5, label='GFRCM-Retrofitted - CP', color='green')
axs[0,2].set_xlabel('PGA (g)', fontsize=10)
axs[0,2].set_ylabel('Probability of exceedence', fontsize=10)
axs[0,2].legend(loc='lower right')
axs[0,2].grid(True, linestyle='--', alpha=0.7)
axs[0,2].set_title('Collapse Prevention', fontsize=10)


############## HEMP jacketing #############
axs[1,0].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[1,0].plot(Pga, noneng, '-', markersize=5, label='Non-Engineered - CP', color='Red')
axs[1,0].plot(Pga, HEMPret, '-', markersize=5, label='HEMP-Retrofitted - CP', color='green')
axs[1,0].set_xlabel('PGA (g)', fontsize=10)
axs[1,0].set_ylabel('Probability of exceedence', fontsize=10)
axs[1,0].legend(loc='lower right')
axs[1,0].grid(True, linestyle='--', alpha=0.7)
axs[1,0].set_title('Collapse Prevention', fontsize=10)


################# FRP jacketing ##############
axs[1,1].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[1,1].plot(Pga, noneng, '-', markersize=5, label='Non-Engineered - CP', color='Red')
axs[1,1].plot(Pga, FRPret, '-', markersize=5, label='FRP-Retrofitted - CP', color='green')
axs[1,1].set_xlabel('PGA (g)', fontsize=10)
axs[1,1].set_ylabel('Probability of exceedence', fontsize=10)
axs[1,1].legend(loc='lower right')
axs[1,1].grid(True, linestyle='--', alpha=0.7)
axs[1,1].set_title('Collapse Prevention', fontsize=10)

# Remove the last empty subplot
fig.delaxes(axs[1,2])

plt.tight_layout(rect=[0, 0, 1.0, 1])  # Adjust the right margin to make space for the legend

plt.show()


fig, axs= plt.subplots(2,3, figsize = (15,10))
#############for pre engineered ###################
axs[0,0].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[0,0].plot(Pga, preeng, '-', markersize=5, label='Pre-Engineered - CP', color='Red')
axs[0,0].plot(Pga, PRCret, '-', markersize=5, label='RC-Retrofitted - CP', color='green')
axs[0,0].set_xlabel('PGA (g)', fontsize=10)
axs[0,0].set_ylabel('Probability of exceedence', fontsize=10)
axs[0,0].legend(loc='lower right')
axs[0,0].grid(True, linestyle='--', alpha=0.7)
axs[0,0].set_title('Collapse Prevention', fontsize=10)

############### Steel Jacketing #######

axs[0,1].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[0,1].plot(Pga, preeng, '-', markersize=5, label='Pre-Engineered - CP', color='Red')
axs[0,1].plot(Pga, PSteelret, '-', markersize=5, label='Steel-Retrofitted - CP', color='green')
axs[0,1].set_xlabel('PGA (g)', fontsize=10)
axs[0,1].set_ylabel('Probability of exceedence', fontsize=10)
axs[0,1].legend(loc='lower right')
axs[0,1].grid(True, linestyle='--', alpha=0.7)
axs[0,1].set_title('Collapse Prevention', fontsize=10)


############# GFRCM Jacketing ##########
axs[0,2].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[0,2].plot(Pga, preeng, '-', markersize=5, label='Pre-Engineered - CP', color='Red')
axs[0,2].plot(Pga, PGFRCMret, '-', markersize=5, label='GFRCM-Retrofitted - CP', color='green')
axs[0,2].set_xlabel('PGA (g)', fontsize=10)
axs[0,2].set_ylabel('Probability of exceedence', fontsize=10)
axs[0,2].legend(loc='lower right')
axs[0,2].grid(True, linestyle='--', alpha=0.7)
axs[0,2].set_title('Collapse Prevention', fontsize=10)


############## HEMP jacketing #############
axs[1,0].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[1,0].plot(Pga, preeng, '-', markersize=5, label='Pre-Engineered - CP', color='Red')
axs[1,0].plot(Pga, PHEMPret, '-', markersize=5, label='HEMP-Retrofitted - CP', color='green')
axs[1,0].set_xlabel('PGA (g)', fontsize=10)
axs[1,0].set_ylabel('Probability of exceedence', fontsize=10)
axs[1,0].legend(loc='lower right')
axs[1,0].grid(True, linestyle='--', alpha=0.7)
axs[1,0].set_title('Collapse Prevention', fontsize=10)


################# FRP jacketing ##############
axs[1,1].plot(Pga, eng, '-', markersize=5, label='Engineered - CP', color='Blue')
axs[1,1].plot(Pga, preeng, '-', markersize=5, label='Pre-Engineered - CP', color='Red')
axs[1,1].plot(Pga, PFRPret, '-', markersize=5, label='FRP-Retrofitted - CP', color='green')
axs[1,1].set_xlabel('PGA (g)', fontsize=10)
axs[1,1].set_ylabel('Probability of exceedence', fontsize=10)
axs[1,1].legend(loc='lower right')
axs[1,1].grid(True, linestyle='--', alpha=0.7)
axs[1,1].set_title('Collapse Prevention', fontsize=10)

# Remove the last empty subplot
fig.delaxes(axs[1,2])

plt.tight_layout(rect=[0, 0, 1.0, 1])  # Adjust the right margin to make space for the legend

plt.show()
