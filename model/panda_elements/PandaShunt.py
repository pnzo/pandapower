from model.CommonFlow import *


class PandaShunt:
    index = 0
    bus = 0
    q_mvar = 0.0
    name = ''
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.bus = common_node.ny
        self.index = common_node.ny
        self.q_mvar = common_node.uhom ** 2 * common_node.bsh * 0.000001
