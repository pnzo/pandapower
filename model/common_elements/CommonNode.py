class CommonNode:
    """Узел, который будет извлекаться из Растра (или Экселя)"""
    def __init__(self, ny: int, name: str, uhom: float,
                 nsx: int, na: int, pn: float, qn: float,
                 pg: float, qg: float, vzd: float,
                 qmin: float, qmax: float, bsh: float, options: str = ""):
        self.ny = ny
        self.name = name
        self.uhom = uhom
        self.nsx = nsx
        self.na = na
        self.pn = pn
        self.qn = qn
        self.pg = pg
        self.qg = qg
        self.vzd = vzd
        self.qmin = qmin
        self.qmax = qmax
        self.bsh = bsh
        self.options = options
        if self.options is None:
            self.options = ""

    def __str__(self):
        return self.name
