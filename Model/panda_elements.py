from Model.common_elements import *
import math
from typing import List


class PandaLine:
    name = ''
    from_bus = 0
    to_bus = 0
    length_km = 1.0
    r_ohm_per_km = 0.0
    x_ohm_per_km = 0.0
    c_nf_per_km = 0.0
    max_i_ka = 0.0
    parallel = 0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_branch: CommonBranch):
        self.name = common_branch.name
        self.from_bus = common_branch.ip
        self.to_bus = common_branch.iq
        self.r_ohm_per_km = common_branch.r
        self.x_ohm_per_km = common_branch.x
        self.c_nf_per_km = -common_branch.b * 1000 / (2 * math.pi * 50)


class PandaBus:
    name = ''
    vn_kv = 0.0
    in_service = True
    index = 0

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.index = common_node.ny
        self.vn_kv = common_node.uhom


class PandaLoad:
    name = ''
    index = 0
    bus = 0
    p_mw = 0.0
    q_mvar = 0.0
    const_z_percent = -30.0
    const_i_percent = 47.0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.bus = common_node.ny
        self.index = common_node.ny
        self.p_mw = common_node.pn
        self.q_mvar = common_node.qn


class PandaExtGrid:
    name = ''
    index = 0
    bus = ''
    vm_pu = 1.0
    va_degree = 0.0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.bus = common_node.ny
        self.vm_pu = common_node.vzd / common_node.uhom
        self.index = common_node.ny


class PandaFlow:
    buses: List[PandaBus] = []
    lines: List[PandaLine] = []
    loads: List[PandaLoad] = []
    ext_grids:  List[PandaExtGrid] = []

    def __init__(self):
        pass

    def __init__(self, common_flow: CommonFlow):
        for common_branch in common_flow.branches:
            self.lines.append(PandaLine(common_branch))
        for common_node in common_flow.nodes:
            self.buses.append(PandaBus(common_node))
            if common_node.pn != 0 or common_node.qn != 0:
                self.loads.append(PandaLoad(common_node))
            if common_node.vzd != 0:
                self.ext_grids.append(PandaExtGrid(common_node))

