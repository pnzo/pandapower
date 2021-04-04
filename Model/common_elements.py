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
