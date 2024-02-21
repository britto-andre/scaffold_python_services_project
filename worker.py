import sys
import importlib

from src.app.common.utils.logger import logger

try:
    importlib.import_module(f'src.app.{sys.argv[1]}').run()
except:
    logger.error(f'Its Fail! {sys.exc_info()[0]}', exc_info=True)
