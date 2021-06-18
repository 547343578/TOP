# VARIABLES DE DECISION
# Mi/Gi(i = 1...8): se instala aspersor MEDIANO/GRANDE en el punto i
# y = (0,1)
# 1: se instala >= 3 aspersonres MEDIO -> O.K. descuento
# 0: no ....
# 
# FUNCION OBJETIVO
# Min Z = 300 * (M1 + M2 + .... + M8) + 490 * (G1 + G2 + ... + G8) - 300*y
# 
# 
# RESTRICCION
# 1) G1 + G2 + G3 + G4 + G5 + G6 + G7 + G8 <= 2
# 2) M3 <= M6
# 3) M1 + M2 + M3 + M4 + M5 + M5 + M6 + M7 + M8 >= 3*y 

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

M1 = solver.BoolVar('M1')
M2 = solver.BoolVar('M2')
M3 = solver.BoolVar('M3')
M4 = solver.BoolVar('M4')
M5 = solver.BoolVar('M5')
M6 = solver.BoolVar('M6')
M7 = solver.BoolVar('M7')
M8 = solver.BoolVar('M8')

G1 = solver.BoolVar('G1')
G2 = solver.BoolVar('G2')
G3 = solver.BoolVar('G3')
G4 = solver.BoolVar('G4')
G5 = solver.BoolVar('G5')
G6 = solver.BoolVar('G6')
G7 = solver.BoolVar('G7')
G8 = solver.BoolVar('G8')

Y = solver.BoolVar('Y')

print('Numero de variables =', solver.NumVariables())

solver.Add(M1 + G1 >= 1)
solver.Add(G1 + G2 + G3 + G4 + G5 + M3 + M5 >= 1)
solver.Add(G5 + G6 + G7 + G8 + M7 >= 1)
solver.Add(G2 + G4 + M2 + M4 >= 1)
solver.Add(G2 + G3 + G4 + G5 + G6 + M3 + M4 + M6 >= 1)
solver.Add(G6 + G7 + G8 + M6 + M7 + M8 >= 1)

solver.Add(G1 + M1 <= 1)
solver.Add(G2 + M2 <= 1)
solver.Add(G3 + M3 <= 1)
solver.Add(G4 + M4 <= 1)
solver.Add(G5 + M5 <= 1)
solver.Add(G6 + M6 <= 1)

solver.Add(G1 + G2 + G3 + G4 + G5 + G6 + G7 + G8 <= 2)
solver.Add(M3 <= M6)
solver.Add(M1 + M2 + M3 + M4 + M5 + M5 + M6 + M7 + M8 >= 3*Y)

print('Numero de restricciones =', solver.NumConstraints())


solver.Minimize(300 * (M1 + M2 + M3 + M4 + M5 + M6 + M7+ M8) + 490 * (G1 + G2 + G3 + G4 + G5 + G6 + G7 + G8) - 300*Y)

status = solver.Solve()

if status == solver.OPTIMAL:
	print("Se ha encontrado la SOLUCION OPTIMA")
	print('Valor de la FUNCION OBJETIVO =', solver.Objective().Value())
	print('Valor optimo de M1 =', M1.solution_value())
	print('Valor optimo de M2 =', M2.solution_value())
	print('Valor optimo de M3 =', M3.solution_value())
	print('Valor optimo de M4 =', M4.solution_value())
	print('Valor optimo de M5 =', M5.solution_value())
	print('Valor optimo de M6 =', M6.solution_value())
	print('Valor optimo de M7 =', M7.solution_value())
	print('Valor optimo de M8 =', M8.solution_value())
	print('Valor optimo de G1 =', G1.solution_value())
	print('Valor optimo de G2 =', G2.solution_value())
	print('Valor optimo de G3 =', G3.solution_value())
	print('Valor optimo de G4 =', G4.solution_value())
	print('Valor optimo de G5 =', G5.solution_value())
	print('Valor optimo de G6 =', G6.solution_value())
	print('Valor optimo de G7 =', G7.solution_value())
	print('Valor optimo de G8 =', G8.solution_value())
else:
	print("NO ha sido posible encontrar la solucion optima")