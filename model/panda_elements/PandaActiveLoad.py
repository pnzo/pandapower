from model.CommonFlow import *


class PandaActiveLoad:
    name: str
    bus: int
    p_mw: float
    const_z_percent: float
    const_i_percent: float
    in_service: bool = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode, common_load_characteristic: CommonLoadCharacteristic):
        self.name = common_node.name + " Pн"
        self.bus = common_node.ny
        self.p_mw = common_node.pn
        self.const_i_percent = common_load_characteristic.p1 * 100.0
        self.const_z_percent = common_load_characteristic.p2 * 100.0
