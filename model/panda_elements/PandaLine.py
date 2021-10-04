from model.CommonFlow import *
import math


class PandaLine:
    name: str
    from_bus: int
    to_bus: int
    r_ohm_per_km: float
    x_ohm_per_km: float
    c_nf_per_km: float
    in_service: bool = True

    def __init__(self):
        pass

    def __init__(self, common_branch: CommonBranch):
        self.name = common_branch.name
        self.from_bus = common_branch.ip
        self.to_bus = common_branch.iq
        self.r_ohm_per_km = common_branch.r
        self.x_ohm_per_km = common_branch.x
        self.c_nf_per_km = -common_branch.b * 1000 / (2 * math.pi * 50)
