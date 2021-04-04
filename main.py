import pandapower as pn
import pandapower.networks as netw
import openpyxl as xl


net = netw.simple_four_bus_system()
pn.runpp(net)
print('1321')