class CommonBranch:
    """Ветвь, которая будет извлекаться из Растра (или Экселя)"""
    def __init__(self, r=0.0, x=0.0, b=0.0, kti=0, name="", ip=0, iq=0, np=0):
        self.r = r
        self.x = x
        self.b = b
        self.kti = kti
        self.name = name
        self.ip = ip
        self.iq = iq
        self.np = np


class CommonNode:
    """Узел, который будет извлекаться из Растра (или Экселя)"""
    def __init__(self, ny=0, name="", uhom=0.0,
                 nsx=0, na=0, pn=0.0, qn=0.0,
                 pg=0.0, qg=0.0, vzd=0.0,
                 qmin=0.0, qmax=0.0):
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
