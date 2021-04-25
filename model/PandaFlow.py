from model.panda_elements.PandaLine import PandaLine
from model.panda_elements.PandaLoad import PandaLoad
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
    loads: List[PandaLoad] = []
    shunts: List[PandaShunt] = []
    ext_grids: List[PandaExtGrid] = []
    generators: List[PandaGenerator] = []
    transformers: List[PandaTransformer] = []

    def __init__(self):
        pass

    def __init__(self, common_flow: CommonFlow):
        for common_branch in common_flow.branches:
            if common_branch.ktr != 0:
                ip_transformer_node_uhom = next((x for x in common_flow.nodes if x.ny == common_branch.ip)).uhom
                self.transformers.append(PandaTransformer(common_branch, ip_transformer_node_uhom))
            if common_branch.ktr == 0:
                self.lines.append(PandaLine(common_branch))
        for common_node in common_flow.nodes:
            self.buses.append(PandaBus(common_node))
            if common_node.pn != 0 or common_node.qn != 0:
                self.loads.append(PandaLoad(common_node))
            if 'base' in common_node.options:
                self.ext_grids.append(PandaExtGrid(common_node))
            if common_node.bsh != 0:
                self.shunts.append(PandaShunt(common_node))
            if common_node.vzd != 0 and 'base' not in common_node.options:
                self.generators.append(PandaGenerator(common_node))
