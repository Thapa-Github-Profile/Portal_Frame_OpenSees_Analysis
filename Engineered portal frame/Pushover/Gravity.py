from Model import *
import openseespy.opensees as ops
ops.recorder('Node', '-file', 'Gravity_Reactions.out','-time','-node', 1,5,9, '-dof', 2, 'reaction')
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)


ops.load(2,0,-84.9179,0)
ops.load(6,0,-88.8839,0)
ops.load(10,0,-62.5959,0)
ops.load(3,0,-84.9179,0)
ops.load(7,0,-88.8839,0)
ops.load(11,0,-62.5959,0)
ops.load(4,0,-47.553,0)
ops.load(8,0,-49.8646,0)
ops.load(12,0,-33.0425,0)


               
# Constraint Handler 
ops.constraints('Transformation')
# DOF Numberer                                
ops.numberer('RCM')   
# System of Equations  
ops.system('BandGeneral') 
# Convergence Test 
ops.test('NormDispIncr',0.000001,100,0,2)   
# Solution Algorithm 
ops.algorithm('Newton') 
# Integrator
#integrator LoadControl $lambda <$numIter $minLambda $maxLambda>  
ops.integrator('LoadControl',0.1)   
# Analysis Type 
ops.analysis('Static')
# Record initial state of model 
ops.record
# Analyze model 
ops.analyze(10)  
ops.loadConst('-time', 0.0)
print("ooo  Gravity  Completed ")
