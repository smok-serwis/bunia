import importlib

def from_name(name):
    if ':' in name:
        module, clsname = name.split(':', 2)

        return importlib.import_module(module).__dict__[clsname]
    else:
        return importlib.import_module(name).COMMAND
