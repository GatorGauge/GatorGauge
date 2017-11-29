<<<<<<< HEAD
import os
import sys

# set the system path to contain the previous directory
mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, mypath + '/../')
=======
""" Configure python to include parent directory modules """

import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH + '/../')
>>>>>>> master
