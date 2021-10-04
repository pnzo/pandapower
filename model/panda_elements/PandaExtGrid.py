from model.CommonFlow import *


class PandaExtGrid:
    name: str
    bus: int
    vm_pu: float
    va_degree: float = 0.0
    in_service: bool = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.bus = common_node.ny
        self.vm_pu = common_node.vzd / common_node.uhom
