import openseespy.opensees as ops
from Model import *
from Gravity import *
import numpy as np
print("Pushover analysis started")

# SET RECORDERS
ops.recorder('Node', '-file', 'Displacement.out', '-time', '-node', 8, '-dof', 1, 'disp')
ops.recorder('Node', '-file', 'ReactionsX.out', '-time', '-node',1,5,9, '-dof', 1, 'reaction')

# ANALYSIS
ops.timeSeries('Linear', 2)
ops.pattern('Plain', 2, 2)

ops.eigen("-getBandArpack",2)

phi1 = ops.nodeEigenvector(6,1,1)/ops.nodeEigenvector(8,1,1)
phi2 = ops.nodeEigenvector(7,1,1)/ops.nodeEigenvector(8,1,1)
phi3 = ops.nodeEigenvector(8,1,1)/ops.nodeEigenvector(8,1,1)
# print(phi1,phi2,phi3)
# print(phi1,phi2,phi3)

# Apply lateral load based on first mode shape in x direction
ops.load(2, phi1, 0.0, 0.0) 
ops.load(3, phi2, 0.0, 0.0)
ops.load(4, phi3, 0.0, 0.0)
# ops.load(4, 1, 0.0, 0.0, 0.0, 0.0, 0.0)3
# Define 4tep parameter4
step_size = 0.005
min_incr = 0.005
max_disp = 0.04* 9 # Analysis upto 2.5% drift
control_node = 4 # master node at top floor
no_steps = int(max_disp/step_size)
control_dof = 1
tol = 1e-3 # Tolerance
iter = 100 # Number of iterations

ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('UmfPack')
ops.test('NormDispIncr', tol, iter)
ops.algorithm('KrylovNewton')
ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter)
ops.analysis('Static')
ops.record()

# Analyze model
for j in range(1,no_steps+1):
    # print(f"step {j} running")
    ok = ops.analyze(1)
    if ok != 0: # reduce step size if analysis is unsuccessful
        print("Reducing step size")
        step_size = 0.001
        ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
        ok = ops.analyze(1)
        if ok != 0: # further reduce step size and increase iterations if analysis is unsuccessful
            print("Further reducing step size")
            step_size = 0.0005
            iter = 4000
            ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
            ok = ops.analyze(1)
        if ok != 0: # Change algorithm, reduce step size
            print("Changing Algorithm to Raphson Newton")
            step_size = 0.0001
            iter = 4000
            ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
            ops.algorithm('RaphsonNewton')
            ok = ops.analyze(1)
        if ok != 0: # Change algorithm
            print("Changing Algorithm to SecantNewton")
            step_size = 0.0001
            iter = 4000
            ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
            ops.algorithm('SecantNewton')
            ok = ops.analyze(1)    
        if ok != 0: # Change algorithm
            print("Changing Algorithm to KrylovNewton")
            step_size = 0.0001
            iter = 4000
            ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
            ops.algorithm('KrylovNewton')
            ok = ops.analyze(1)
        if ok != 0: # Change algorithm
            print("Changing Algorithm to Broyden")
            step_size = 0.0001
            iter = 4000
            ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
            ops.algorithm('Broyden')
            ok = ops.analyze(1)        
        if ok !=0: #EXIT code if analysis is still unsuccessful
            print("Analysis Unsuccessful")
            exit()
        if ok == 0: # Back to regular algorithm if analysis is successful
            print("Back to regular algorithm")
            step_size = 0.01
            iter = 500      
            ops.integrator('DisplacementControl', control_node, control_dof, step_size,iter,min_incr)
            ops.algorithm('NewtonLineSearch')
    # Reset for the next analysis sequence

ops.wipeAnalysis()


