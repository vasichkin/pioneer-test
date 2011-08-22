"""
Way to import definitions from files in feature folder

"""

import os.path
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from steps.steps_nova_manage import *
from steps.steps_nova_init import *
