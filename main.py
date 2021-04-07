import pandapower as pn
import pandapower.networks as netw
import openpyxl as xl
from Model.common_elements import *

flow = CommonFlow('Files/nodes_branches.xlsx')
print(flow.branches[0])
