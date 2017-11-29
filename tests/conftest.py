""" Configure python to include parent directory modules """

import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH + '/../')
