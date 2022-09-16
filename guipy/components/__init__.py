import importlib
import pkgutil
from inspect import isclass

__all__ = []

# modified from: https://julienharbulot.com/python-dynamical-import.html
# iterate through the modules in the current package
# package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in pkgutil.iter_modules(__path__):

    # import the module and iterate through its attributes
    module = importlib.import_module(f"{__name__}.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isclass(attribute):
            # Add the class to this package's variables
            globals()[attribute_name] = attribute
            __all__.append(attribute_name)
