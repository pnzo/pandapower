import pandapower as pn

from Model.common_elements import *
from Model.panda_elements import *

common_flow = CommonFlow('Files/nodes_branches.xlsx')
panda_flow = PandaFlow(common_flow)
print(123)

