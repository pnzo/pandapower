from model.CommonFlow import *
import math


class PandaLine:
    name = ''
    from_bus = 0
    to_bus = 0
    length_km = 1.0
    r_ohm_per_km = 0.0
    x_ohm_per_km = 0.0
    c_nf_per_km = 0.0
    max_i_ka = 0.0
    parallel = 0
    in_service = True

    def __init__(self):
        pass

    def __init__(self, common_branch: CommonBranch):
        self.name = common_branch.name
        self.from_bus = common_branch.ip
        self.to_bus = common_branch.iq
        self.r_ohm_per_km = common_branch.r
        self.x_ohm_per_km = common_branch.x
        self.c_nf_per_km = -common_branch.b * 1000 / (2 * math.pi * 50)
