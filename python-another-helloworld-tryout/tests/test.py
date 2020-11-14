import os,sys
from pprint import pprint

TEST_DIR = os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(TEST_DIR+'/..')
SRC_DIR=os.path.abspath(PROJ_HOME+'/src')
sys.path.append(PROJ_HOME)
# pprint(SRC_DIR)
# sys.exit()

from src.main import *

def test_helloworld():
  helloworld()

def test_helloAnotherWorld():
  helloAnotherWorld()
