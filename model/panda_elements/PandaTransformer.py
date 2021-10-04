from model.CommonFlow import *
import math


class PandaTransformer:
    name: str
    hv_bus: int
    lv_bus: int
    vn_hv_kv: float
    vn_lv_kv: float
    sn_mva: float = 100.0
    vk_percent: float
    vkr_percent: float
    i0_percent: float
    shift_degree: float
    in_service: bool = True

    def __init__(self):
        pass

    def __init__(self, common_branch: CommonBranch, high_voltage: float):
        module = (common_branch.ktr ** 2 + common_branch.kti ** 2) ** 0.5
        phase = math.atan(-common_branch.kti / common_branch.ktr) * (180 / math.pi)
        self.name = common_branch.name
        self.hv_bus = common_branch.ip
        self.lv_bus = common_branch.iq
        self.vn_hv_kv = high_voltage
        self.vn_lv_kv = high_voltage * module
        self.shift_degree = phase
        x = common_branch.x
        r = common_branch.r
        uhom = high_voltage
        xk = x / (uhom**2)
        rk = r / (uhom**2)
        zk = math.sqrt(xk**2 + rk**2)
        self.vk_percent = zk * 100 * self.sn_mva
        self.vkr_percent = rk * 100 * self.sn_mva

