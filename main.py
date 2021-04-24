import pandapower as pn
import pandapower.networks as networks

from model.CommonFlow import CommonFlow
from model.PandaFlow import PandaFlow

common_flow = CommonFlow('Files/nodes_branches_3.xlsx')
panda_flow = PandaFlow(common_flow)

net = pn.create_empty_network()
for bus in panda_flow.buses:
    pn.create_bus(net=net, vn_kv=bus.vn_kv, name=bus.name, index=bus.index, max_vm_pu=2.0, min_vm_pu=0.5)
for load in panda_flow.loads:
    pn.create_load(net=net, bus=load.bus, p_mw=load.p_mw, q_mvar=load.q_mvar, index=load.index,
                   const_i_percent=30.0, const_z_percent=30.0)
for line in panda_flow.lines:
    pn.create_line_from_parameters(net=net, from_bus=line.from_bus, to_bus=line.to_bus, parallel=1,
                                   r_ohm_per_km=line.r_ohm_per_km, x_ohm_per_km=line.x_ohm_per_km,
                                   c_nf_per_km=line.c_nf_per_km, max_i_ka=1, length_km=1.0)
for ext_grid in panda_flow.ext_grids:
    pn.create_ext_grid(net=net, bus=ext_grid.bus, name=ext_grid.name, index=ext_grid.index, vm_pu=ext_grid.vm_pu)
for transformer in panda_flow.transformers:
    pn.create_transformer_from_parameters(net, hv_bus=transformer.hv_bus, lv_bus=transformer.lv_bus, sn_mva=100.0,
                                          vn_hv_kv=transformer.vn_hv_kv, vn_lv_kv=transformer.vn_lv_kv,
                                          vk_percent=transformer.vk_percent, vkr_percent=transformer.vkr_percent,
                                          i0_percent=0.0, pfe_kw=0.0)


pn.runpp(net, max_iteration=40, tolerance_mva=0.1)
pn.to_excel(net, 'D:/mynet.xlsx')
