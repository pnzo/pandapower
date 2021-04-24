from model.CommonFlow import *


class PandaLoad:
    name = ''
    bus = 0
    index = 0
    p_mw = 0.0
    q_mvar = 0.0
    const_z_percent = -30.0
    const_i_percent = 47.0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.index = common_node.ny
        self.bus = common_node.ny
        self.p_mw = common_node.pn
        self.q_mvar = common_node.qn
