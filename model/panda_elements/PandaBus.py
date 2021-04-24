from model.CommonFlow import *


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
