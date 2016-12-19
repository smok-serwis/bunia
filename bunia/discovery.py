import importlib
import inspect
import pkgutil

from bunia.api import Command


def from_name(name):
    if ':' in name:
        module, clsname = name.split(':', 2)

        return importlib.import_module(module).__dict__[clsname]
    else:
        return importlib.import_module(name).COMMAND


def from_module(module):
    """
    Walk a module (+ imported submodules) and return  Command instances found

    :param module: module to examine
    :return: list of Command instances found
    """
    # get all classes
    commands = []
    for name, member in inspect.getmembers(module):
        if inspect.isclass(member) and issubclass(member, Command):
            commands.append(member)

    # get submodules
    try:
        l = pkgutil.walk_packages(module.__path__, onerror=lambda x: None)
    except AttributeError:  # no __path__
        return commands

    for finder, modname, ispkg in l:
        commands.extend(from_module(finder.find_module(modname).load_module(modname)))

    return commands

