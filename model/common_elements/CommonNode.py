class CommonNode:
    """Узел, который будет извлекаться из Растра (или Экселя)"""
    def __init__(self, ny=0, name="", uhom=0.0,
                 nsx=0, na=0, pn=0.0, qn=0.0,
                 pg=0.0, qg=0.0, vzd=0.0,
                 qmin=0.0, qmax=0.0, bsh=0.0, options=''):
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
            self.options = ''

    def __str__(self):
        return self.name
