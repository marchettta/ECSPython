class Compoment_t:
    base_ID = 0
    def __init__(self):
        self.ID = Compoment_t.base_ID
        Compoment_t.base_ID += 1