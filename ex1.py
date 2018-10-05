from openmdao.api import Problem, ScipyOptimizeDriver, ExecComp, IndepVarComp 

# build the model 
prob = Problem() 
indeps = prob.model.add_subsystem('indeps', IndepVarComp()) 
indeps.add_output('x', 3.0) 
indeps.add_output('y', -4.0) 

prob.model.add_subsystem('paraboloid', ExecComp('f = (x-3)**2 + x*y + (y+4)**2 - 3')) 

prob.model.connect('indeps.x', 'paraboloid.x') 
prob.model.connect('indeps.y', 'paraboloid.y') 

prob.driver = ScipyOptimizeDriver() 
prob.driver.options['optimizer'] = 'SLSQP' 

prob.model.add_design_var('indeps.x', lower=-50, upper=50) 
prob.model.add_design_var('indeps.y', lower=-50, upper=50) 
prob.model.add_objective('paraboloid.f') 

prob.setup() 
prob.run_driver() 

# minimum value 
print(prob['paraboloid.f']) 
# location of the minimum 
print(prob['indeps.x']) 
print(prob['indeps.y'])
