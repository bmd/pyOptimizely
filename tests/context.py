import os
import sys

# allows optimizely.py to be imported like a module without
# already being installed
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
