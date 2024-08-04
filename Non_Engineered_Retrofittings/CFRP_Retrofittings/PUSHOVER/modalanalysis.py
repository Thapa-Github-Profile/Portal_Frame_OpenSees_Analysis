import Modal
import openseespy.opensees as ops
import numpy as np

#EIGEN

ops.eigen("-getBandArpack",2)

phi1 = ops.nodeEigenvector(6,1,1)/ops.nodeEigenvector(8,1,1)
phi2 = ops.nodeEigenvector(7,1,1)/ops.nodeEigenvector(8,1,1)
phi3 = ops.nodeEigenvector(8,1,1)/ops.nodeEigenvector(8,1,1)
print(phi1,phi2,phi3)