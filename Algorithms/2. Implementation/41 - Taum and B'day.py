def taumBday(b, w, bc, wc, z):
    if abs(bc - wc) > z:
        if bc > wc:
            return w * wc + b * (wc + z)
        elif bc < wc:
            return b * bc + w * (bc + z)
    else:
        return b * bc + w * wc

# OR

def taumBday(b, w, bc, wc, z):
    return b * min(bc, wc + z) + w * min(wc, bc + z)