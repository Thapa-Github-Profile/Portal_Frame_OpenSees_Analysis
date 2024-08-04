# Import OpenSeesPy library
import openseespy.opensees as ops
import matplotlib.pyplot as plt
import os

import openseespy.postprocessing.Get_Rendering as opsplt
ops.wipe()
ops.model('BasicBuilder', '-ndm', 2, '-ndf', 3)  # 2 dimensions, 3 DOF per node
# GLOBAL GEOMETRY
x=[0.0, 3.2, 7.1] 
y=[0.0, 3,6,9]
# z=[0.0, 2.845, 5.69,8.534]

nodeID = 1   ################################## Start with the first node ID
for i in range(len(x)):
    for j in range(len(y)):
    
        x_coord = x[i]
        y_coord = y[j]
        # Check if x_coord is 7.1 and z_coord is 9
        if not (x_coord==7.2 and y_coord==9):
            # Create the node and assign coordinates
            ops.node(nodeID, x_coord, y_coord)
                        
            if y_coord == 0: #fixing base
                ops.fix(nodeID, 1, 1, 1)
            # Increment the node ID
            nodeID += 1

totalid=nodeID-1
#Assigning mass in each nodeID
##### First floor#####
ops.mass(2,5.62,5.62,0)
ops.mass(6,8.69,8.96,0)
ops.mass(10,6.32,6.32,0)

#############second floor#################
ops.mass(3,5.62,5.62,0)
ops.mass(7,8.69,8.69,0)
ops.mass(11,6.32,6.32,0)

##########3rd floor##############
ops.mass(4,2.89,2.89,0)
ops.mass(8,4.82,4.82,0)
ops.mass(12,3.3,3.3,0)

ops.equalDOF(2,6,2,3)
ops.equalDOF(6,10,2,3)
ops.equalDOF(3,7,2,3)
ops.equalDOF(7,11,2,3)
ops.equalDOF(4,8,2,3)
ops.equalDOF(8,12,2,3)




C_unconf = 1
C_conf = 2
R_steel = 3
fiber = 5


# Basic parameters for materials
fc_1 = -15000  # f'c in compression for unconfined concrete
fc_2 = -15000  # f'c in compression for confined concrete
epsc = -0.002  # strain at maximum stress in compression
fu_1 = fc_1 * 0.2  # ultimate stress for unconfined concrete
fu_2 = fc_2 * 0.2  # ultimate stress for confined concrete
epsu = -0.02  # strain at ultimate stress in compression
lambda_ = 0.1  # ratio between reloading stiffness and initial stiffness in compression
ft_1 = fc_1 * -0.1  # maximum stress in tension for unconfined concrete
ft_2 = fc_2 * -0.1  # maximum stress in tension for confined concrete
Et_1 = ft_1 / 0.002  # Elastic modulus in tension for unconfined concrete
Et_2 = ft_2 / 0.002  # Elastic modulus in tension for confined concrete
fy = 415000  # fy for reinforcing steel
Es = 210000000  # E for reinforcing steel
b = 0.005  # strain hardening ratio
R0 = 20  # smoothness of the elastic-to-plastic transition
cR1 = 0.925  # smoothness of the elastic-to-plastic transition
cR2 = 0.15  # smoothness of the elastic-to-plastic transition

# Definition of Concrete02 material
# uniaxialMaterial Concrete02 $matTag $fpc $epsc0 $fpcu $epsU $lambda $ft $Ets
ops.uniaxialMaterial('Concrete02', C_unconf, fc_1, epsc, fu_1, epsu, lambda_, ft_1, Et_1)
ops.uniaxialMaterial('Concrete02', C_conf, fc_2, epsc, fu_2, epsu, lambda_, ft_2, Et_2)

# Definition of Steel02 steel
# uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2
ops.uniaxialMaterial('Steel02', R_steel, fy, Es, b, R0, cR1, cR2)
# Angle_Material=10
# ops.uniaxialMaterial('Steel02', Angle_Material, 250000, Es, 0.0000001, R0, cR1, c
# uniaxialMaterial('FRPConfinedConcrete02', matTag, fc0, Ec, ec0, <'-JacketC', tfrp, Efrp, erup, R>, <'-Ultimate', fcu, ecu>, ft, Ets, Unit)
ops.uniaxialMaterial('MultiLinear', fiber,0.00045,460050,0.0038,431110,0.00690,872170)
# ops.uniaxialMaterial('FRPConfinedConcrete02', fiber,-15,18319,-0.002, 2.44,915.96,1)
# Continue with the rest of your analysis and modeling in OpenSeesPy.
# SECTIONS
# Define section IDs
Gcol = 1  #Ground floor column 350*350 with 8 16mm
Fcol = 3  #Ground floor column 350*350 with 4 16+4 12
Scol = 2  #Ground floor column 350*350 with 8 12mm
Beam230x350=4  #all size equal of 325*230 with 3 12 Top N 3 16 Bot

