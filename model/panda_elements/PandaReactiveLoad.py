from model.CommonFlow import *


class PandaReactiveLoad:
    name: str
    bus = 0
    q_mvar: float
    const_z_percent: float
    const_i_percent: float
    in_service: bool = True

    def __init__(self):
        pass

    def __init__(self, common_node: CommonNode, common_load_characteristic: CommonLoadCharacteristic):
        self.name = common_node.name + " Qн"
        self.bus = common_node.ny
        self.q_mvar = common_node.qn
        self.const_i_percent = common_load_characteristic.q1 * 100.0
        self.const_z_percent = common_load_characteristic.q2 * 100.0
