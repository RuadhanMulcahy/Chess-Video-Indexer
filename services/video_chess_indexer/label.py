class Label():
    def __init__(self, id, x_center, y_center, w, h, conf):
        self.id = id
        self.x_center = float(x_center)
        self.y_center = float(y_center)
        self.w = float(w)
        self.h = float(h)
        self.conf = float(conf)