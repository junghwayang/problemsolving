def kangaroo(x1, v1, x2, v2):
    return "YES" if v1 > v2 and (x1-x2) % (v2-v1) == 0 else "NO"

"""
It's simple when we use equation.
When the number of `jump` is same, two kangaroos will meet.

x1 + (v1 * jump) = x2 + (v2 * jump)
x1 - x2 = (v2 - v1) * jump
(x1 - x2) / (v2 - v1) = jump

`jump` should be an integer, so when `(x1-x2) % (v2-v1) == 0`, kangaroos will meet finally!
"""