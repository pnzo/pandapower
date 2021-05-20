from model.CommonFlow import *
import math


class PandaTransformer:
    name = ''
    hv_bus = 0
    lv_bus = 0
    vn_hv_kv = 0.0
    vn_lv_kv = 0.0
    sn_mva = 100.0
    vk_percent = 0.0
    vkr_percent = 0.0
    i0_percent = 0.0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_branch: CommonBranch, high_voltage: float):
        self.name = common_branch.name
        self.hv_bus = common_branch.ip
        self.lv_bus = common_branch.iq
        self.vn_hv_kv = high_voltage
        self.vn_lv_kv = high_voltage * common_branch.ktr
        x = common_branch.x
        r = common_branch.r
        uhom = high_voltage
        xk = x / (uhom**2)
        rk = r / (uhom**2)
        zk = math.sqrt(xk**2 + rk**2)
        self.vk_percent = zk * 100 * self.sn_mva
        self.vkr_percent = rk * 100 * self.sn_mva

