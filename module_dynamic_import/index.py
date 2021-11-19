import importlib

actions = {}
module_dir = 'actions'
module_names = ["add", "sub"]

for module in module_names:
  action = importlib.import_module(f"{module_dir}.{module}", module)
  actions[module] = getattr(action, module)
  print(actions[module](11111,999))
