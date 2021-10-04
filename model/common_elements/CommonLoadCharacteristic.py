class CommonLoadCharacteristic:
    """СХН, которая будет извлекаться из Растра (или Экселя)"""
    def __init__(self, nsx=0, p0=0.0, p1=0.0, p2=0.0, q0=0.0, q1=0.0, q2=0.0):
        self.nsx = nsx
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2

    def __str__(self):
        return str(self.nsx)