# Define dimensions
pi = 3.14
Rebar_16 = pi * 0.016 * 0.016 / 4 # area rebar 16mm
Rebar_20 = pi * 0.020 * 0.020 / 4 # area rebar 20mm
Rebar_12 = pi * 0.012 * 0.012 / 4 # area rebar 12mm
b_col = 0.23   # column base
h_col = 0.23  # column height
r_col = 0.02   # column cover
b_beam = 0.23  # beam base
h_beam = 0.35  # beam height
r_beam = 0.02  # beam cover
# # Load procedure
import FiberBuilder

# Build sections
# def columnbuilder(id,HSec,BSec,cover,coreID, coverID,Steel,intbar,cornerbar,fiber,ft):
ft = 0.002
FiberBuilder.CFRPBuilder(Gcol,h_col,b_col,r_col,C_conf,C_unconf,R_steel,Rebar_16,0.0000000000000001,fiber,ft)
FiberBuilder.CFRPBuilder(Fcol,h_col,b_col,r_col,C_conf,C_unconf,R_steel,Rebar_12,0.0000000000000001,fiber,ft)
FiberBuilder.CFRPBuilder(Scol,h_col,b_col,r_col,C_conf,C_unconf,R_steel,Rebar_12,0.0000000000000001,fiber,ft)

# def Beambuilder(id, HSec, BSec, cover, coreID, coverID, steelID, numBarsTop, barAreaTop, numBarsBot, barAreaBot):
FiberBuilder.BeamBuilder(Beam230x350, h_beam, b_beam, r_beam, C_conf, C_unconf, R_steel, 3, Rebar_12, 3, Rebar_12)

# ELEMENTS
# Definition of transformation IDs
PDTransCol = 1
LTransBeaY = 3

# Definition of transformations
# geomTransf PDelta $transfTag $vecxzX $vecxzY $vecxzZ <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>
ops.geomTransf('PDelta', PDTransCol) 
ops.geomTransf('PDelta', LTransBeaY)
# Definition of the number of integration points
NI = 5
# Define element properties (e.g., section and transformation tags)
# Initialize the element tag


######################  COLUMN  ##############################################
# Ground Floor Column
#ops.element('nonlinearBeamColumn', eleTag, i, j, NI, Col325x325, PDTransCol)
ops.element('nonlinearBeamColumn',1 ,1 , 2, NI, Gcol, PDTransCol)
ops.element('nonlinearBeamColumn',2 ,5 , 6, NI, Gcol, PDTransCol)
ops.element('nonlinearBeamColumn',3 ,9 , 10,NI, Gcol, PDTransCol)

################column elements##################
####### First Floor ####################
#ops.element('nonlinearBeamColumn', eleTag, i, j, NI, Col300x300, PDTransCol)
ops.element('nonlinearBeamColumn',12 ,2 , 3, NI, Fcol, PDTransCol)
ops.element('nonlinearBeamColumn',13 ,6 , 7, NI, Fcol, PDTransCol)
ops.element('nonlinearBeamColumn',14 ,10 ,11,NI, Fcol, PDTransCol)

################column elements##################
####### second  Floor ####################
#ops.element('nonlinearBeamColumn', eleTag, i, j, NI, Col300x300, PDTransCol)
ops.element('nonlinearBeamColumn',23 ,3 , 4, NI, Scol, PDTransCol)
ops.element('nonlinearBeamColumn',24 ,7 , 8, NI, Scol, PDTransCol)
ops.element('nonlinearBeamColumn',25 ,11, 12,NI, Scol, PDTransCol)

##### Beams Parllel to Y- axis########
########### Ground Floor ##############
ops.element('nonlinearBeamColumn', 55, 2, 6 , NI, Beam230x350, LTransBeaY)
ops.element('nonlinearBeamColumn', 56, 6, 10, NI, Beam230x350, LTransBeaY)

##### Beams Parllel to Y- axis########
########### First Floor ##############
ops.element('nonlinearBeamColumn', 63, 3, 7 , NI, Beam230x350, LTransBeaY)
ops.element('nonlinearBeamColumn', 64, 7, 11, NI, Beam230x350, LTransBeaY)

##### Beams Parllel to Y- axis########
########### Second Floor ##############
ops.element('nonlinearBeamColumn', 71, 4, 8, NI, Beam230x350, LTransBeaY)
ops.element('nonlinearBeamColumn', 72, 8, 12, NI, Beam230x350, LTransBeaY)

#opsplt.plot_model()
# opsplt.plot_model("nodes","elements")
# opsplt.plot_modeshape(1)
# opsplt.plot_modeshape(2)
# opsplt.plot_modeshape(3)
