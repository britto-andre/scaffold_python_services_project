import sys
import importlib

try:
    importlib.import_module(f'src.app.{sys.argv[1]}.worker').run()
except:
    print('Its failed.')
