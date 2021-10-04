from model.CommonFlow import *


class PandaBus:
    name: str
    vn_kv: float
    in_service: bool = True
    index: int

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode):
        self.name = common_node.name
        self.index = common_node.ny
        self.vn_kv = common_node.uhom
