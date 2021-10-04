from model.CommonFlow import *


class PandaGenerator:
    index: int
    bus: int
    p_mw: float
    name: str
    vm_pu: float
    min_q_mvar: float
    max_q_mvar: float
    in_service: bool = True

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
