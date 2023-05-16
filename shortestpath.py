import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pandas as pd

routes = pd.read_csv('routes.csv')

model = pyo.ConcreteModel()

# Sets and Parameters
model.d       = {}
model.in_set  = {}
model.out_set = {}

for index,row in routes.iterrows():
    model.d[(row['from'],row['to'])] = row['distance']
    try:
        model.in_set[row['to']].append(row['from'])
    except:
        model.in_set[row['to']] = [row['from']]
        
    try:    
        model.out_set[row['from']].append(row['to'])
    except:
        model.out_set[row['from']] = [row['to']]

        
begin_node = 'A'
end_node   = 'F'

path_node = set(routes['from'].to_list()).intersection(set(routes['to'].to_list()))

path_node = path_node - set([begin_node]) - set([end_node])

# Variables
model.x = pyo.Var(list(zip(routes['from'],routes['to'])), within=pyo.Binary)

# Objective Function
model.obj = pyo.Objective(expr = sum([model.x[j['from'],j['to']]*j['distance'] for i,j in routes.iterrows()]),
                          sense=pyo.minimize)


# Constarints
model.C1 = pyo.Constraint(expr = sum([model.x[begin_node,node] for node in model.out_set[begin_node]]) == 1)

model.C2 = pyo.Constraint(expr = sum([model.x[node,end_node] for node in model.in_set[end_node]]) == 1)


model.C3 = pyo.ConstraintList()
for node in path_node:
    model.C3.add(expr = sum([model.x[node,i] for i in model.out_set[node]]) == sum([model.x[j,node] for j in model.in_set[node]]))
    
#solve
opt = SolverFactory('gurobi')
model.results = opt.solve(model)

model.pprint()
print('\n\nOF:',pyo.value(model.obj))
for route in list(zip(routes['from'],routes['to'])):
    if pyo.value(model.x[route[0], route[1]]) >= 0.9:
        print('Route activated: %s-%s' % (route[0], route[1]))