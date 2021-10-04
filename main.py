import pandapower as pn
import pandapower.converter as converter
import pandapower.networks as networks

from model.CommonFlow import CommonFlow
from model.PandaFlow import PandaFlow

common_flow = CommonFlow('Files/nodes_branches_3.xlsx')
panda_flow = PandaFlow(common_flow)

net = pn.create_empty_network()
for bus in panda_flow.buses:
    pn.create_bus(net=net, vn_kv=bus.vn_kv, name=bus.name, index=bus.index, max_vm_pu=2.0, min_vm_pu=0.5)
for active_load in panda_flow.active_loads:
    pn.create_load(net=net, bus=active_load.bus, p_mw=active_load.p_mw, q_mvar=0.0,
                   const_i_percent=active_load.const_i_percent, const_z_percent=active_load.const_z_percent)
for reactive_load in panda_flow.reactive_loads:
    pn.create_load(net=net, bus=reactive_load.bus, p_mw=0.0, q_mvar=reactive_load.q_mvar,
                   const_i_percent=reactive_load.const_i_percent, const_z_percent=reactive_load.const_z_percent)
for line in panda_flow.lines:
    pn.create_line_from_parameters(net=net, from_bus=line.from_bus, to_bus=line.to_bus, parallel=1,
                                   r_ohm_per_km=line.r_ohm_per_km, x_ohm_per_km=line.x_ohm_per_km,
                                   c_nf_per_km=line.c_nf_per_km, max_i_ka=1.0, length_km=1.0)
for ext_grid in panda_flow.ext_grids:
    pn.create_ext_grid(net=net, bus=ext_grid.bus, name=ext_grid.name, vm_pu=ext_grid.vm_pu)
for shunt in panda_flow.shunts:
    pn.create_shunt(net, bus=shunt.bus, q_mvar=shunt.q_mvar, index=shunt.index)
for generator in panda_flow.generators:
    pn.create_gen(net, bus=generator.bus, p_mw=generator.p_mw, vm_pu=generator.vm_pu, name=generator.name,
                  index=generator.index, min_q_mvar=generator.min_q_mvar, max_q_mvar=generator.max_q_mvar,
                  max_p_mw=generator.p_mw, min_p_mw=generator.p_mw)
for transformer in panda_flow.transformers:
    pn.create_transformer_from_parameters(net, hv_bus=transformer.hv_bus, lv_bus=transformer.lv_bus,
                                          sn_mva=transformer.sn_mva, vn_hv_kv=transformer.vn_hv_kv,
                                          vn_lv_kv=transformer.vn_lv_kv, vk_percent=transformer.vk_percent,
                                          vkr_percent=transformer.vkr_percent,
                                          i0_percent=0.0, pfe_kw=0.0, in_service=True,
                                          shift_degree=transformer.shift_degree)

for i in range(1, 2):
    pn.runpp(net, max_iteration=40, tolerance_mva=0.1)

    # pn.runopp(net, max_iteration=40, tolerance_mva=0.1)
    print("1")
pn.to_excel(net, 'D:/mynet.xlsx')
