import openseespy.opensees as ops
import matplotlib.pyplot as plt
import  openseespy.postprocessing.Get_Rendering as opsplt
import os

ops.model('BasicBuilder','-ndm',2,'-ndf',3)


nodeID = 1
x = [0.0, 3.2, 7.1]
y = [0.0, 3, 6, 9]
for i in range(len(x)):
    for k in range(len(y)):
        x_coord = x[i]
        y_coord = y[k]
                # Check if x_coord is 7.1 , y coord is 10.04 and z_coord is 9
        if not (x_coord == 7.1 and y_coord == 9.1):
                # Create the node and assign coordinates
            ops.node(nodeID, x_coord, y_coord)

            
            if y_coord == 0:  # fixing base
                    ops.fix(nodeID, 1, 1, 1)
                # Increment the node ID
            nodeID += 1



ops.equalDOF(2,6,2,3)
ops.equalDOF(3,7,2,3)
ops.equalDOF(4,8,2,3)
ops.equalDOF(10,6,2,3)
ops.equalDOF(11,7,2,3)
ops.equalDOF(12,8,2,3)


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



C_unconf = 1
C_conf = 2
R_steel = 3
frpconc = 4



# Basic parameters for materials
fc_1 = -15000  # f'c in compression for unconfined concrete
fc_2 = -48000  # f'c in compression for confined concrete
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
         
ops.uniaxialMaterial(
    "Concrete02", C_unconf, fc_1, epsc, fu_1, epsu, lambda_, ft_1, Et_1
)
ops.uniaxialMaterial("Concrete02", C_conf, fc_2, epsc, fu_2, epsu, lambda_, ft_2, Et_2)

# Definition of Steel02 steel
# uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2
ops.uniaxialMaterial("Steel02", R_steel, fy, Es, b, R0, cR1, cR2)


# ops.uniaxialMaterial('FRPConfinedConcrete02',frpconc,-15,18319.211,-0.002,'-Ultimate',-48.030,-0.0454,2.450,915.960,1)




Col300x300_4_16 = 1
# Col300x300_4_16 = 2
Col300x300_4_12 = 3
Beam230x350 = 4


pi = 3.14
Rebar_16 = pi * 0.016 * 0.016 / 4  # area rebar
# Rebar_20 = pi * 0.02 * 0.02 / 4
Rebar_12 = pi * 0.012 * 0.012 / 4
b_col = 0.2300  # column base
h_col = 0.2300  # column height
cover_Col = 0.02  # column cover
b_beam = 0.23  # beam base
h_beam = 0.35  # beam height
cover_Beam = 0.02  # beam cover

import FiberBuilder

FiberBuilder.ColumnBuilder(
    Col300x300_4_16,
    h_col,
    b_col,
    cover_Col,
    C_conf,
    C_conf,
    R_steel,
    Rebar_16,
    0.00000000001,
)

# FiberBuilder.ColumnBuilder(
#     Col300x300_4_16,
#     h_col,
#     b_col,
#     cover_Col,
#     C_conf,
#     C_unconf,
#     R_steel,
#     Rebar_16,
#     Rebar_12,
# )

FiberBuilder.ColumnBuilder(
    Col300x300_4_12,
    h_col,
    b_col,
    cover_Col,
    C_conf,
    C_conf,
    R_steel,
    Rebar_12,
    0.000000001,
)




FiberBuilder.BeamBuilder(
    Beam230x350,
    h_beam,
    b_beam,
    cover_Beam,
    C_unconf,
    C_unconf,
    R_steel,
    3,
    Rebar_12,
    3,
    Rebar_12,
)


PDTransCol = 1
LTransBeam = 2
ops.geomTransf('PDelta', PDTransCol) 
ops.geomTransf('PDelta', LTransBeam)
        
NI = 5

ops.element("nonlinearBeamColumn", 1, 1, 2, NI, Col300x300_4_16, PDTransCol)
ops.element("nonlinearBeamColumn", 2, 2, 3, NI, Col300x300_4_12, PDTransCol)
ops.element("nonlinearBeamColumn", 3, 3, 4, NI, Col300x300_4_12, PDTransCol)
ops.element("nonlinearBeamColumn", 4, 5, 6, NI, Col300x300_4_16, PDTransCol)
ops.element("nonlinearBeamColumn", 5, 6, 7, NI, Col300x300_4_12, PDTransCol)
ops.element("nonlinearBeamColumn", 6, 7, 8, NI, Col300x300_4_12, PDTransCol)
ops.element("nonlinearBeamColumn", 7, 9, 10, NI, Col300x300_4_16, PDTransCol)
ops.element("nonlinearBeamColumn", 8, 10, 11, NI, Col300x300_4_12, PDTransCol)
ops.element("nonlinearBeamColumn", 9, 11, 12, NI, Col300x300_4_12, PDTransCol)


ops.element('nonlinearBeamColumn', 10, 2,  6, NI,Beam230x350,LTransBeam)
ops.element("nonlinearBeamColumn", 11, 6, 10, NI, Beam230x350, LTransBeam)
ops.element("nonlinearBeamColumn", 12, 3, 7, NI, Beam230x350, LTransBeam)
ops.element("nonlinearBeamColumn", 13, 7, 11, NI, Beam230x350, LTransBeam)
ops.element("nonlinearBeamColumn", 14, 4, 8, NI, Beam230x350, LTransBeam)
ops.element("nonlinearBeamColumn", 15, 8, 12, NI, Beam230x350, LTransBeam)

# opsplt.plot_model()
# opsplt.plot_model("nodes","elements")
# opsplt.plot_modeshape(1)
# opsplt.plot_modeshape(2)
# opsplt.plot_modeshape(3)

