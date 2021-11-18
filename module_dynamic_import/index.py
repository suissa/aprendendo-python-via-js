#from actions.add import *
import importlib

#print(add(2,3))
actions = {}

moduleNames = ['actions.add', 'actions.sub']

#my_module = importlib.import_module('*', 'actions.add')

command = 'add'
#exec("from actions.%s import *" % command)

actions[command] = importlib.import_module('actions.add', 'add')
print(actions)
print(actions[command].add(2,3))
#print(actions[command](2,3))

import importlib.util
import sys

spec = importlib.util.spec_from_file_location(command, './actions/add.py')
print(spec)
module = importlib.util.module_from_spec(spec)
print(module)
sys.modules[command] = module
spec.loader.exec_module(module)
#print(add(2,5))