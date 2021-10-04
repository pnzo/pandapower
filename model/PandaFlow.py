from model.panda_elements.PandaLine import PandaLine
from model.panda_elements.PandaActiveLoad import PandaActiveLoad
from model.panda_elements.PandaReactiveLoad import PandaReactiveLoad
from model.panda_elements.PandaBus import PandaBus
from model.panda_elements.PandaGenerator import PandaGenerator
from model.panda_elements.PandaExtGrid import PandaExtGrid
from model.panda_elements.PandaShunt import PandaShunt
from model.panda_elements.PandaTransformer import PandaTransformer
from model.CommonFlow import CommonFlow
from typing import List


class PandaFlow:
    buses: List[PandaBus] = []
    lines: List[PandaLine] = []
    active_loads: List[PandaActiveLoad] = []
    reactive_loads: List[PandaReactiveLoad] = []
    shunts: List[PandaShunt] = []
    ext_grids: List[PandaExtGrid] = []
    generators: List[PandaGenerator] = []
    transformers: List[PandaTransformer] = []

    def __init__(self):
        pass

    def __init__(self, common_flow: CommonFlow):
        for common_branch in common_flow.branches:
            if common_branch.ktr != 0:
                ip_transformer_node_uhom = next(x for x in common_flow.nodes if x.ny == common_branch.ip).uhom
                self.transformers.append(PandaTransformer(common_branch, ip_transformer_node_uhom))
            if common_branch.ktr == 0:
                self.lines.append(PandaLine(common_branch))
        for common_node in common_flow.nodes:
            self.buses.append(PandaBus(common_node))
            if common_node.pn != 0:
                load_characteristic = next(x for x in common_flow.load_characteristics if common_node.nsx == x.nsx)
                self.active_loads.append(PandaActiveLoad(common_node, load_characteristic))
            if common_node.qn != 0:
                load_characteristic = next(x for x in common_flow.load_characteristics if common_node.nsx == x.nsx)
                self.reactive_loads.append(PandaReactiveLoad(common_node, load_characteristic))
            if 'base' in common_node.options:
                self.ext_grids.append(PandaExtGrid(common_node))
            if common_node.bsh != 0:
                self.shunts.append(PandaShunt(common_node))
            if common_node.vzd != 0 and 'base' not in common_node.options:
                self.generators.append(PandaGenerator(common_node))
