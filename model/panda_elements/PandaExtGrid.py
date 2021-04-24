from model.CommonFlow import *


class PandaExtGrid:
    name = ''
    bus = 0
    index = 0
    vm_pu = 1.0
    va_degree = 0.0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.bus = common_node.ny
        self.vm_pu = common_node.vzd / common_node.uhom
