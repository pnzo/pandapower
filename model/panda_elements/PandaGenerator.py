from model.CommonFlow import *


class PandaGenerator:
    index = 0
    bus = 0
    p_mw = 0.0
    name = ''
    vm_pu = 0.0
    min_q_mvar = 0.0
    max_q_mvar = 0.0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.bus = common_node.ny
        self.index = common_node.ny
        self.p_mw = common_node.pg
        self.min_q_mvar = common_node.qmin
        self.max_q_mvar = common_node.qmax
        self.vm_pu = common_node.vzd / common_node.uhom
