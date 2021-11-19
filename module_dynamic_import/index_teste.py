
import importlib.util
import sys

spec = importlib.util.spec_from_file_location(command, './actions/add.py')
print(spec)
module = importlib.util.module_from_spec(spec)
print(module)
sys.modules[command] = module
spec.loader.exec_module(module)
#print(add(2,5))