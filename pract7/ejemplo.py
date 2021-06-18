from ortools.linear_solver import pywraplp


# Declarar el SOLVER
# Create the linear solver with the GLOP backend.
solver = pywraplp.Solver.CreateSolver('GLOP')


# Crear las variables
x1 = solver.NumVar(0, solver.infinity(), 'x1')
x2 = solver.NumVar(0, solver.infinity(), 'x2')

print('Numero de variables =', solver.NumVariables())


# Definir las Restricciones
# Restriccion 1: x1<=1
solver.Add(1 * x1 + 0 * x2 <= 4)

# Restriccion 2: 2 x2 <= 12
solver.Add(0 * x1 + 2 * x2 <= 12)

# Restriccion 3: 3 * x1 + 2 * x2 <= 18
solver.Add(3 * x1 + 2 * x2 <= 18)

print('Numero de restricciones =', solver.NumConstraints())


# Definir la Funcion objetiva
solver.Maximize(3 * x1 + 5 * x2)


# Llamar al Solver
status = solver.Solve()


# Mostrar los resultados 
if status == solver.ABNORMAL:
	print("Se ha producido un error mientras se ejecutaba el solver")
elif status == solver.FEASIBLE:
	print("Se ha encontrado una SOLUCION FACTIBLE")
	Print('Valor de la FUNCION OBJETIVO =', objetivo.Value())
	print('Valor optimo de [x1] =', x1.solution_value())
	print('Valor optimo de [x2] =', x2.solution_value())
elif status == solver.INFEASIBLE:
	print("El problema NO tiene SOLUCION POSBLE")
elif status == solver.NOT_SOLVED:
	print('No se ha podido encontrar NINGUNA SOLUCION en el TIEMPO proporcionado')
elif status == solver.OPTIMAL:
	print('Se ha encontrado la SOLUCION OPTIMA')
	print('Valor de la Funcion Objetivo =', solver.Objective().Value())
	print('Valor optimo de [x1] =', x1.solution_value())
	print('Valor optimo de [x2] =', x2.solution_value())
elif status == solver.UNBOUNDED:
	print("Solucion no acotada por las restricciones")
else:
	print("Codigo de error desconocido")
