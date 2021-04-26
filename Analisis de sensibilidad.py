# Analisis de sensibilidad
from docplex.mp.model import Model

# Se nombra el modelo
md1 = Model('Problema Clásico')

# Se crean las variables
xt = md1.continuous_var(name='xt')
xg = md1.continuous_var(name='xg')
xa = md1.continuous_var(name='xa')
ca = md1.continuous_var(name='ca')
va = md1.continuous_var(name='va')

# Se introduce la funcion objetivo
md1.maximize(450*xg+120*xt+22*va+28*xa-28*ca)

# Se introducen las restricciones
md1.add_constraint(xt+xa+0.1*xg <= 800)
md1.add_constraint(2*xt+3*xa+0.05*xg <= 1000)
md1.add_constraint(4*xa+ca-5*xg-va == 0)

# Se soluciona el sistema
solution = md1.solve(log_output=True)
print("\nSolucion del sistema\n")
print(solution)

# Numero de restricciones
n_const = md1.number_of_constraints

# Restricciones en un arreglo
const = [md1.get_constraint_by_index(i) for i in range(n_const)]

# Variable de holgura
h = md1.slack_values(const)

# Impresion variables de holgura
print("Variables de holgura\n")
for n in range(n_const):
    print("La variable de holgura de la restricción "+str(const[n])+" es "+str(h[n]))

# Impresion valor dual
print("\nValor dual\n")
valor_dual = md1.dual_values(const)
for n in range(n_const):
    print("El valor dual de la restricción "+str(const[n])+" es "+str(valor_dual[n]))

# Aplicacion analisis de sensibilidad
cpx = md1.get_engine().get_cplex()
of = cpx.solution.sensitivity.objective()
b = cpx.solution.sensitivity.rhs()
var_list = [md1.get_var_by_name('xt'), md1.get_var_by_name('xg'), md1.get_var_by_name('xa'), md1.get_var_by_name('ca'), md1.get_var_by_name('va')]

print("\nAnalisis\n")
for n in range(len(var_list)):
    print("La variable "+str(var_list[n])+" "+str(of[n]))

print("\nAnalisis\n")
for n in range(n_const):
    print("La restricción "+str(const[n])+" "+str(b[n]))
print("\n")

md2 = Model('Problema Aplicado')

'''
Una empresa de muebles planea introducir una línea para jardín que conste de sillas, mecedoras y sillones.
Cada mueble requiere madera, plástico y aluminio para su fabricación de acuerdo con la siguiente tabla.

          |  Madera  |  Plastico  |  Aluminio  
-----------------------------------------------
 silla    | 1 unidad | 1 unidad   | 2 unidades 
 mecedora | 1 unidad | 1 unidad   | 3 unidades
 sillon   | 1 unidad | 2 unidades | 5 unidades

La empresa dispone de 400 unidades de madera, 500 de plástico y 1,450 de aluminio para iniciar la
producción. Considera que puede vender cada silla en 21 dólares, cada mecedora en $24 y cada sillón en
$36 y que puede colocar en el mercado toda su producción. Determina los niveles de producción para cada
uno de sus productos a fin de obtener el mayor ingreso posible y adicionalmente se busca realizar el respectivo
analisis de sensibilidad.

x = número de sillas producidas
y = número de mecedoras producidas
z = número de sillones producidos

link ejercicio: http://practicasprofesionales.ula.edu.mx/documentos/ULAONLINE/Licenciatura/Ing_ind_prod/PMI402/Semana%204/PMI402_S4_E_Ejem_met_Sim.pdf
'''

x = md2.continuous_var(name='x')
y = md2.continuous_var(name='y')
z = md2.continuous_var(name='z')

md2.maximize(21*x+24*y+36*z)
md2.add_constraint(x+y+z <= 400)
md2.add_constraint(x+y+2*z <= 500)
md2.add_constraint(2*x+3*y+5*z <= 1450)

solution2 = md2.solve(log_output=True)

print("\nSolucion del sistema\n")
print(solution2)

# Numero de restricciones
n_const2 = md2.number_of_constraints

# Restricciones en un arreglo
const2 = [md2.get_constraint_by_index(i) for i in range(n_const2)]

# Variable de holgura
h2 = md2.slack_values(const2)

# Impresion variables de holgura
print("Variables de holgura\n")
for n in range(n_const2):
    print("La variable de holgura de la restricción "+str(const2[n])+" es "+str(h2[n]))

# Impresion valor dual
print("\nValor dual\n")
valor_dual2 = md2.dual_values(const2)
for n in range(n_const2):
    print("El valor dual de la restricción "+str(const2[n])+" es "+str(valor_dual2[n]))

# Aplicacion analisis de sensibilidad
cpx2 = md2.get_engine().get_cplex()
of2 = cpx2.solution.sensitivity.objective()
b2 = cpx2.solution.sensitivity.rhs()
var_list2 = [md2.get_var_by_name('x'), md2.get_var_by_name('y'), md2.get_var_by_name('z')]

print("\nAnalisis\n")
for n in range(len(var_list2)):
    print("La variable "+str(var_list2[n])+" "+str(of2[n]))

print("\nAnalisis\n")
for n in range(n_const2):
    print("La restricción "+str(const2[n])+" "+str(b2[n]))
print("\n")
