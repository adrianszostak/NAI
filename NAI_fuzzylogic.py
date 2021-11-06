'''
Authors: Hubert Korzeniewski s19469, Adrian Szostak s19777
Job satisfaction with the use of fuzzy logic.

To run program install:
pip install scikit-fuzzy
pip install matplotlib
'''

'''
Import necessary libraries
'''

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Create the four fuzzy variables - three inputs, one output.
'''
salary = ctrl.Antecedent(np.arange(40, 200, 1), 'average_salary')
stress_lvl = ctrl.Antecedent(np.arange(1, 10, 1), 'stress_lvl')
relations_with_co_workers = ctrl.Antecedent(np.arange(1, 10, 1), 'relations_with_co_workers')
satisfaction = ctrl.Consequent(np.arange(1, 10, 1), 'satisfaction')

'''
Auto-membership function population. Here we use the convenience `automf` to populate the fuzzy variables with terms.
'''
salary.automf(3)
stress_lvl.automf(3)
relations_with_co_workers.automf(3)

satisfaction['low'] = fuzz.trimf(satisfaction.universe, [0, 0, 5])
satisfaction['medium'] = fuzz.trimf(satisfaction.universe, [0, 5, 10])
satisfaction['high'] = fuzz.trimf(satisfaction.universe, [5, 10, 10])


'''
Defining complex rules
1. If the stress_lvl is good OR the salary is poor OR relations_with_co_workers is poor, the the satisfaction will be low.
2. If the salary is good, then satisfaction will be high.
3. If the stress_lvl is poor AND salary is average, then satisfaction will be high.
4. If the relations_with_co_workers is good AND stress_lvl is poor, then satisfaction will be high
5. If the relations_with_co_workers is average AND stress_lvl is good, then satisfaction will be medium.
6. the If relations_with_co_workers is poor AND stres_lvl is good, then satisfaction will be low.
'''
rule1 = ctrl.Rule(stress_lvl['good'] | salary['poor'] | relations_with_co_workers['poor'], satisfaction['low'])
rule4 = ctrl.Rule(salary['good'], satisfaction['high'])
rule5 = ctrl.Rule(stress_lvl['poor'] & salary['average'], satisfaction['high'])
rule2 = ctrl.Rule(relations_with_co_workers['good'] & stress_lvl['poor'], satisfaction['high'])
rule3 = ctrl.Rule(relations_with_co_workers['average'] & stress_lvl['good'], satisfaction['medium'])
rule6 = ctrl.Rule(relations_with_co_workers['poor'] & stress_lvl['good'], satisfaction['low'])

'''
Control System Creation and Simulation
---------------------------------------

Add these rules to a new ControlSystem and define a ControlSystemSimulation to run it.
'''
satisfaction_ctrl = ctrl.ControlSystem([rule1, rule2, rule4, rule5, rule3, rule6])

'''
starting the program with a set of input data
'''
satisfaction_stats = ctrl.ControlSystemSimulation(satisfaction_ctrl)

'''
Simulating our control system by simply specifying the inputs and calling the ``compute`` method.
'''
satisfaction_stats.input['average_salary'] = 120
satisfaction_stats.input['stress_lvl'] = 4
satisfaction_stats.input['relations_with_co_workers'] = 9
satisfaction_stats.compute()

'''
Once computed, we can view the result as well as visualize it.
'''
print(satisfaction_stats.output['satisfaction'])
satisfaction.view(sim=satisfaction_stats)
